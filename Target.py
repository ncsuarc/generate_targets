from enum import Enum, unique

@unique
class Shape(Enum):
    circle = 0
    semicircle = 1
    quarter_circle = 2
    triangle = 3
    square = 4
    rectangle = 5
    trapezoid = 6
    pentagon = 7
    hexagon = 8
    heptagon = 9
    octogon = 10
    star = 11
    cross = 12

@unique
class Color(Enum):
    red = 0
    orange = 1
    yellow = 2
    green = 3
    blue = 4
    purple = 5
    brown = 6
    black = 7
    gray = 8
    white = 9


