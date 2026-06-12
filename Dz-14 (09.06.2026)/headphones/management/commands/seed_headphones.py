from django.core.management.base import BaseCommand
from headphones.models import Headphone

class Command(BaseCommand):
    help = "Заповнює базу даних популярними моделями навушників"

    def handle(self, *args, **options):
        headphones_data = [
            {
                "slug": "budslive",
                "name": "Samsung Galaxy Buds Live",
                "description": "Бездротові навушники унікальної ергономічної форми (у вигляді квасолі) з активним шумозаглушенням та глибоким звуком від AKG."
            },
            {
                "slug": "airpods",
                "name": "Apple AirPods",
                "description": "Культові повністю бездротові навушники-вкладиші від Apple з процесором H1, миттєвим підключенням до iPhone та підтримкою Siri."
            },
            {
                "slug": "wh1000xm4",
                "name": "Sony WH-1000XM4",
                "description": "Повнорозмірні навушники закритого типу, що вважаються одним із світових лідерів у категорії інтелектуального шумозаглушення (ANC)."
            },
            {
                "slug": "marshall-major4",
                "name": "Marshall Major IV",
                "description": "Накладні навушники у фірмовому рок-дизайні з феноменальним часом автономної роботи — понад 80 годин бездротового відтворення."
            },
            {
                "slug": "pro-2",
                "name": "Apple AirPods Pro 2",
                "description": "Вакуумні навушники з покращеним адаптивним аудіо, персоналізованим просторовим звуком та зарядним кейсом MagSafe (USB-C)."
            }
        ]

        for data in headphones_data:
            headphone, created = Headphone.objects.update_or_create(
                slug=data["slug"],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f"Додано навушники: {headphone.name}"
                ))
            else:
                self.stdout.write(self.style.WARNING(
                    f"Оновлено навушники: {headphone.name}"
                ))