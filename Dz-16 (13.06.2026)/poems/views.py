from .serializers import PoemSerializer, AuthorSerializer, ThemeSerializer
from .models import Poem, Author, Theme

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404

import random

# =====================================================================
#  Допоміжні функції
# =====================================================================

def _get_random_object_from_queryset(queryset):
    """Повертає випадковий об'єкт з готової вибірки"""

    pks = queryset.values_list('pk', flat=True)

    if pks:
        random_id = random.choice(pks)
        return queryset.filter(pk=random_id).first()
    else:
        return None

# =====================================================================
#  Функції API
# =====================================================================

@api_view(['GET'])
def get_random_poem(request):
    """Отримати випадковий вірш"""

    queryset = Poem.objects.all()
    random_poem = _get_random_object_from_queryset(queryset)
    
    if not random_poem:
        return Response(
            {'error': 'No poems found'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = PoemSerializer(random_poem)
        
    return Response(
        serializer.data, 
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def get_author_random_poem(request, author_slug):
    """Отримати випадковий вірш конкретного автора"""

    author = get_object_or_404(Author, slug=author_slug)

    poems = Poem.objects.filter(author=author)
    random_poem = _get_random_object_from_queryset(poems)
    
    if not random_poem:
        return Response(
            {'error': 'This author has no poems yet'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = PoemSerializer(random_poem)
        
    return Response(
        serializer.data, 
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def get_theme_random_poem(request, theme_slug):
    """Отримати випадковий вірш за конкретною тематикою"""

    theme = get_object_or_404(Theme, slug=theme_slug)

    poems = Poem.objects.filter(themes=theme)
    random_poem = _get_random_object_from_queryset(poems)
    
    if not random_poem:
        return Response(
            {'error': 'No poems found for this theme'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = PoemSerializer(random_poem)
        
    return Response(
        serializer.data, 
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def get_authors(request):
    """Отримати всіх авторів"""

    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    
    return Response(
        serializer.data, 
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def get_themes(request):
    """Отримати всі тематики"""

    themes = Theme.objects.all()
    serializer = ThemeSerializer(themes, many=True)
    
    return Response(
        serializer.data, 
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def get_author_poems_titles(request, author_slug):
    """Отримати назви всіх віршів конкретного автора"""

    author = get_object_or_404(Author, slug=author_slug)

    poems = Poem.objects.filter(author=author)
    poems_titles = list(poems.values_list('title', flat=True))

    return Response(
        poems_titles, 
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def get_theme_poems_titles(request, theme_slug):
    """Отримати назви всіх віршів за вказаною тематикою"""

    theme = get_object_or_404(Theme, slug=theme_slug)

    poems = Poem.objects.filter(themes=theme)
    poems_titles = list(poems.values_list('title', flat=True))

    return Response(
        poems_titles, 
        status=status.HTTP_200_OK
    )