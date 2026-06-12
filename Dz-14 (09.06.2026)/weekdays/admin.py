from django.contrib import admin
from .models import Weekday


@admin.register(Weekday)
class WeekdayAdmin(admin.ModelAdmin):
    """Налаштування адмін-панелі для моделі дня тижня."""
    
    list_display = ('id', 'name', 'image_path')

    search_fields = ('name', 'image_path')
    ordering = ('id',)