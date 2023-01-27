from django.urls import path 
from apps.products import views

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
    path('products/search/', views.search),
    path('products/categories/', views.GetCategory.as_view()),
    path('products/<slug:category_slug>/subcategories/', views.GetSubCategory.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetails.as_view()),
    path('products/<slug:category_slug>/<slug:sub_category_slug>/', views.SubCategoryDetails.as_view()),
    path('product/<slug:category_slug>/<slug:sub_category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
]