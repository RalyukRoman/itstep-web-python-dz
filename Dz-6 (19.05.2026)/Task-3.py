class Airplane:
    def __init__(self, type, passengers, max_passengers):
        self.type = type
        self.passengers = passengers
        self.max_passengers = max_passengers

    def __str__(self):
        return (
            f"\n--Airplane--\n"
            f"Type: {self.type}\n"
            f"Passengers: {self.passengers}\n"
            f"Max passengers: {self.max_passengers}"
        )

    # Operation ==
    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.type.lower() == other.type.lower()
        return False
    
    # Operations +, -, +=, -=
    def __add__(self, value):
        if isinstance(value, (int, float)):
            return Airplane(
                self.type,
                self.passengers + value,
                self.max_passengers)
        return NotImplemented

    def __sub__(self, value):
        if isinstance(value, (int, float)):
            if (self.passengers < value):
                raise ValueError(
                    "The number of passengers cannot be less than zero!")
            return Airplane(
                self.type,
                self.passengers - value,
                self.max_passengers)
        return NotImplemented

    def __iadd__(self, value):
        if isinstance(value, (int, float)):
            self.passengers += value
            return self
        return NotImplemented

    def __isub__(self, value):
        if isinstance(value, (int, float)):
            if (self.passengers <= value):
                raise ValueError(
                    "The number of passengers cannot be less than zero!")
            self.passengers -= value
            return self
        return NotImplemented

    # Operations >, <, <=, >=
    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers < other.max_passengers
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers <= other.max_passengers
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers > other.max_passengers
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers >= other.max_passengers
        return NotImplemented
    
# Example of use
air1 = Airplane("Boeing 737", 120, 180)
air2 = Airplane("Boeing 737", 150, 180)
air3 = Airplane("Airbus A320", 100, 150)

print()

print(f"air1: {air1}", '\n')
print(f"air2: {air2}", '\n')
print(f"air3: {air3}", '\n')

print(f"air1 == air2: {air1 == air2}")
print(f"air1 == air3: {air1 == air3}", '\n')

print(f"air1 < air3:  {air1 < air3}")
print(f"air1 > air3:  {air1 > air3}")
print(f"air1 <= air2: {air1 <= air2}", '\n')

air4 = air1 + 30
print(f"air4 = air1 + 30: {air4}", '\n')
air4 = air1 - 50
print(f"air4 = air1 - 50: {air4}", '\n')

air5 = Airplane("Embraer 190", 50, 100)
print(f"air5: {air5}", '\n')

air5 += 20
print(f"air5 += 20: {air5}", '\n')
air5 -= 40
print(f"air5 -= 40: {air5}")