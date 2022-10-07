from django.urls import path 
from apps.file_generator import views

urlpatterns = [
    path('xlsx-generator/', views.XLSXGen),
]