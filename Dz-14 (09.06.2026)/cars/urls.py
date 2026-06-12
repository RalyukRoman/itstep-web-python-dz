from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars_main, name='cars_main'),
    path('<str:car_brand_slug>/', views.car_brand, name='car_brand'),
]