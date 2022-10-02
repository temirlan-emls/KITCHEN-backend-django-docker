"""kitchen_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.products  import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', views.getProducts, name='Products'),
    path('api/categories/', views.getCategories, name='Categories'),
    path('api/categories/<str:category>/', views.getSubCategory, name='SubCategories'),
    # path('api/subcategories/', views.getSubCategories, name='SubCategories'),
    # path('api/product/<int:id>', views.product, name='product'),
    # path('api/product/categories/', views.categories, name='categories'),
    # path('api/product/category/', views.category, name='category'),
    # path('api/<str:prod_categ>/<str:prod_subcateg>', views.categories, name='categories'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
