class NonNegative:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"Помилка! Значення для {self.name.strip('_')} не може бути від'ємним!")
        setattr(instance, self.name, value)