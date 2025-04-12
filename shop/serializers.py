from rest_framework import serializers
from .models import Product, ProductCategory

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=ProductCategory.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'slug', 'description', 'price', 'sale_price',
            'image', 'category', 'category_id', 'in_stock', 'featured'
        ]
