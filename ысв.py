import abc


class Shape(abc.ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abc.abstractmethod
    def area(self): pass  # абстрактны метод

    def print_point(self):  # неабстрактный метод
        print("X:", self.x, "\tY:", self.y)


# класс прямоугольника
class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def area(self): return self.width * self.height


rect = Rectangle(10, 20, 100, 100)
rect.print_point()  # X: 10   Y: 20