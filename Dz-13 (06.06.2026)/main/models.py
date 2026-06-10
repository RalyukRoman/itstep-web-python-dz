from django.db import models

class Writer(models.Model):
    """Модель для письменників."""

    name = models.CharField("Повне ім'я", max_length=100)
    slug = models.SlugField("Ідентифікатор", max_length=100, unique=True)
    bio = models.TextField("Біографія", blank=True)

    class Meta:
        verbose_name = "Письменник"
        verbose_name_plural = "Письменники"

    def __str__(self):
        return self.name


class Book(models.Model):
    """Модель для книг."""

    writer = models.ForeignKey(
        Writer, 
        on_delete=models.CASCADE, 
        related_name='books',
        verbose_name="Автор"
    )

    title = models.CharField("Назва", max_length=100)
    slug = models.SlugField("Ідентифікатор", max_length=100, unique=True)
    description = models.TextField("Опис", blank=True)
    publication_year = models.PositiveIntegerField("Рік видання")

    top_place = models.PositiveIntegerField(
        "Місце в топі", 
        blank=True,
        null=True, 
        unique=True
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['top_place']

    def __str__(self):
        return f"{self.title} ({self.writer.name})"
