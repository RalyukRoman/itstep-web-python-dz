from rest_framework import serializers
from .models import Prediction


class PredictionSerializer(serializers.ModelSerializer):
    """Серіалізатор моделі передбачення"""

    class Meta:
        model = Prediction
        fields = '__all__'