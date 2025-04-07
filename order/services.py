from .models import Cart, Order, OrderItem
from django.db import transaction
from rest_framework.exceptions import PermissionDenied, ValidationError


class OrderService:
    @staticmethod
    def create_order(user_id, cart_id):
        with transaction.atomic():
            cart = Cart.objects.get(pk=cart_id)
            cart_items = cart.cart_items.select_related('product').all()
            total_price = sum(
                [item.product.price * item.quantity for item in cart_items])

            order = Order.objects.create(
                user_id=user_id, total_price=total_price)
            order_items = [
                OrderItem(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity,
                    total_price=item.product.price * item.quantity,
                ) for item in cart_items
            ]
            OrderItem.objects.bulk_create(order_items)
            cart.delete()

            return order

    @staticmethod
    def cancel_order(order, user):
        if user.is_staff:
            order.status = Order.CANCELED
            order.save()
            return order

        if user != order.user:
            raise PermissionDenied(
                {'details': 'You can only cancel you own order'})

        if order.status == order.DELIVERED:
            raise ValidationError(
                {'details': "Order already delivered. You can't cancel the order"})

        order.status = Order.CANCELED
        order.save()
        return order
