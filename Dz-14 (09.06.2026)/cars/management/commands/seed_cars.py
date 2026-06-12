from django.core.management.base import BaseCommand
from cars.models import CarBrand

class Command(BaseCommand):
    help = "Заповнює базу даних автомобільними брендами"

    def handle(self, *args, **options):
        brands_data = [
            {
                "slug": "toyota",
                "name": "Toyota",
                "description": "Японська автомобільна корпорація, відома своєю надійністю та гібридними технологіями."
            },
            {
                "slug": "honda",
                "name": "Honda",
                "description": "Японський виробник автомобілів та мотоциклів, відомий високотехнологічними двигунами VTEC."
            },
            {
                "slug": "renault",
                "name": "Renault",
                "description": "Французька автомобільна компанія, один із лідерів європейського ринку комерційного автотранспорту."
            },
            {
                "slug": "bmw",
                "name": "BMW",
                "description": "Німецький виробник автомобілів преміумкласу, що орієнтується на драйв та динаміку."
            },
            {
                "slug": "tesla",
                "name": "Tesla",
                "description": "Американська компанія, яка здійснила революцію на ринку електромобілів та автопілотів."
            }
        ]

        for data in brands_data:
            brand, created = CarBrand.objects.update_or_create(
                slug=data["slug"],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f"Додано бренд: {brand.name}"
                ))
            else:
                self.stdout.write(self.style.WARNING(
                    f"Оновлено бренд: {brand.name}"
                ))