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
    
    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.price == other.price

    def __ne__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.price != other.price

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.price < other.price

    def __le__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.price <= other.price

    def __gt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.price > other.price

    def __ge__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.price >= other.price
    
    def __add__(self, value: float):
        if not isinstance(value, (int, float)):
            return NotImplemented
        new_price = self.price + value
        return Book(
            self.title, self.year,
            self.publisher, self.genre,
            self.author, new_price)
    
    def __sub__(self, value: float):
        if not isinstance(value, (int, float)):
            return NotImplemented
        new_price = max(0.0, self.price - value)
        return Book(
            self.title, self.year,
            self.publisher, self.genre,
            self.author, new_price)

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

# Застосування знижки 10%
book1.apply_discount(10)
print("\nПісля застосування знижки 10%:")
print(book1)
print('-' * 25)

# Введення через консоль
book2 = Book()
book2.input_data()
print(book2)
print('-' * 25, '\n')

# Створення книг для порівняння
book1 = Book("1984", 1949, "Secker & Warburg", "Антиутопія", "Джордж Орвелл", 450.0)
book2 = Book("Який чудесний світ новий!", 1932, "Chatto & Windus", "Антиутопія", "Олдос Гакслі", 380.0)
book3 = Book("451 градус за Фаренгейтом", 1953, "Ballantine Books", "Антиутопія", "Рей Бредбері", 450.0)

# Порівняння цін на книги
print(f"book1 ({book1.price} ₴) <  book2 ({book2.price} ₴): {book1 < book2}")
print(f"book2 ({book2.price} ₴) <  book3 ({book3.price} ₴): {book2 < book3}")
print(f"book1 ({book1.price} ₴) >= book3 ({book3.price} ₴): {book1 >= book3}")
print(f"book1 ({book1.price} ₴) == book3 ({book3.price} ₴): {book1 == book3} \n")
print('-' * 25, '\n')

# Зміна ціни книги
print(f"Початкова ціна книги: {book2.price:,.2f} ₴")
book2 = book2 + 50
print(f"Ціна книги (+50):     {book2.price:,.2f} ₴")
book2 = book2 - 100
print(f"Ціна книги (-100):    {book2.price:,.2f} ₴")
