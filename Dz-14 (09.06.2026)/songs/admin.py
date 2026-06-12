from django.contrib import admin
from .models import SongTranslation


@admin.register(SongTranslation)
class SongTranslationAdmin(admin.ModelAdmin):
    """Налаштування адмін-панелі для моделі перекладу пісні."""
    
    list_display = ('lang_code', 'title', 'artist')

    search_fields = ('title', 'lyrics', 'artist')
    ordering = ('lang_code',)
