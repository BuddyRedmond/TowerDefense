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
    def __init__(self, position, width, height, image):
        self.position = position # topleft
        self.image = pygame.image.load(image)
        self.width = width
        self.height = height
        
    def collide(self, other):
        other_pos = other.get_position()
        other_width, other_height = other.get_dims()
        c1 = other_pos
        c2 = (other_pos[0] + other_width, other_pos[1])
        c3 = (other_pos[0] + other_width, other_pos[1] + other_height)
        c4 = (other_pos[0], other_pos[1] + other_height)
        if self.is_inside(c1) or self.is_inside(c2) or self.is_inside(c3) or self.is_inside(c4):
            return True
        return False

    def calc_center(self):
        px, py = self.position
        cx, cy = px + .5*self.width, py + .5*self.height
        return (int(cx), int(cy))

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
        return self.calc_center()

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
