from django.db import models

class Weekday(models.Model):
    """Модель для дня тижня."""

    id = models.IntegerField(primary_key=True)  

    name = models.CharField("Назва", max_length=100)
    image_path = models.CharField("Шлях до зображення", max_length=100)

    class Meta:
        verbose_name = "День тижня"
        verbose_name_plural = "Дні тижня"

    def __str__(self):
        return self.name
