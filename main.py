from random import randrange
import pygame as py
import sys
from jarvis import *
from utilities import *
from pygame.locals import *


# pygame initialization
py.init()

#  constants
disp_tup = (1080, 720)
SCREEN = py.display.set_mode(disp_tup)
SCREEN_COLOR = (36, 36, 36)
FPS = py.time.Clock()


# variables
running = True

# shapes
circle_list = []
# for i in range(30):
#     rad = random.randrange(5, 20)
#     x = random.randrange(rad, SCREEN.get_width()-rad)
#     y = random.randrange(rad, SCREEN.get_height()-rad)
#     color = randomColor()
#     dx, dy = 2, 2
#     stroke = 2
#     i = Circles(x, y, dx, dy, SCREEN, color, rad, stroke)
#     circle_list.append(i)
p_rad = 120
for i in range(20):
    rad = random.randrange(5, 20)
    x = random.randrange(rad, SCREEN.get_width()-rad)
    y = random.randrange(rad, SCREEN.get_height()-rad)
    color = randomColor()
    dx, dy = 2, 2
    stroke = 3
    i = Circles(x, y, dx, dy, SCREEN, color, rad, stroke, p_rad)
    circle_list.append(i)


if __name__ == '__main__':
    while running:
        FPS.tick(30)
        SCREEN.fill(SCREEN_COLOR)
        for event in py.event.get():
            if event.type == QUIT:
                running = False

        # circle movement
        # for i in circle_list:
        #     i.drawCircle()
        #     i.rotateCircle(150,10)
        #     # for a, b in itertools.combinations(circle_list, 2):
        #     #     pyth = pythTheorem(a.x, a.y, b.x, b.y)
        #     #     rads = a.rad+b.rad
        #     #     if pyth <= rads:
        #     #         a.color = randomColor()
        #     #         b.color = randomColor()

        #  circle_rotation
        for i in circle_list:
            i.drawCircle()
            i.moveCircle()
        py.display.update()
py.quit()
sys.exit()
