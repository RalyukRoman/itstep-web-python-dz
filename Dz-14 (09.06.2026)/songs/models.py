from django.db import models


class SongTranslation(models.Model):
    """Модель для перекладу пісень."""

    lang_code = models.CharField(max_length=5, unique=True) 
    
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    lyrics = models.TextField()

    class Meta:
        verbose_name = "Переклад пісні"
        verbose_name_plural = "Переклади пісень"

    def __str__(self):
        return f"{self.lang_code} - {self.title}"
