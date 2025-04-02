from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django.db.models import Count


@api_view()
def all_products(request):
    products = Product.objects.select_related('category').all()
    products_data = ProductSerializer(
        products, many=True, context={'request': request})
    return Response(products_data.data)


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
