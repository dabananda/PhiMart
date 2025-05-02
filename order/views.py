from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Cart, CartItem
from .models import Order, OrderItem
from .services import OrderService
from .serializers import CartSerializer, CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer, OrderSerializer, CreateOrderSerializer, OrderUpdateSerializer, EmptySerializer


class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Cart.objects.prefetch_related('cart_items__product').filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        existing_cart = Order.objects.filter(user=request.user).first()

        if existing_cart:
            serializer = self.get_serializer(existing_cart)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return super().create(request, *args, **kwargs)


class CartItemViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}

    def get_queryset(self):
        return CartItem.objects.select_related('product').filter(cart_id=self.kwargs['cart_pk'])


class OrderViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        order = self.get_object()
        OrderService.cancel_order(order=order, user=request.user)
        return Response({'status': "Order canceled"})

    # @action(detail=True, methods=['patch'])
    # def update_status(self, request, pk=None):
    #     order = self.get_object()
    #     serializer = UpdateCartItemSerializer(
    #         order, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response({'status': f'Order status updated to {request.data['status']}'})

    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        order = self.get_object()
        serializer = OrderUpdateSerializer(
            order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': f'Order status updated to {request.data["status"]}'
            })
        return Response(serializer.errors, status=400)

    def get_permissions(self):
        if self.action in ['update_status', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == 'cancel':
            return EmptySerializer
        if self.action == 'create':
            return CreateOrderSerializer
        if self.action == 'update_status':
            return OrderUpdateSerializer
        return OrderSerializer

    def get_serializer_context(self):
        return {'user_id': self.request.user.id, 'user': self.request.user}

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.prefetch_related('items__product').all()
        return Order.objects.prefetch_related('items__product').filter(user=self.request.user)
