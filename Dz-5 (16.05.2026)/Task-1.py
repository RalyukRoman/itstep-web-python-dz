import datetime

class Car():
    def __init__(
            self,
            model: str = "", 
            year: int = 2000, 
            maker: str = "", 
            capacity: float = 0.0, 
            color: str = "", 
            price: float = 0.0):
        
        self.model = model
        self.year = year
        self.maker = maker
        self.capacity = capacity
        self.color = color
        self.price = price

    def __str__(self):
        return (
            f"\n-- Інформація про машину --\n"
            f"Назва моделі: {self.model};\n"
            f"Рік випуску: {self.year} р.;\n"
            f"Виробник: {self.maker};\n"
            f"Об'єм двигуна: {self.capacity} л;\n"
            f"Колір машини: {self.color};\n"
            f"Ціна: {self.price:,.2f} ₴;\n"
        )
    
    def __eq__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self.price == other.price

    def __ne__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self.price != other.price

    def __lt__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self.price < other.price

    def __le__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self.price <= other.price

    def __gt__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self.price > other.price

    def __ge__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self.price >= other.price
    
    def __add__(self, value: float):
        if not isinstance(value, (int, float)):
            return NotImplemented
        new_price = self.price + value
        return Car(
            self.model, self.year, 
            self.maker, self.capacity, 
            self.color, new_price)
    
    def __sub__(self, value: float):
        if not isinstance(value, (int, float)):
            return NotImplemented
        new_price = max(0.0, self.price - value)
        return Car(
            self.model, self.year, 
            self.maker, self.capacity, 
            self.color, new_price)

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        current_year = datetime.date.today().year
        if value < 1886 or value > current_year:
            raise ValueError(f"Рік випуску має бути від 1886 до {current_year}!")
        self._year = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Об'єм двигуна не може бути від'ємним!")
        self._capacity = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Ціна не може бути від'ємною!")
        self._price = value

    def input_data(self):
        print("\n-- Введіть дані про машину --")
        self.model = input("Введіть назву моделі: ").strip()
        self.maker = input("Введіть виробника: ").strip()
        self.color = input("Введіть колір машини: ").strip()

        while True:
            try:
                self.year = int(
                    input("Введіть рік випуску: "))
                break
            except ValueError as error:
                print(f"Помилка: {error} Спробуйте ще раз.")

        while True:
            try:
                self.capacity = float(
                    input("Введіть об'єм двигуна (в літрах): "))
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
        
        print("-- Дані про машину введено успішно --")

    def get_age(self) -> int:
        current_year = datetime.date.today().year
        return current_year - self.year
    
    def apply_discount(self, percentage: float):
        if 0 <= percentage <= 100:
            self.price -= self.price * (percentage / 100)
        else:
            raise ValueError("Відсоток має бути від 0 до 100")


# Створення об'єкта з початковими даними
car1 = Car(
    "Model S", 2022, "Tesla", 
    12.4, "Червоний", 1850000)
print(car1)
print(f"Вік машини: {car1.get_age()} р. \n")
print('-' * 25)

# Застосування знижки 10%
car1.apply_discount(10)
print("\nПісля застосування знижки 10%:")
print(car1)
print('-' * 25)

# Введення через консоль
car2 = Car()
car2.input_data()
print(car2)
print('-' * 25, '\n')

# Створення авто для порівняння
car1 = Car("Model S", 2022, "Tesla", 0.0, "Червоний", 1850000)
car2 = Car("Leaf", 2020, "Nissan", 0.0, "Білий", 750000)
car3 = Car("Model S", 2023, "Tesla", 0.0, "Чорний", 2100000)

# Порівняння цін на авто
print(f"car1 ({car1.price} ₴) <  car2 ({car2.price} ₴):  {car1 < car2}")
print(f"car2 ({car2.price} ₴) <  car3 ({car3.price} ₴): {car2 < car3}")
print(f"car1 ({car1.price} ₴) >= car3 ({car3.price} ₴): {car1 >= car3}")
print(f"car1 ({car1.price} ₴) == car3 ({car2.price} ₴):  {car1 == car3} \n") 
print('-' * 25, '\n')

# Зміна ціни авто
print(f"Початкова ціна машини:  {car2.price:,.2f} ₴")
car2 = car2 + 50000
print(f"Ціна машини (+50 000):  {car2.price:,.2f} ₴")
car2 = car2 - 100000
print(f"Ціна машини (-100 000): {car2.price:,.2f} ₴")