from rest_framework import serializers
from decimal import Decimal
from .models import Category, Product, Review


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField(read_only=True)

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


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'ratings', 'comment']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)
