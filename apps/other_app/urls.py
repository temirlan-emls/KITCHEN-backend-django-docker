from django.urls import path 
from apps.other_app import views

urlpatterns = [
    path('slideImg/', views.SlideImgApi.as_view()),
]