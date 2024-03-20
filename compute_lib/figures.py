from abc import ABC, abstractmethod


class Figure(ABC):
    """
    Abstract class for defining figures
    """

    @abstractmethod
    def compute_area(self) -> int:
        pass

    @abstractmethod
    def check_is_rectangular(self):
        pass

    @abstractmethod
    def who_am_i(self):
        pass


class Triangle(Figure):
    def __init__(self, a: int, b: int, c: int):
        self.__area = 0.0
        self.__a = a
        self.__b = b
        self.__c = c
        self.__sides_num = 3

    def compute_area(self) -> int:
        """
        Compute the area
        :return: the area of the triangle
        """
        s = (self.__a + self.__b + self.__c) / 2
        self.__area = (s * (s - self.__a) * (s - self.__b) * (s - self.__c)) ** 0.5
        return self.__area

    def who_am_i(self):
        return "I'm Triangle"

    def check_is_rectangular(self) -> bool:
        # return self.__a**2 + self.__b**2 == self.__c**2 or
        lv_list = [self.__a, self.__b, self.__c]
        a, b, c = sorted(lv_list)

        return a ** 2 + b ** 2 == c ** 2


class Rectangle(Figure):
    """
    Rectangle is defined by two points

    """

    def __init__(self, a: int, b: int):
        self.__a = a
        self.__b = b
        self.__area = 0.0
        self.__sides_num = 4

    def who_am_i(self):
        return "I'm Rectangle"

    def compute_area(self) -> int:
        """
        Compute the area of the rectangle
        :return: the area of the rectangle
        """
        self.__area = (self.__b + self.__a) * 2
        return self.__area

    def check_is_rectangular(self):
        pass


def test_null_sides_tr():
    triangle_1 = Triangle(0, 0, 0)
    assert triangle_1.compute_area() == 0
    assert triangle_1.check_is_rectangular() == True


def test_null_sides_rect():
    rectangle_1 = Rectangle(0, 0)
    assert rectangle_1.compute_area() == 0
