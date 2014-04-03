# Rectangle base class
#
# Capable of storing/drawing and image
# and testing if a point is inside of
# that image
#
# 2014/3/27
# written by Michael Shawn Redmond

import pygame
from config import *

class Rectangle:
    def __init__(self, position, image, width, height):
        self.position = position # topleft
        self.image = pygame.image.load(image)
        self.width = width
        self.height = height

    def calc_center(self):
        px, py = self.position
        cx, cy = px + .5*self.width, py + .5*self.height
        self.center = cx, cy

    def get_image(self):
        return self.image

    def set_image(self, image):
        self.image = pygame.image.load(image)

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position
        self.calc_center

    def get_center(self):
        return self.center

    def set_center(self, center):
        cx, cy = center
        px, py = cx - .5*self.width, cy - .5*self.height
        self.position = px, py
        self.center = cx, cy

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width
        self.calc_center

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height
        self.cacl_center

    def get_dims(self):
        return (self.get_width(), self.get_height())
    
    def paint(self, surface):
        surface.blit(self.image, self.position)

    def is_inside(self, position):
        if position[0] >= self.position[0] and position[0] < self.position[0] + self.width:
            if position[1] >= self.position[1] and position[1] < self.position[1] + self.height:
                return True
        return False
