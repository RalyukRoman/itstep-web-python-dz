from django.core.management.base import BaseCommand
from predictions.models import Prediction


class Command(BaseCommand):
    help = "Заповнює базу даних передбаченнями"

    def handle(self, *args, **options):
        
        # =============================================================
        #  Додати передбачення 
        # =============================================================

        predicitions_data = [
            {"text": "Сьогодні на вас чекає приємний сюрприз."},
            {"text": "Будьте уважні до дрібниць, вони змінять ваше життя."},
            {"text": "Ваша енергія приверне нові можливості."},
            {"text": "Не бійтеся ризикувати – успіх на вашому боці."},
            {"text": "Чекайте на важливу звістку до кінця тижня."},
            {"text": "Час для відпочинку – ви це заслужили."},
            {"text": "Нове знайомство виявиться дуже корисним."},
            {"text": "Ваші зусилля нарешті принесуть плоди."},
            {"text": "Зверніть увагу на своє здоров'я та внутрішній спокій."},
            {"text": "Гармонія вдома принесе успіх у всіх справах."},
        ]

        for data in predicitions_data:
            prediction, created = Prediction.objects.get_or_create(
                text=data["text"]
            )

            if created:
                self.stdout.write(self.style.SUCCESS(
                    f"Додано передбачення: «{prediction.text}»"
                ))
            else:
                self.stdout.write(self.style.WARNING(
                    f"Передбачення вже існує: «{prediction.text}»"
                ))