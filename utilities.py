import math
import random


def pythTheorem(x1, y1, x2, y2):
    return abs(math.hypot(x1-x2, y1-y2))

def perimeter(rad):
    return math.pi*rad*2

def randomColor():
    r, g, b = random.randrange(0, 255), random.randrange(
        0, 255), random.randrange(0, 255)
    return r, g, b
