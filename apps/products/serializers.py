from rest_framework import serializers
from apps import products
from apps.products.models import Product, Category, SubCategory

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product 
        fields = (
            'id',
            'slug',
            'name',
            'code',
            'image',
            'properties',
            'description',
            'review',
            'price',
            'get_absolute_url',
            'get_thumbnail',
        )

class SubCategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta: 
        model = SubCategory 
        fields = (
            'id',
            'slug',
            'sub_category_icon',
            'sub_category_name',
            'sub_category_name',
            'get_absolute_url',
            'products'
        )

class SubCategoriesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SubCategory 
        fields = (
            'id',
            'slug',
            'sub_category_image',
            'sub_category_icon',
            'sub_category_name',
            'get_absolute_url',
        )

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategoriesSerializer(many=True)
    class Meta: 
        model = Category 
        fields = (
            'id',
            'slug',
            'category_name',
            'category_image',
            'category_icon',
            'get_absolute_url',
            'subcategories',
        )

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category 
        fields = (
            'id',
            'slug',
            'category_name',
            'category_image',
            'category_icon',
            'get_absolute_url',
        )