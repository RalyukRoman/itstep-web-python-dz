from django.contrib import admin
from .models import Author, Poem


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Налаштування адмін-панелі для моделі автора"""

    list_display = ('name', 'bio')
    prepopulated_fields = {'slug': ('name',)}

    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    """Налаштування адмін-панелі для моделі поеми"""

    list_display = ('title', 'author', 'content')

    search_fields = ('title', 'author')
    ordering = ('title', 'author')
