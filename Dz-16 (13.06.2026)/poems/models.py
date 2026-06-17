from django.db import models


class Author(models.Model):
    """Модель автора"""

    name = models.CharField("ПІБ", max_length=100)
    slug = models.SlugField("Ідентифікатор", unique=True)
    bio = models.TextField("Біографія")

    def __str__(self):
        return self.name
    

class Theme(models.Model):
    """Модель тематики"""

    name = models.CharField("Назва теми", max_length=100)
    slug = models.SlugField("Ідентифікатор", unique=True)

    def __str__(self):
        return self.name


class Poem(models.Model):
    """Модель поэми"""

    title = models.CharField("Назва", max_length=200)
    content = models.TextField("Зміст")

    themes = models.ManyToManyField(
        Theme, 
        related_name='poems',
        verbose_name="Тематики"
    )
    
    author = models.ForeignKey(
        Author, models.CASCADE, 
        related_name='poems',
        verbose_name="Автор"
    )

    def __str__(self):
        return self.title
