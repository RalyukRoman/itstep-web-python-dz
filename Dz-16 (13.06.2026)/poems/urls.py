from django.urls import path
from . import views

urlpatterns = [
    path('poems/random/', views.get_random_poem, name='get_random_poem'),
    
    path('authors/', views.get_authors, name='get_authors'),
    path('authors/<slug:author_slug>/poems/', views.get_author_poems_titles, name='get_author_poems'),
    path('authors/<slug:author_slug>/poems/random/', views.get_author_random_poem, name='get_author_random_poem'),

    path('themes/', views.get_themes, name='get_themes'),
    path('themes/<slug:theme_slug>/poems/', views.get_theme_poems_titles, name='get_theme_poems'),
    path('themes/<slug:theme_slug>/poems/random/', views.get_theme_random_poem, name='get_theme_random_poem'),
]
