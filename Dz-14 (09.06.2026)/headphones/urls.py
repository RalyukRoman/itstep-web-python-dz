from django.urls import path
from . import views

urlpatterns = [
    path('', views.headphone_detail, name='headphone_detail'),
]