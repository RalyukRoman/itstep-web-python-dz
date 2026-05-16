import datetime

class Stadium():
    def __init__(
            self, 
            name: str = "", 
            date: datetime.date = None, 
            country: str = "", 
            city: str = "", 
            capacity: int = 0):
        
        self.name = name
        self.country = country
        self.city = city
        self.capacity = capacity

        if date is None:
            self.date = datetime.date.today()
        else:
            self.date = date

    def __str__(self):
        return (
            f"\n-- Інформація про стадіон --\n"
            f"Назва: {self.name};\n"
            f"Дата відкриття: {self.date};\n"
            f"Країна: {self.country};\n"
            f"Місто: {self.city};\n"
            f"Місткість: {self.capacity};\n"
        )
    
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, datetime.date):
            raise TypeError("Дата має бути об'єктом datetime.date")
        if value.year < 566:
            raise ValueError(f"Рік відкриття має бути від 566!")
        if value > datetime.date.today():
            raise ValueError(f"Дата відкриття має бути раніше за сьогодні!")
        self._date = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Місткість не може бути від'ємною!")
        self._capacity = value

    def input_data(self):
        print("\n-- Введіть дані про стадіон --")
        self.name = input("Введіть назву: ").strip()
        self.country = input("Введіть країну: ").strip()
        self.city = input("Введіть місто: ").strip()

        while True:
            try:
                date_str = input("Введіть дату відкриття (ДД.ММ.РРРР): ").strip()
                raw_date = datetime.datetime.strptime(date_str, "%d.%m.%Y")
                self.date = raw_date.date()
                break
            except (ValueError, TypeError) as error:
                print(f"Помилка: {error} Спробуйте ще раз.")

        while True:
            try:
                self.capacity = int(
                    input("Введіть місткість: "))
                break
            except (ValueError, TypeError) as error:
                print(f"Помилка: {error} Спробуйте ще раз.")
        
        print("-- Дані про стадіон введено успішно --")

    def get_age(self) -> int:
        current_year = datetime.date.today().year
        return current_year - self.date.year


# Створення об'єкта з початковими даними
stadium1 = Stadium(
    "НСК Олімпійський", 
    datetime.date(1923, 8, 12), 
    "Україна", "Київ", 70050)
print(stadium1)
print(f"Вік стадіону: {stadium1.get_age()} р. \n")
print('-' * 25)

# Створення порожнього об'єкта та введення через консоль
stadium2 = Stadium()
stadium2.input_data()
print(stadium2)
print('-' * 25)