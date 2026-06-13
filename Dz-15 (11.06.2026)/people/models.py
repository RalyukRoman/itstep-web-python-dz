from django.db import models

class Person(models.Model):
    """Модель людини"""
    full_name = models.CharField("ПІБ", max_length=50)
    city = models.CharField("Місто", max_length=50)
    email = models.EmailField("Email", null=True)
    birthday = models.DateField("День народження")

    def __str__(self):
        return self.full_name
