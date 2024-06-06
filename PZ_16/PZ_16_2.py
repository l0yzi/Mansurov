# Создание базового класса "Фигура" и его наследование для создания классов "Квадрат", "Прямоугольник", "Круг".
# Класс "Фигура" будет иметь общие методы, такие как вычисление площади и периметра,
# а классы-наследники будут иметь спецефичные свойства и методы.
import math
class Figure:
    def __init__(self):
        self.area = 0
        self.perimeter = 0

    # Общие методы для всех фигур
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Square(Figure):
    def __init__(self, side):
        super().__init__()
        self.side = side
    # Специфические методы для квадрата
    def calculate_area(self):
        self.area = self.side ** 2
    def calculate_perimeter(self):
        self.perimeter = 4 * self.side

class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    # Специфические методы для прямоугольника
    def calculate_area(self):
        self.area = self.length * self.width
    def calculate_perimeter(self):
        self.perimeter = 2 * (self.length + self.width)


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    # Специфические методы для круга
    def calculate_area(self):
        self.area = math.pi * self.radius ** 2
    def calculate_perimeter(self):
        self.perimeter = 2 * math.pi * self.radius

square = Square(5)
square.calculate_area()
square.calculate_perimeter()
print("Площадь квадрата:", square.area)
print("Периметр квадрата:", square.perimeter)

rectangle = Rectangle(10, 5)
rectangle.calculate_area()
rectangle.calculate_perimeter()
print("Площадь прямоугольника:", rectangle.area)
print("Периметр прямоугольника:", rectangle.perimeter)

circle = Circle(3)
circle.calculate_area()
circle.calculate_perimeter()
print("Площадь круга:", circle.area)
print("Периметр круга:", circle.perimeter)