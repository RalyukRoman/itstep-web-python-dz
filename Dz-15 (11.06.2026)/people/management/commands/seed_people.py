from django.core.management.base import BaseCommand
from people.models import Person

class Command(BaseCommand):
    help = "Заповнює базу даних інформацією про людей"

    def handle(self, *args, **options):
        people_data = [
            {"full_name": "Олександр Шевченко", "city": "Київ", "email": "o.shevchenko@example.com", "birthday": "1990-05-12"},
            {"full_name": "Андрій Шевченко", "city": "Київ", "email": "a.shevchenko@example.com", "birthday": "1985-09-29"},
            {"full_name": "Марія Мельник", "city": "Львів", "email": "m.melnyk@example.com", "birthday": "1992-03-15"},
            {"full_name": "Олена Мельник", "city": "Львів", "email": "e.melnyk@example.com", "birthday": "1994-11-22"},
            {"full_name": "Дмитро Ковальчук", "city": "Одеса", "email": "d.kovalchuk@example.com", "birthday": "1988-07-04"},
            {"full_name": "Олексій Ковальчук", "city": "Одеса", "email": "al.kovalchuk@example.com", "birthday": "1991-01-30"},
            {"full_name": "Тетяна Бондаренко", "city": "Харків", "email": "t.bondarenko@example.com", "birthday": "1993-05-18"},
            {"full_name": "Сергій Бондаренко", "city": "Харків", "email": "s.bondarenko@example.com", "birthday": "1987-12-12"},
            {"full_name": "Микола Ткаченко", "city": "Дніпро", "email": "m.tkachenko@example.com", "birthday": "1982-06-25"},
            {"full_name": "Ольга Ткаченко", "city": "Дніпро", "email": "ol.tkachenko@example.com", "birthday": "1989-08-08"},
            {"full_name": "Петро Кравченко", "city": "Вінниця", "email": "p.kravchenko@example.com", "birthday": "1980-02-14"},
            {"full_name": "Ганна Кравченко", "city": "Вінниця", "email": "g.kravchenko@example.com", "birthday": "1995-10-10"},
            {"full_name": "Василь Олійник", "city": "Запоріжжя", "email": "v.oliynyk@example.com", "birthday": "1984-04-03"},
            {"full_name": "Світлана Олійник", "city": "Запоріжжя", "email": "s.oliynyk@example.com", "birthday": "1991-07-21"},
            {"full_name": "Роман Шевчук", "city": "Полтава", "email": "r.shevchuk@example.com", "birthday": "1986-09-14"},
            {"full_name": "Юлія Шевчук", "city": "Полтава", "email": "y.shevchuk@example.com", "birthday": "1990-12-05"},
            {"full_name": "Віталій Поліщук", "city": "Київ", "email": "v.polishchuk@example.com", "birthday": "1983-01-20"},
            {"full_name": "Наталія Поліщук", "city": "Київ", "email": "n.polishchuk@example.com", "birthday": "1988-05-25"},
            {"full_name": "Артем Лисенко", "city": "Львів", "email": "a.lysenko@example.com", "birthday": "1996-08-14"},
            {"full_name": "Оксана Лисенко", "city": "Львів", "email": "o.lysenko@example.com", "birthday": "1992-02-28"},
            {"full_name": "Ігор Романюк", "city": "Одеса", "email": "i.romanyuk@example.com", "birthday": "1981-11-11"},
            {"full_name": "Юрій Романюк", "city": "Одеса", "email": "y.romanyuk@example.com", "birthday": "1985-04-19"},
            {"full_name": "Вадим Мазур", "city": "Харків", "email": "v.mazur@example.com", "birthday": "1994-06-07"},
            {"full_name": "Інна Мазур", "city": "Харків", "email": "i.mazur@example.com", "birthday": "1990-09-22"},
            {"full_name": "Тарас Кравчук", "city": "Дніпро", "email": "t.kravchuk@example.com", "birthday": "1987-03-31"},
            {"full_name": "Павло Кравчук", "city": "Дніпро", "email": "p.kravchuk@example.com", "birthday": "1989-10-14"},
            {"full_name": "Максим Павленко", "city": "Вінниця", "email": "m.pavlenko@example.com", "birthday": "1993-02-02"},
            {"full_name": "Людмила Павленко", "city": "Вінниця", "email": "l.pavlenko@example.com", "birthday": "1991-06-16"},
            {"full_name": "Богдан Савченко", "city": "Запоріжжя", "email": "b.savchenko@example.com", "birthday": "1988-08-19"},
            {"full_name": "Євген Савченко", "city": "Запоріжжя", "email": "e.savchenko@example.com", "birthday": "1984-12-03"},
            {"full_name": "Назар Козак", "city": "Полтава", "email": "n.kozak@example.com", "birthday": "1995-05-05"},
            {"full_name": "Михайло Козак", "city": "Полтава", "email": "m.kozak@example.com", "birthday": "1992-07-27"},
            {"full_name": "Денис Мороз", "city": "Київ", "email": "d.moroz@example.com", "birthday": "1980-09-09"},
            {"full_name": "Вікторія Мороз", "city": "Київ", "email": "v.moroz@example.com", "birthday": "1986-04-11"},
            {"full_name": "Антон Кузьменко", "city": "Львів", "email": "a.kuzmenko@example.com", "birthday": "1990-10-31"},
            {"full_name": "Іванна Кузьменко", "city": "Львів", "email": "i.kuzmenko@example.com", "birthday": "1994-12-15"},
            {"full_name": "Валентин Пономаренко", "city": "Одеса", "email": "v.ponomarenko@example.com", "birthday": "1982-01-25"},
            {"full_name": "Яна Пономаренко", "city": "Одеса", "email": "y.ponomarenko@example.com", "birthday": "1987-08-30"},
            {"full_name": "Олег Харченко", "city": "Харків", "email": "o.kharchenko@example.com", "birthday": "1991-03-12"},
            {"full_name": "Дарина Харченко", "city": "Харків", "email": "d.kharchenko@example.com", "birthday": "1993-09-04"},
            {"full_name": "Гліб Василенко", "city": "Дніпро", "email": "g.vasylenko@example.com", "birthday": "1989-05-20"},
            {"full_name": "Христина Василенко", "city": "Дніпро", "email": "kh.vasylenko@example.com", "birthday": "1995-11-01"},
            {"full_name": "Леонід Коваль", "city": "Вінниця", "email": "l.koval@example.com", "birthday": "1983-06-18"},
            {"full_name": "Софія Коваль", "city": "Вінниця", "email": "s.koval@example.com", "birthday": "1988-10-22"},
            {"full_name": "Ростислав Дмитренко", "city": "Запоріжжя", "email": "r.dmytrenko@example.com", "birthday": "1985-02-10"},
            {"full_name": "Аліна Дмитренко", "city": "Запоріжжя", "email": "a.dmytrenko@example.com", "birthday": "1992-04-28"},
            {"full_name": "Станіслав Білоус", "city": "Полтава", "email": "s.bilous@example.com", "birthday": "1987-07-15"},
            {"full_name": "Олеся Білоус", "city": "Полтава", "email": "o.bilous@example.com", "birthday": "1994-01-05"},
            {"full_name": "Кирило Мельник", "city": "Київ", "email": "k.melnyk@example.com", "birthday": "1991-09-19"},
            {"full_name": "Єлизавета Мельник", "city": "Київ", "email": "y.melnyk@example.com", "birthday": "1993-03-24"},
            {"full_name": "Андрій Ковальчук", "city": "Львів", "email": "an.kovalchuk@example.com", "birthday": "1986-11-30"},
            {"full_name": "Лариса Ковальчук", "city": "Львів", "email": "l.kovalchuk@example.com", "birthday": "1984-05-09"},
            {"full_name": "Марк Бондар", "city": "Одеса", "email": "m.bondar@example.com", "birthday": "1996-02-17"},
            {"full_name": "Олександр Коваленко", "city": "Київ", "email": "o.kovalenko@example.com", "birthday": "1988-06-21"},
            {"full_name": "Олена Коваленко", "city": "Київ", "email": "e.kovalenko@example.com", "birthday": "1990-12-11"}
        ]

        for data in people_data:
            person, created = Person.objects.update_or_create(
                email=data["email"],
                defaults=data
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f"Додано людину: {person.full_name}"
                ))
            else:
                self.stdout.write(self.style.WARNING(
                    f"Оновлено людину: {person.full_name}"
                ))