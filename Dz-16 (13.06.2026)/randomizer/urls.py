from django.urls import path
from . import views

urlpatterns = [
    path('numbers/random/', views.get_random_numbers, name='get_random_numbers')
]
