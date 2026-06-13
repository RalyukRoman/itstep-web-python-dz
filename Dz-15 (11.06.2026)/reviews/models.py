from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class AppReview(models.Model):
    """Модель відгуків на додатки"""
    nickname = models.CharField("Нік", max_length=50)
    email = models.EmailField("Email")
    
    # Зірки від 1 до 5
    stars = models.IntegerField(
        "Кількість зірочок", 
        validators=[
            MinValueValidator(1), 
            MaxValueValidator(5)
        ],
    )

    experience = models.TextField("Опис досвіду")
    created_at = models.DateTimeField("Дата створення", auto_now_add=True)

    def __str__(self):
        return f"Відгук від {self.nickname} ({self.stars}⭐)"


class BookReview(models.Model):
    """Модель відгуків на книги"""

    nickname = models.CharField("Нік", max_length=50)

    # Рейтинг від 0 до 100
    rating = models.IntegerField(
        "Рейтинг книги",
        validators=[
            MinValueValidator(0), 
            MaxValueValidator(100)
        ],
    )
    
    review_text = models.TextField("Рецензія на книгу")
    has_spoilers = models.BooleanField("Містить спойлери", default=False)
    created_at = models.DateTimeField("Дата створення", auto_now_add=True)

    def __str__(self):
        return f"Рецензія від {self.nickname} - {self.rating}/100"
