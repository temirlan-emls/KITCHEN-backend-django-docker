from apps.products.models import Product, Category, SubCategory
from apps.products.serializers import ProductSerializer
from django.http import JsonResponse


def getProducts(request): 
    data = Product.objects.all()
    serializer = ProductSerializer(data, many=True)
    return JsonResponse({'Products': serializer.data})

def getCategories(request): 
    data = Category.objects.all().values()
    return JsonResponse({'Categories': list(data)})

def getSubCategory(request, category): 
    categ_id = Category.objects.all().filter(url_name=category).values_list('id', flat=True)
    sub_categ = SubCategory.objects.all().filter(parent_id=int(categ_id[0])).values()
    print(sub_categ)
    return JsonResponse({'SubCategories': list(sub_categ)})


# def product(request, id): 
#     data = Product.objects.get(pk=id)
#     serializer = ProductSerializer(data)
#     return JsonResponse({'product': serializer.data})

# def categories(request): 
#     data = Product.objects.order_by().values_list('prod_categ', flat=True).distinct()
#     return JsonResponse({'categories': list(data)}) 

# def category(request): 
#     data = Product.objects.values_list('prod_categ')
#     return JsonResponse({'category': list(data)})
