from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'stock_quantity', 'image_url', 'created_date']

    def validate(self, data):
        """Validate required fields."""
        if data['price'] <= 0:
            raise serializers.ValidationError("Price must be greater than 0")
        if data['stock_quantity'] < 0:
            raise serializers.ValidationError("Stock quantity cannot be negative")
        return data