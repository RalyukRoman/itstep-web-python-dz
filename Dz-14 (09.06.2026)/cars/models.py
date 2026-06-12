from django.db import models


class CarBrand(models.Model):
    """Модель для автомобільного бренду."""

    slug = models.SlugField("Ідентифікатор", max_length=100, unique=True)

    name = models.CharField("Назва", max_length=100)
    description = models.TextField("Описання", blank=True)

    class Meta:
        verbose_name = "Автомобільний бренд"
        verbose_name_plural = "Автомобільні бренди"

    def __str__(self):
        return self.name
