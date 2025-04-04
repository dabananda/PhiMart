from rest_framework import serializers
from .models import Cart, CartItem
from product.models import Product


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']


class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'quantity']

    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        try:
            cart_item = CartItem.objects.get(
                cart_id=cart_id, product_id=product_id)
            cart_item.quantity += quantity
            self.instance = cart_item.save()
        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(
                cart_id=cart_id, **self.validated_data)

        return self.instance

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError(
                f"Product with id {value} doesn't exist!")
        return value


class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField(
        method_name='get_total_price')

    class Meta:
        model = CartItem
        fields = ['id', 'quantity', 'total_price', 'product']

    def get_total_price(self, cart_item: CartItem):
        return cart_item.quantity * cart_item.product.price


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(
        method_name='get_total_price')

    class Meta:
        model = Cart
        fields = ['id', 'user', 'total_price', 'cart_items']

    def get_total_price(self, cart: Cart):
        return sum(
            [item.product.price * item.quantity for item in cart.cart_items.all()])
