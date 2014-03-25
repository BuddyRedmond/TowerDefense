import pygame
from config import *

class Rectangle:
    def __init__(self, position, image, width, height):
        self.position = position
        self.image = image
        self.width = width
        self.height = height
        self.center = (position[0] + .5*width, position[1] + .5*height)

    def paint(self, surface):
        surface.blit(self.image, self.position)

    def is_inside(self, position):
        if position[0] >= self.position[0] and position[0] <= self.position[0] + self.width:
            if position[1] >= self.position[1] and position[1] <= self.position[1] + self.height:
                return True
        return False
