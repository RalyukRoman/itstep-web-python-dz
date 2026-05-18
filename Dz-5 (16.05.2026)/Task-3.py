from NonNegative import NonNegative
import datetime

class Stadium():
    capacity = NonNegative('_capacity')

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
    
    def __eq__(self, other):
        if not isinstance(other, Stadium):
            return NotImplemented
        return self.capacity == other.capacity

    def __ne__(self, other):
        if not isinstance(other, Stadium):
            return NotImplemented
        return self.capacity != other.capacity

    def __lt__(self, other):
        if not isinstance(other, Stadium):
            return NotImplemented
        return self.capacity < other.capacity

    def __le__(self, other):
        if not isinstance(other, Stadium):
            return NotImplemented
        return self.capacity <= other.capacity

    def __gt__(self, other):
        if not isinstance(other, Stadium):
            return NotImplemented
        return self.capacity > other.capacity

    def __ge__(self, other):
        if not isinstance(other, Stadium):
            return NotImplemented
        return self.capacity >= other.capacity
    
    def __add__(self, value: int):
        if not isinstance(value, (int, float)):
            return NotImplemented
        new_capacity = int(self.capacity + value)
        return Stadium(
            self.name, self.date,
            self.country, self.city,
            new_capacity)

    def __sub__(self, value: int):
        if not isinstance(value, (int, float)):
            return NotImplemented
        new_capacity = max(0, int(self.capacity - value))
        return Stadium(
            self.name, self.date,
            self.country, self.city,
            new_capacity)
    
    def __call__(self, visitors_count: int) -> bool:
        return visitors_count <= self.capacity
    
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

# Введення через консоль
stadium2 = Stadium()
stadium2.input_data()
print(stadium2)
print('-' * 25, '\n')

# Створення стадіонів для порівняння
stadium1 = Stadium("Стадіон А", datetime.date(2000, 5, 10), "Україна", "Київ", 50000)
stadium2 = Stadium("Стадіон Б", datetime.date(2005, 6, 15), "Польща", "Варшава", 40000)
stadium3 = Stadium("Стадіон В", datetime.date(2010, 7, 20), "Німеччина", "Берлін", 50000)

# Порівняння місткості стадіонів
print(f"stadium1 ({stadium1.capacity}) <  stadium2 ({stadium2.capacity}): {stadium1 < stadium2}")
print(f"stadium2 ({stadium2.capacity}) <  stadium3 ({stadium3.capacity}): {stadium2 < stadium3}")
print(f"stadium1 ({stadium1.capacity}) >= stadium3 ({stadium3.capacity}): {stadium1 >= stadium3}")
print(f"stadium1 ({stadium1.capacity}) == stadium3 ({stadium3.capacity}): {stadium1 == stadium3} \n")
print('-' * 25, '\n')

# Зміна місткості стадіону
print(f"Початкова місткість стадіону: {stadium2.capacity}")
stadium2 = stadium2 + 5000
print(f"Місткість стадіону (+5000):   {stadium2.capacity}")
stadium2 = stadium2 - 10000
print(f"Місткість стадіону (-10000):  {stadium2.capacity} \n")

print(f"Чи вмістить стадіон 80,000 глядачів: {stadium2(80000)}")
