class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __str__(self):
        return (
            f"\n--Flat--\n"
            f"Area: {self.area}\n"
            f"Price: {self.price}$"
        )
        
    # Operation ==, !=
    def __eq__(self, other):
        if isinstance(other, Flat):
            return self.area == other.area
        return False
    
    def __ne__(self, other):
        return not self.__eq__(other)

    # Operations >, <, <=, >=
    def __lt__(self, other):
        if isinstance(other, Flat):
            return self.price < other.price
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Flat):
            return self.price <= other.price
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Flat):
            return self.price > other.price
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Flat):
            return self.price >= other.price
        return NotImplemented
    
# Example of use
f1 = Flat(area=60, price=50000) 
f2 = Flat(area=60, price=55000)
f3 = Flat(area=45, price=40000)

print()

print(f"f1: {f1}", '\n')
print(f"f2: {f2}", '\n')
print(f"f3: {f3}", '\n')

print(f"f1 == f2: {f1 == f2}")
print(f"f1 == f3: {f1 == f3}", '\n')

print(f"f1 != f3: {f1 != f3}")
print(f"f1 != f2: {f1 != f2}", '\n')

print(f"f1 < f2:  {f1 < f2}") 
print(f"f1 > f3:  {f1 > f3}")
print(f"f2 <= f1: {f2 <= f1}")
print(f"f1 >= f1: {f1 >= f1}")