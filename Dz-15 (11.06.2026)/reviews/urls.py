from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.app_reviews, name="app_reviews"),
    path('book/', views.book_reviews, name='book_reviews'),
]
