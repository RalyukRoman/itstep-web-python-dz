from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_translation, {'lang_code': 'en'}, name='song_default'),
    path('<str:lang_code>/', views.song_translation, name='song_translation'),
]