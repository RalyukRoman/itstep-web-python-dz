from django.db import models


class Headphone(models.Model):
    """Модель для навушників."""

    slug = models.SlugField("Ідентифікатор", max_length=100, unique=True)

    name = models.CharField("Назва", max_length=100)
    description = models.TextField("Описання", blank=True)

    class Meta:
        verbose_name = "Навушник"
        verbose_name_plural = "Навушники"

    def __str__(self):
        return self.name
