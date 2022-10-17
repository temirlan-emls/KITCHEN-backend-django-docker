from rest_framework import serializers
from apps import products
from apps.products.models import Product, Category, SubCategory
from django.conf import settings

class ProductSerializer(serializers.ModelSerializer):
    title_image_url = serializers.SerializerMethodField()
    thumbnail_url = serializers.SerializerMethodField()
    second_image_url = serializers.SerializerMethodField()
    third_image_url = serializers.SerializerMethodField()
    sub_category_slug = serializers.SerializerMethodField()
    category_slug = serializers.SerializerMethodField()

    class Meta: 
        model = Product 
        fields = (
            'id',
            'slug',
            'name',
            'code',
            'price',
            'description',
            'dimensions',
            'consumption',
            'properties',
            'title_image_url',
            'thumbnail_url',
            'second_image_url',
            'third_image_url',
            'review',
            'get_thumbnail',
            'sub_category_slug',
            'category_slug',
        )
        
    def get_sub_category_slug(self, product):
        subcategory = SubCategory.objects.filter(id=product.sub_category.id)
        return subcategory.values_list('slug', flat=True)[0]

    def get_category_slug(self, product):
        subcategory = SubCategory.objects.filter(id=product.sub_category.id)
        category_id = subcategory.values_list('category_id', flat=True)[0]
        category = Category.objects.filter(id=category_id)
        return category.values_list('slug', flat=True)[0]

    def get_title_image_url(self, product):
        if product.title_image == '':
            return None
        else:
            request = self.context.get('request')
            photo_url = product.title_image.url
            return request.build_absolute_uri(photo_url)

    def get_thumbnail_url(self, product):
        if product.thumbnail == '':
            return None
        else:
            request = self.context.get('request')
            photo_url = product.thumbnail.url
            return request.build_absolute_uri(photo_url)

    def get_second_image_url(self, product):
        if product.image == '':
            return None
        else:
            request = self.context.get('request')
            photo_url = product.image.url
            return request.build_absolute_uri(photo_url)

    def get_third_image_url(self, product):
        if product.image2 == '':
            return None
        else:
            request = self.context.get('request')
            photo_url = product.image2.url
            return request.build_absolute_uri(photo_url)

class SubCategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    sub_category_icon_url = serializers.SerializerMethodField()
    sub_category_image_url = serializers.SerializerMethodField()

    class Meta: 
        model = SubCategory 
        fields = (
            'id',
            'slug',
            'sub_category_icon_url',
            'sub_category_image_url',
            'sub_category_name',
            'products'
        )

    def get_sub_category_icon_url(self, subcategory):
        if subcategory.sub_category_icon == '':
            return None
        else:
            request = self.context.get('request')
            photo_url = subcategory.sub_category_icon.url
            return request.build_absolute_uri(photo_url)
    def get_sub_category_image_url(self, subcategory):
        if subcategory.sub_category_image == '':
            return None
        else:
            request = self.context.get('request')
            photo_url = subcategory.sub_category_image.url
            return request.build_absolute_uri(photo_url)

class SubCategoriesSerializer(serializers.ModelSerializer):
    sub_category_icon_url = serializers.SerializerMethodField()
    sub_category_image_url = serializers.SerializerMethodField()

    class Meta: 
        model = SubCategory 
        fields = (
            'id',
            'slug',
            'sub_category_image_url',
            'sub_category_icon_url',
            'sub_category_name',
        )

    def get_sub_category_icon_url(self, subcategory):
        if subcategory.sub_category_icon == '':
            return None
        else:
            request = self.context.get('request')
            photo_url = subcategory.sub_category_icon.url
            return request.build_absolute_uri(photo_url)

    def get_sub_category_image_url(self, subcategory):
        if subcategory.sub_category_image == '':
            return None
        else:
            request = self.context.get('request')
            photo_url = subcategory.sub_category_image.url
            return request.build_absolute_uri(photo_url)

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategoriesSerializer(many=True)
    category_icon_url = serializers.SerializerMethodField()
    category_image_url = serializers.SerializerMethodField()
    class Meta: 
        model = Category 
        fields = (
            'id',
            'slug',
            'category_name',
            'category_image_url',
            'category_icon_url',
            'subcategories',
        )

    def get_category_icon_url(self, category):
        if category.category_icon == '':
            return None
        else:
            request = self.context.get('request')
            photo_url = category.category_icon.url
            return request.build_absolute_uri(photo_url)

    def get_category_image_url(self, category):
        if category.category_image == '':
            return None
        else:
            request = self.context.get('request')
            photo_url = category.category_image.url
            return request.build_absolute_uri(photo_url)

class CategoriesSerializer(serializers.ModelSerializer):
    category_icon_url = serializers.SerializerMethodField()
    category_image_url = serializers.SerializerMethodField()
    class Meta: 
        model = Category 
        fields = (
            'id',
            'slug',
            'category_name',
            'category_image_url',
            'category_icon_url',
        )

    def get_category_icon_url(self, category):
        if category.category_icon == '':
            return None
        else:
            request = self.context.get('request')
            photo_url = category.category_icon.url
            return request.build_absolute_uri(photo_url)

    
    def get_category_image_url(self, category):
        if category.category_image == '':
            return None
        else:
            request = self.context.get('request')
            photo_url = category.category_image.url
            return request.build_absolute_uri(photo_url)