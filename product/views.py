from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django.db.models import Count


@api_view(['GET', 'POST'])
def all_products(request):
    if request.method == 'GET':
        products = Product.objects.select_related('category').all()
        products_data = ProductSerializer(products, many=True)
        return Response(products_data.data)

    if request.method == 'POST':
        products_data = ProductSerializer(data=request.data)

        if products_data.is_valid():
            products_data.save()
            return Response(products_data.data, status=status.HTTP_201_CREATED)

        else:
            return Response(products_data.error, status=status.HTTP_400_BAD_REQUEST)


@api_view()
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product_data = ProductSerializer(product, context={'request': request})
    return Response(product_data.data)


@api_view()
def all_categories(request):
    categories = Category.objects.annotate(
        product_count=Count('products')
    )
    categories_data = CategorySerializer(categories, many=True)
    return Response(categories_data.data)


@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category_data = CategorySerializer(category)
    return Response(category_data.data)
