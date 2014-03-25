import pygame
from config import *
import rectangle

class Creep(rectangle.Rectangle):
    def __init__(self, position, image, width, height):
        rectangle.Rectangle.__init__(self, position, image, width, height)
        self.health = CREEP_DEFAULT_HEALTH
        self.speed = CREEP_DEFAULT_SPEED
        self.speed_modifier = 1
        #self.resistances = CREEP_DEFAULT_RESISTANCES

    def hit(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

    def game_logic(self, keys, newkeys):
        pass
