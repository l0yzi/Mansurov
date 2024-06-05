# Создание базового класса "Транспортное средство" и его наследование для создания классов "Автомобиль" и "Мотоцикл".
# В классе "Транспортное средство" будут общие свойства, такие как максимальная скорость и количество колес,
# а классы-наследники будут иметь свои уникальные свойства и методы.

class Vfigure:
    def __init__(self, max_speed, num_wheels):
        self.max_speed = max_speed
        self.num_wheels = num_wheels

class Car(Vehicle):
    def __init__(self, max_speed, num_wheels, num_passengers):
        super().__init__(max_speed, num_wheels)
        self.num_passengers = num_passengers

class Motorcycle(Vehicle):
    def __init__(self, max_speed, num_wheels, engine_type):
        super().__init__(max_speed, num_wheels)
        self.engine_type = engine_type

car = Car(200, 4, 5)
motorcycle = Motorcycle(120, 2, "бензиновый")

print("Максимальная скорость автомобиля:", car.max_speed)
print("Количество колес мотоцикла:", motorcycle.num_wheels)
print("Тип двигателя мотоцикла:", motorcycle.engine_type)
