import datetime

class Book():
    def __init__(
            self, 
            title: str = "", 
            year: int = 2000, 
            publisher: str = "", 
            genre: str = "", 
            author: str = "", 
            price: float = 0.0):
        
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def __str__(self):
        return (
            f"\n-- Інформація про книгу --\n"
            f"Назва: {self.title};\n"
            f"Рік видання: {self.year} р.;\n"
            f"Видавець: {self.publisher};\n"
            f"Жанр: {self.genre};\n"
            f"Автор: {self.author};\n"
            f"Ціна: {self.price:,.2f} ₴;\n"
        )
    
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        current_year = datetime.date.today().year
        if value < 1452 or value > current_year:
            raise ValueError(f"Рік видання має бути від 1452 до {current_year}!")
        self._year = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Ціна не може бути від'ємною!")
        self._price = value

    def input_data(self):
        print("\n-- Введіть дані про книгу --")
        self.title = input("Введіть назву: ").strip()
        self.publisher = input("Введіть видавця: ").strip()
        self.genre = input("Введіть жанр: ").strip()
        self.author = input("Введіть автора: ").strip()

        while True:
            try:
                self.year = int(
                    input("Введіть рік видання: "))
                break
            except (ValueError, TypeError) as error:
                print(f"Помилка: {error} Спробуйте ще раз.")

        while True:
            try:
                self.price = float(
                    input("Введіть ціну (в гривнях): "))
                break
            except (ValueError, TypeError) as error:
                print(f"Помилка: {error} Спробуйте ще раз.")
        
        print("-- Дані про книгу введено успішно --")

    def get_age(self) -> int:
        current_year = datetime.date.today().year
        return current_year - self.year
    
    def apply_discount(self, percentage: float):
        if 0 <= percentage <= 100:
            self.price -= self.price * (percentage / 100)
        else:
            raise ValueError("Відсоток має бути від 0 до 100")


# Створення об'єкта з початковими даними
book1 = Book(
    "Кобзар", 1840, "В друкарні Є. Фішера", 
    "Поезія", "Тарас Шевченко", 1200.0)
print(book1)
print(f"Вік книги: {book1.get_age()} р. \n")
print('-' * 25)

# Застосуємо знижку 10%
book1.apply_discount(10)
print("\nПісля застосування знижки 10%:")
print(book1)
print('-' * 25)

# Створення порожнього об'єкта та введення через консоль
book2 = Book()
book2.input_data()
print(book2)
print('-' * 25)