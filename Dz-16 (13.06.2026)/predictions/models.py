from django.db import models


class Prediction(models.Model):
    """Модель передбачення"""

    text = models.TextField()

    def __str__(self):
        return self.text

