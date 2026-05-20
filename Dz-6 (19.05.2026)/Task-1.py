class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Circle (radius {self.radius})"
        
    # Operation ==
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False

    # Operations >, <, <=, >=
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.radius <= other.radius
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.radius >= other.radius
        return NotImplemented

    # Operations +, -, +=, -=
    def __add__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius + value)
        return NotImplemented

    def __sub__(self, value):
        if isinstance(value, (int, float)):
            if (self.radius <= value):
                raise ValueError(
                    "The radius cannot be less than or equal to zero!")
            return Circle(self.radius - value)
        return NotImplemented

    def __iadd__(self, value):
        if isinstance(value, (int, float)):
            self.radius += value
            return self
        return NotImplemented

    def __isub__(self, value):
        if isinstance(value, (int, float)):
            if (self.radius <= value):
                raise ValueError(
                    "The radius cannot be less than or equal to zero!")
            self.radius -= value
            return self
        return NotImplemented

# Example of use
c1 = Circle(radius=20)
c2 = Circle(radius=15)
c3 = Circle(radius=14)

print()

print(f"c1: {c1}")
print(f"c2: {c2}")
print(f"c3: {c3}", '\n')

print(f"c1 == c2: {c1 == c2}")
print(f"c1 == c3: {c1 == c3}", '\n')

print(f"c1 < c2:  {c1 < c2}")
print(f"c1 > c3:  {c1 > c3}")
print(f"c2 <= c3: {c2 <= c3}")
print(f"c1 >= c2: {c1 >= c2}", '\n')

c4 = c1 + 5
print(f"c4 = c1 + 5:  {c4}")
c4 = c1 - 15
print(f"c4 = c1 - 15: {c4}", '\n')

c5 = Circle(radius=18)
print(f"c5: {c5}", '\n')

c5 += 10
print(f"с5 += 10: {c5}")
c5 -= 25
print(f"с5 -= 25: {c5}")