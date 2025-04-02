from rest_framework import serializers
from decimal import Decimal
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'product_count']


class ProductSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField(method_name='calc_tax')

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'price_with_tax',
                  'stock', 'category', 'created_at', 'updated_at']

    def calc_tax(self, product):
        return round(product.price * Decimal(1.18), 2)

    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError("Price must be positive")
        else:
            return price
