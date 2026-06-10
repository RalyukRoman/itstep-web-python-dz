from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,  name='index'),

    # Маршрути для письменників
    path('writers/', views.writers_list, name='writers_list'),
    path('writers/<str:writer_slug>', views.writer_detail, name='writer_detail'),
    path('writers/<str:writer_slug>/<str:book_slug>', views.writer_book_detail, name='writer_book_detail'),
    path('writers/<path:undefined>', views.writers_list),

    # Маршрути для книг
    path('books/', views.books_top, name='books_top'),
    path('books/<int:book_place>', views.book_detail, name='book_detail'),
    path('books/<path:undefined>', views.books_top)
]