from django.contrib import admin
from .models import Writer, Book


@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    """Налаштування адмін-панелі для моделі письменників."""
    
    list_display = ('name', 'slug')
    
    prepopulated_fields = {'slug': ('name',)}

    search_fields = ('name', 'bio')
    ordering = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Налаштування адмін-панелі для моделі книг."""

    list_display = ('title', 'writer', 'publication_year', 'top_place', 'slug')
    list_filter = ('writer', 'publication_year')

    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('writer',)

    search_fields = ('title', 'description', 'writer__name')
    ordering = ('top_place', 'title')
