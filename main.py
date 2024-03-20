# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from compute_lib import figures as figs
import pytest


class Square(figs.Figure):
    def who_am_i(self):
        return "I am a square"

    def __init__(self, x: int):
        self.__x = x
        self.__area = 0.0
        self.__sides_num = 4

    def compute_area(self) -> int:
        self.__area = (self.__x * self.__x)
        return self.__area

    def check_is_rectangle(self):
        if self.__sides_num != 3:
            return False
        else:
            return True


if __name__ == '__main__':

    new_objects = [figs.Triangle(5, 3, 4), figs.Triangle(4, 5, 6), figs.Rectangle(4, 4)]
    for obj in new_objects:
        print(obj.compute_area(), obj.who_am_i(), obj.check_is_rectangular())
