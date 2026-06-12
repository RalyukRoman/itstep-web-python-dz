from django.contrib import admin
from .models import Headphone


@admin.register(Headphone)
class HeadphoneAdmin(admin.ModelAdmin):
    """Налаштування адмін-панелі для моделі навушників."""
    
    list_display = ('name', 'slug')
    
    prepopulated_fields = {'slug': ('name',)}

    search_fields = ('name', 'description')
    ordering = ('name',)
