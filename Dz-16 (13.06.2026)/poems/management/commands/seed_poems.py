from django.core.management.base import BaseCommand
from poems.models import Poem, Author, Theme


class Command(BaseCommand):
    help = "Заповнює базу даних авторами, тематиками та віршами"

    def handle(self, *args, **options):
        
        # =============================================================
        #  Додати авторів 
        # =============================================================

        authors_data = [
            {
                "slug": "taras-shevchenko",
                "name": "Тарас Шевченко",
                "bio": "Видатний український поет, художник, мислитель, класик української літератури."
            },
            {
                "slug": "lesya-ukrainka",
                "name": "Леся Українка",
                "bio": "Українська письменниця, перекладачка, культурна діячка, одна з центральних постатей української культури."
            },
            {
                "slug": "ivan-franko",
                "name": "Іван Франко",
                "bio": "Видатний український письменник, поет, публіцист, перекладач, вчений, громадський і політичний діяч."
            },
            {
                "slug": "vasyl-stus",
                "name": "Василь Стус",
                "bio": "Видатний український поет-шістдесятник, перекладач, прозаїк, мислитель, правозахисник, дисидент."
            },
        ]

        for data in authors_data:
            defaults = {k: v for k, v in data.items() if k != "slug"}
            
            author, created = Author.objects.update_or_create(
                slug=data["slug"],
                defaults=defaults
            )

            if created:
                self.stdout.write(self.style.SUCCESS(
                    f"Додано автора: {author.name}"
                ))
            else:
                self.stdout.write(self.style.WARNING(
                    f"Оновлено автора: {author.name}"
                ))
        
        # =============================================================
        #  Додати тематики 
        # =============================================================

        themes_data = [
            {"slug": "peizazhna-liryka", "name": "Пейзажна лірика"},
            {"slug": "filosofska-liryka", "name": "Філософська лірика"},
            {"slug": "hromadyanska-liryka", "name": "Громадянська лірика"},
            {"slug": "intymna-liryka", "name": "Інтимна лірика"},
            {"slug": "patriotichna-liryka", "name": "Патріотична лірика"},
        ]

        for data in themes_data:
            defaults = {k: v for k, v in data.items() if k != "slug"}

            theme, created = Theme.objects.update_or_create(
                slug=data["slug"],
                defaults=defaults
            )

            if created:
                self.stdout.write(self.style.SUCCESS(
                    f"Додано тему: {theme.name}"
                ))
            else:
                self.stdout.write(self.style.WARNING(
                    f"Оновлено тему: {theme.name}"
                ))

        # =============================================================
        #  Додати вірши 
        # =============================================================

        poems_data = [
            {
                "title": "Садок вишневий коло хати",
                "content": "Садок вишневий коло хати, Хрущі над вишнями гудуть, Плугатарі з плугами йдуть...",
                "author_slug": "taras-shevchenko",
                "theme_slugs": ["peizazhna-liryka"]
            },
            {
                "title": "Реве та стогне Дніпр широкий",
                "content": "Реве та стогне Дніпр широкий, Сердитий вітер завива, Додолу верби гне високі...",
                "author_slug": "taras-shevchenko",
                "theme_slugs": ["peizazhna-liryka"]
            },
            {
                "title": "Зоре моя вечірняя",
                "content": "Зоре моя вечірняя, Зійди над горою, Поговоримо тихесенько В неволі з тобою.",
                "author_slug": "taras-shevchenko",
                "theme_slugs": ["peizazhna-liryka"]
            },
            {
                "title": "Тече вода з-під явора",
                "content": "Тече вода з-під явора Яром на долину. Пишається над водою Червона калина.",
                "author_slug": "taras-shevchenko",
                "theme_slugs": ["peizazhna-liryka"]
            },
            {
                "title": "Ой одна я, одна",
                "content": "Ой одна я, одна, як билина в полі. Та дала мені доля таку талань...",
                "author_slug": "taras-shevchenko",
                "theme_slugs": ["peizazhna-liryka"]
            },
            {
                "title": "Contra spem spero!",
                "content": "Геть те, думи, ви хмари осінні! То ж тепера весна золота! Чи то так у жалю, в голосінні...",
                "author_slug": "lesya-ukrainka",
                "theme_slugs": ["filosofska-liryka"]
            },
            {
                "title": "Слово, чому ти не твердая криця",
                "content": "Слово, чому ти не твердая криця, Що серед бою так ясно іскриться? Чом ти не гострий, безжалісний меч...",
                "author_slug": "lesya-ukrainka",
                "theme_slugs": ["filosofska-liryka"]
            },
            {
                "title": "Хотіла б я піснею стати",
                "content": "Хотіла б я піснею стати У сюю хвилину ясну, Щоб вільно по світі літати...",
                "author_slug": "lesya-ukrainka",
                "theme_slugs": ["filosofska-liryka"]
            },
            {
                "title": "Як дитиною, бувало",
                "content": "Як дитиною, бувало, Упаду собі на лихо, То хоч в серце біль доходив, Я собі вставала тихо.",
                "author_slug": "lesya-ukrainka",
                "theme_slugs": ["filosofska-liryka"]
            },
            {
                "title": "Стояла я і слухала весну",
                "content": "Стояла я і слухала весну, Весна мені багато говорила, Співала пісню дзвінку, голосну...",
                "author_slug": "lesya-ukrainka",
                "theme_slugs": ["filosofska-liryka", "peizazhna-liryka"]
            },
            {
                "title": "Без надії сподіваюсь",
                "content": "Без надії сподіваюсь, Без надії сподіваюсь, Що колись і я дождуся, Що колись і я дождуся...",
                "author_slug": "lesya-ukrainka",
                "theme_slugs": ["filosofska-liryka"]
            },
            {
                "title": "Чого являєшся мені у сні?",
                "content": "Чого являєшся мені у сні? Чого звертаєш ти до мене пишні Очі, що в них проміння грає іскорне...",
                "author_slug": "lesya-ukrainka",
                "theme_slugs": ["intymna-liryka"]
            },
            {
                "title": "Гімн",
                "content": "Вічний революціонер — Дух, що тіло рве до бою, Рве за поступ, щастя й волю, — Він живе, він ще не вмер.",
                "author_slug": "ivan-franko",
                "theme_slugs": ["hromadyanska-liryka", "patriotichna-liryka"]
            },
            {
                "title": "Каменярі",
                "content": "Я бачив дивний сон. Неначе я ішов В якійсь невідомій, неходженій дорозі...",
                "author_slug": "ivan-franko",
                "theme_slugs": ["hromadyanska-liryka"]
            },
            {
                "title": "Ой ти, дівчино, з горіха зерня",
                "content": "Ой ти, дівчино, з горіха зерня, Чом твоє серденько — колюче терня? Чом твої устоньки — тиха молитва...",
                "author_slug": "ivan-franko",
                "theme_slugs": ["intymna-liryka"]
            },
            {
                "title": "Чого являєшся мені",
                "content": "Чого являєшся мені У сні? Чого звертаєш ти до мене пишні Очі, що в них проміння грає іскорне...",
                "author_slug": "ivan-franko",
                "theme_slugs": ["intymna-liryka"]
            },
            {
                "title": "Мойсей",
                "content": "Народе мій, замучений, розбитий, Мов паралітик той на роздорожжу...",
                "author_slug": "ivan-franko",
                "theme_slugs": ["hromadyanska-liryka", "patriotichna-liryka", "filosofska-liryka"]
            },
            {
                "title": "Як добре те, що смерті не боюсь я",
                "content": "Як добре те, що смерті не боюсь я І не питаю, чи тяжкий мій хрест...",
                "author_slug": "vasyl-stus",
                "theme_slugs": ["filosofska-liryka", "patriotichna-liryka"]
            },
            {
                "title": "На колимськім морозі калина",
                "content": "На колимськім морозі калина Зацвіла понад снігом, як кров...",
                "author_slug": "vasyl-stus",
                "theme_slugs": ["patriotichna-liryka", "hromadyanska-liryka"]
            },
            {
                "title": "Верни до мене, пам'яте моя",
                "content": "Верни до мене, пам'яте моя, І не вмреш ти, і не вмреш ти, і не вмреш ти...",
                "author_slug": "vasyl-stus",
                "theme_slugs": ["filosofska-liryka"]
            },
            {
                "title": "Ярій, душе! Ярій, а не ридай",
                "content": "Ярій, душе! Ярій, а не ридай. В огні, у полум'ї, у димі, у диму...",
                "author_slug": "vasyl-stus",
                "theme_slugs": ["filosofska-liryka", "hromadyanska-liryka"]
            },
        ]

        for data in poems_data:
            author_slug = data["author_slug"]
            theme_slugs = data["theme_slugs"]
            poem_title = data["title"]

            defaults = {
                k: v for k, v in data.items() 
                if k not in ["title", "author_slug", "theme_slugs"]
            }
            
            author = Author.objects.get(slug=author_slug)
            defaults["author"] = author
            
            poem, created = Poem.objects.update_or_create(
                title=poem_title,
                defaults=defaults
            )
            
            themes = Theme.objects.filter(slug__in=theme_slugs)
            poem.themes.set(themes)

            if created:
                self.stdout.write(self.style.SUCCESS(
                    f"Додано вірш: {poem.title}"
                ))
            else:
                self.stdout.write(self.style.WARNING(
                    f"Оновлено вірш: {poem.title}"
                ))