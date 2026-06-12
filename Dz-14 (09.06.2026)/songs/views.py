from django.shortcuts import render, get_object_or_404
from .models import SongTranslation


def song_translation(request, lang_code='en'):
    """Сторінка для відображення строк пісні в конкретній мові."""

    translation = get_object_or_404(
        SongTranslation, lang_code=lang_code
    )

    context = {
        'lang': lang_code,
        'song': translation
    }
    
    path = 'songs/lyrics.html'
    return render(request, path, context)
