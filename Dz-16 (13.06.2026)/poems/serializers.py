from rest_framework import serializers
from .models import Author, Poem, Theme


class AuthorSerializer(serializers.ModelSerializer):
    """Серіалізатор моделі автора"""

    class Meta:
        model = Author
        fields = '__all__'


class ThemeSerializer(serializers.ModelSerializer):
    """Серіалізатор моделі тематики"""

    class Meta:
        model = Theme
        fields = '__all__'


class PoemSerializer(serializers.ModelSerializer):
    """Серіалізатор моделі вірша"""

    author = serializers.StringRelatedField()
    themes = serializers.StringRelatedField(many=True)

    class Meta:
        model = Poem
        fields = '__all__'
