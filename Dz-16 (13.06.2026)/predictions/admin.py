from django.contrib import admin
from .models import Prediction


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    """Налаштування адмін-панелі для моделі передбачення"""

    list_display = ('text',)

    search_fields = ('text',)
    ordering = ('text',)
