from django.core.management.base import BaseCommand
from weekdays.models import Weekday

class Command(BaseCommand):
    help = "Заповнює базу даних усіма 7 днями тижня"

    def handle(self, *args, **options):
        days_data = [
            {"id": 1, "name": "Понеділок", "image_path": "weekdays/images/days/monday.jpg"},
            {"id": 2, "name": "Вівторок", "image_path": "weekdays/images/days/tuesday.jpg"},
            {"id": 3, "name": "Середа", "image_path": "weekdays/images/days/wednesday.jpg"},
            {"id": 4, "name": "Четвер", "image_path": "weekdays/images/days/thursday.jpg"},
            {"id": 5, "name": "П'ятниця", "image_path": "weekdays/images/days/friday.jpg"},
            {"id": 6, "name": "Субота", "image_path": "weekdays/images/days/saturday.jpg"},
            {"id": 7, "name": "Неділя", "image_path": "weekdays/images/days/sunday.jpg"},
        ]

        for data in days_data:
            day, created = Weekday.objects.update_or_create(
                id=data["id"],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f"Додано день: {day.name}"
                ))
            else:
                self.stdout.write(self.style.WARNING(
                    f"Оновлено день: {day.name}"
                ))