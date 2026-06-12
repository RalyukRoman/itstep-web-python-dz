from django.contrib import admin
from .models import CarBrand


@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    """Налаштування адмін-панелі для моделі автомобільної компанії."""
    
    list_display = ('name', 'slug')
    
    prepopulated_fields = {'slug': ('name',)}

    search_fields = ('name', 'description')
    ordering = ('name',)
