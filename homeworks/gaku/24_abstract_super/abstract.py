from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._height + self._width)


class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return 3.14 * self._radius**2

    def perimeter(self):
        return 2 * 3.14 * self._radius

