import pygame as py
from utilities import *
import math


class Shapes:
    def __init__(self, x, y, dx, dy, screen, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.screen = screen
        self.color = color


class Circles(Shapes):
    c_diff = 5
    r_diff = 2

    def __init__(self, x, y, dx, dy, screen, color, rad, stroke, p_rad):
        Shapes.__init__(self, x, y, dx, dy, screen, color)
        self.diff = 5
        self.rad = rad
        self.rad += Circles.r_diff*1.5
        self.stroke = stroke
        self.vel = 10
        self.p_rad = p_rad
        self.omega = self.vel/self.p_rad
        self.omega += Circles.c_diff*5
        self.rads = math.radians(self.omega)
        Circles.c_diff += 5
        Circles.r_diff += 1

    def drawCircle(self):
        py.draw.circle(self.screen, self.color,
                       (self.x, self.y), self.rad, self.stroke)

    def moveCircle(self):
        x_vel = self.dx
        y_vel = self.dy
        self.x -= x_vel
        self.y -= y_vel
        if self.x-self.rad <= 0 or self.x+self.rad >= self.screen.get_width():
            self.dx = -self.dx
        if self.y-self.rad <= 0 or self.y+self.rad >= self.screen.get_height():
            self.dy = -self.dy

    def rotateCircle(self):
        self.rads += .07
        self.x = self.screen.get_width()/2 + math.cos(self.rads)*self.p_rad
        self.y = self.screen.get_height()/2+math.sin(self.rads)*self.p_rad
