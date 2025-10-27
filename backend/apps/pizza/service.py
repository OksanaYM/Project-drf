import math
from math import cos


def calc (a,b,operator):
    if operator == '+':
        # return a + b
        # return cos(a)
        # return b + cos(a)
        return b + math.cos(a)
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b

