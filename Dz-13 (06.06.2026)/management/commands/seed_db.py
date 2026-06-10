from django.core.management.base import BaseCommand
from main.models import Writer, Book

class Command(BaseCommand):
    """Команда для наповнення бази даних тестовими даними."""
    
    help = "Наповнює базу даних початковими даними (5 письменників, 20 книг)."

    def handle(self, *args, **kwargs):
        # Дані для письменників
        writers_data = [
            {"name": "Джордж Орвелл", "slug": "george-orwell", "bio": "Англійський письменник та публіцист, автор антиутопій."},
            {"name": "Дж. Р. Р. Толкін", "slug": "jrr-tolkien", "bio": "Англійський письменник, філолог та поет, автор класичного фентезі."},
            {"name": "Ернест Гемінґвей", "slug": "ernest-hemingway", "bio": "Американський письменник, лауреат Нобелівської премії з літератури."},
            {"name": "Стівен Кінг", "slug": "stephen-king", "bio": "Американський письменник, відомий як 'Король жахів'."},
            {"name": "Агата Крісті", "slug": "agatha-christie", "bio": "Англійська письменниця, одна з найвідоміших майстрів детективного жанру."}
        ]

        writers = []
        for w in writers_data:
            writer, created = Writer.objects.get_or_create(
                slug=w['slug'],
                defaults={'name': w['name'], 'bio': w['bio']}
            )
            
            writers.append(writer)

            if created:
                self.stdout.write(self.style.NOTICE(
                    f"Створено письменника: {writer.name}"
                ))

        # Дані для книг (по 4 на кожного автора)
        books_data = [
            ("1984", "1984-novel", "Роман-антиутопія про тоталітарне суспільство.", 1949),
            ("Колгосп тварин", "animal-farm", "Алегорична повість, що висміює радянську ідеологію.", 1945),
            ("Пам'яті Каталонії", "homage-to-catalonia", "Документальна розповідь про громадянську війну в Іспанії.", 1938),
            ("У злиднях Парижа і Лондона", "down-and-out", "Автобіографічна розповідь про життя бідняків.", 1933),
            
            ("Гобіт", "the-hobbit", "Подорож Більбо Беггінса до Самотньої гори.", 1937),
            ("Хранителі персня", "fellowship-of-the-ring", "Перша частина епопеї 'Володар перснів'.", 1954),
            ("Дві вежі", "the-two-towers", "Друга частина епопеї 'Володар перснів'.", 1954),
            ("Повернення короля", "return-of-the-king", "Завершальна частина епопеї.", 1955),
            
            ("Старий і море", "the-old-man-and-the-sea", "Повість про боротьбу старого рибалки з великою рибою.", 1952),
            ("Прощавай, зброє!", "a-farewell-to-arms", "Історія кохання на тлі Першої світової війни.", 1929),
            ("По кому подзвін", "for-whom-the-bell-tolls", "Роман про долю американця в іспанській війні.", 1940),
            ("Фієста", "the-sun-also-rises", "Роман про 'втрачене покоління'.", 1926),
            
            ("Сяйво", "the-shining", "Містичний трилер про похмурий готель.", 1977),
            ("Воно", "it-horror", "Протистояння групи дітей стародавньому злу.", 1986),
            ("Мизері", "misery", "Психологічний трилер про письменника та його фанатку.", 1987),
            ("Зелена миля", "the-green-mile", "Драматична історія у в'язниці для смертників.", 1996),
            
            ("Вбивство у Східному експресі", "orient-express", "Одна з найвідоміших справ Еркюля Пуаро.", 1934),
            ("Смерть на Нілі", "death-on-the-nile", "Розслідування вбивства під час круїзу.", 1937),
            ("Десять негренят", "and-then-there-were-none", "Класичний детективний трилер про острів.", 1939),
            ("Вбивство Роджера Акройда", "roger-ackroyd", "Шедевр з несподіваним фіналом.", 1926)
        ]

        for i, (title, slug, desc, year) in enumerate(books_data):
            writer_index = i // 4
            book, created = Book.objects.get_or_create(
                slug=slug,
                defaults={
                    'writer': writers[writer_index],
                    'title': title,
                    'description': desc,
                    'publication_year': year,
                    'top_place': i + 1
                }
            )
            
            if created:
                self.stdout.write(self.style.NOTICE(
                    f"Створено книгу: {book.title} (Топ: {book.top_place})"
                ))

        self.stdout.write(self.style.SUCCESS(
            "\nБазу даних успішно наповнено!"
        ))
