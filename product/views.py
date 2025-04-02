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
        products_data.is_valid(raise_exception=True)
        products_data.save()
        return Response(products_data.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    if request.method == 'GET':
        product = get_object_or_404(Product, pk=pk)
        product_data = ProductSerializer(product)
        return Response(product_data.data)

    if request.method == 'PUT':
        product = get_object_or_404(Product, pk=pk)
        product_data = ProductSerializer(product, data=request.data)
        product_data.is_valid(raise_exception=True)
        product_data.save()
        return Response(product_data.data)

    if request.method == 'DELETE':
        product = get_object_or_404(Product, pk=pk)
        copy_product = product
        product.delete()
        temp_product = ProductSerializer(copy_product)
        return Response(temp_product.data, status=status.HTTP_204_NO_CONTENT)


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
