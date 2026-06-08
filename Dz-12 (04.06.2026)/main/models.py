from django.db import models


class News(models.Model):
    """Модель для новин"""
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст новини")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публікації")

    def __str__(self):
        return self.title
    

class CityOfficial(models.Model):
    """Модель для міських персоналів міста"""
    name = models.CharField(max_length=200, verbose_name="Ім'я")
    position = models.CharField(max_length=200, verbose_name="Посада")
    description = models.TextField(verbose_name="Опис")

    def __str__(self):
        return self.name


class Fact(models.Model):
    """Модель для цікавих фактів про місто"""
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст факту")

    def __str__(self):
        return self.title


class HistoricalPhoto(models.Model):
    """Модель для історичних фотографій"""
    title = models.CharField(max_length=200, verbose_name="Назва фото")
    description = models.TextField(verbose_name="Опис фотографії")

    # файли потраплять у media/history_photos/
    image = models.ImageField(upload_to='history_photos/', verbose_name="Фото")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата додавання")

    def __str__(self):
        return self.title
    

class HistoricalPeople(models.Model):
    """Модель для історичних людей"""
    name = models.CharField(max_length=200, verbose_name="Ім'я")
    description = models.TextField(verbose_name="Опис")
    birth_date = models.DateField(verbose_name="Дата народження")
    death_date = models.DateField(verbose_name="Дата смерті")

    def __str__(self):
        return self.name