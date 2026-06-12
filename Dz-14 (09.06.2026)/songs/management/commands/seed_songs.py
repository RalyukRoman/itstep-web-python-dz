from django.core.management.base import BaseCommand
from songs.models import SongTranslation

class Command(BaseCommand):
    help = "Заповнює базу даних перекладами пісні Queen - We Are The Champions"

    def handle(self, *args, **options):
        songs_data = [
            {
                "lang_code": "en",
                "title": "We Are The Champions",
                "artist": "Queen",
                "lyrics": "We are the champions, my friends\nAnd we'll keep on fighting till the end"
            },
            {
                "lang_code": "fr",
                "title": "Nous Sommes Les Champions",
                "artist": "Queen",
                "lyrics": "Nous sommes les champions, mon ami\nEt nous continuerons à nous battre jusqu'à la fin"
            },
            {
                "lang_code": "de",
                "title": "Wir Sind Die Champions",
                "artist": "Queen",
                "lyrics": "Wir sind die Champions, mein Freund\nUnd wir werden далі kämpfen bis zum Ende"
            },
            {
                "lang_code": "es",
                "title": "Somos Los Campeones",
                "artist": "Queen",
                "lyrics": "Somos los campeones, amigo mío\nY seguiremos luchando hasta el final"
            },
            {
                "lang_code": "uk",
                "title": "Ми — Чемпіони",
                "artist": "Queen",
                "lyrics": "Ми чемпіони, мій друже\nІ ми продовжимо боротися до самого кінця"
            }
        ]

        for data in songs_data:
            song, created = SongTranslation.objects.update_or_create(
                lang_code=data["lang_code"],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f"Додано переклад для мови: {song.lang_code}"
                ))
            else:
                self.stdout.write(self.style.WARNING(
                    f"Оновлено переклад для мови: {song.lang_code}"
                ))