class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        sign = "+" if self.imag >= 0 else "-"
        return f"{self.real:.2f} {sign} {abs(self.imag):.2f}i"

    # (a + bi) + (c + di) = (a + c) + (b + d)i
    def __add__(self, other):
        if isinstance(other, Complex):
            real = self.real + other.real
            imag = self.imag + other.imag
            return Complex(real, imag)
        return NotImplemented

    # (a + bi) + (c + di) = (a - c) + (b - d)i
    def __sub__(self, other):
        if isinstance(other, Complex):
            real = self.real - other.real
            imag = self.imag - other.imag
            return Complex(real, imag)
        return NotImplemented

    # (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
    def __mul__(self, other):
        if isinstance(other, Complex):       
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
            return Complex(real, imag)
        return NotImplemented

    # (a + bi) / (c + di) = ((ac + bd) / (c^2 + d^2)) + ((bc - ad) / (c^2 + d^2))i
    def __truediv__(self, other):
        if isinstance(other, Complex):
            denominator = other.real**2 + other.imag**2
            if denominator == 0:
                raise ZeroDivisionError(
                    "Division by zero in complex numbers")
            real = (self.real * other.real + self.imag * other.imag) / denominator
            imag = (self.imag * other.real - self.real * other.imag) / denominator
            return Complex(real, imag)
        return NotImplemented

# Example of use
c1 = Complex(real=3, imag=2)
c2 = Complex(real=1, imag=4)

print()

print(f"c1: {c1}")
print(f"c2: {c2}", '\n')

print(f"Add  (c1 + c2): {c1 + c2}")
print(f"Sub  (c1 - c2): {c1 - c2}")
print(f"Mult (c1 * c2): {c1 * c2}")
print(f"Div  (c1 / c2): {c1 / c2}")