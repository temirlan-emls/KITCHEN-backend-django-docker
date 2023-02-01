from unicodedata import category
from django.db.models import Q
from django.http import Http404

from apps.products.serializers import ProductSerializer, SubCategorySerializer, CategorySerializer, CategoriesSerializer, SubCategoriesSerializer
from apps.products.models import Product, Category, SubCategory

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

import random

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True, context={"request": request})
        return Response(serializer.data)

class RandomProductsList(APIView):
    def get(self, request, format=None):
        products = list(Product.objects.all())
        random_items = random.sample(products, 7)
        serializer = ProductSerializer(random_items, many=True, context={"request": request})
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, sub_category_slug, product_slug):
            try:
                return Product.objects.filter(sub_category__slug=sub_category_slug).get(slug=product_slug)
            except Product.DoesNotExist:
                raise Http404

    def get(self, request, category_slug,  sub_category_slug, product_slug, format=None):
        category = Category.objects.filter(slug=category_slug).values_list('id', flat=True)[0]
        subcategory = SubCategory.objects.filter(slug=sub_category_slug).values_list('category_id', flat=True)[0]
        if category == subcategory:
            product = self.get_object(sub_category_slug,product_slug)
            serializer = ProductSerializer(product, context={"request": request})
            return Response(serializer.data)
        else:
            raise Http404


class SubCategoryDetails(APIView):
    def get_object(self, category_slug, sub_category_slug):
            try:
                category = Category.objects.filter(slug=category_slug).values_list('id', flat=True)[0]
                return SubCategory.objects.filter(category_id=category).get(slug=sub_category_slug)
            except Product.DoesNotExist:
                raise Http404

    def get(self, request, category_slug,  sub_category_slug, format=None):
        sub_category = self.get_object(category_slug, sub_category_slug)
        serializer = SubCategorySerializer(sub_category, context={"request": request})
        return Response(serializer.data)


class CategoryDetails(APIView):
    def get_object(self, category_slug):
            try:
                return Category.objects.get(slug=category_slug)
            except Product.DoesNotExist:
                raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category, context={"request": request})
        return Response(serializer.data)


class GetCategory(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategoriesSerializer(categories, many=True, context={"request": request})
        return Response(serializer.data)

class GetSubCategory(APIView):
    def get_object(self, category_slug):
            try:
                category = Category.objects.filter(slug=category_slug).values_list('id', flat=True)[0]
                return SubCategory.objects.filter(category_id=category).values()
            except SubCategory.DoesNotExist:
                raise Http404

    def get(self, request, category_slug, format=None):
        sub_category = self.get_object(category_slug)
        serializer = SubCategoriesSerializer(sub_category, many=True, context={"request": request})
        return Response(serializer.data)

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        product = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(slug__icontains=query))


        serializer = ProductSerializer(product, many=True, context={"request": request})
        return Response(serializer.data)
    else:
        return Response({'products': []})










# from apps.products.models import Product, Category, SubCategory
# from apps.products.serializers import ProductSerializer
# from django.http import JsonResponse



# def getCategories(request): 
#     data = Category.objects.all().values()
#     return JsonResponse({'Categories': list(data)})

# def getSubCategories(request, category): 
#     categ_id = Category.objects.all().filter(slug=category).values_list('id', flat=True)
#     sub_categ = SubCategory.objects.all().filter(category_id=int(categ_id[0])).values()
#     return JsonResponse({'SubCategories': list(sub_categ)})

# def getSubCategory(request, subcategory): 
#     subcateg_id = SubCategory.objects.all().filter(slug=subcategory).values_list('id', flat=True)
#     products = Product.objects.all().filter(sub_category=int(subcateg_id[0])).values()
#     print(products)
#     return JsonResponse({'Products': list(products)})

# def getProduct(request, product): 
#     data = Product.objects.get(slug=product)
#     serializer = ProductSerializer(data)
#     return JsonResponse({'Product': serializer.data})
