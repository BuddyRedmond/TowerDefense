# Creep Class
#
# Handles creep's health, speed,
# and various attributes, taking
# damage, moving, and drawing.
#
# 2014/3/27
# written by Michael Shawn Redmond

import pygame
from config import *
import rectangle

class Creep(rectangle.Rectangle):
    def __init__(self, position, width=CREEP_DEFAULT_WIDTH, height=CREEP_DEFAULT_HEIGHT, image=CREEP_DEFAULT_IMAGE, value=CREEP_DEFAULT_VALUE):
        rectangle.Rectangle.__init__(self, position, width, height, image)
        self.health = CREEP_DEFAULT_HEALTH
        self.speed = CREEP_DEFAULT_SPEED
        self.value = value
        self.speed_modifier = 1
        self.destination = None
        self.visited = 0
        #self.resistances = CREEP_DEFAULT_RESISTANCES

    def hit(self, damage):
        self.health -= damage

    def get_value(self):
        return self.value

    def is_alive(self):
        return self.health > 0
        
    def set_destination(self, position):
        self.destination = position
        
    def has_destination(self):
        return self.destination is not None

    def get_visited(self):
        return self.visited

    def is_dead(self):
        return self.health <= 0
        
    def move(self):
        if not self.has_destination():
            return
        x, y = self.position
        dx = self.destination[0]-x
        dy = self.destination[1]-y
        on_left = dx < 0
        above = dy < 0
        dx = min(abs(dx), self.speed*self.speed_modifier)
        dy = min(abs(dy), self.speed*self.speed_modifier)
        if on_left:
            dx *= -1
        if above:
            dy *= -1
        self.position = (x + dx, y + dy)
        if self.position == self.destination:
            self.visited += 1
            self.destination = None

    def game_logic(self, keys, newkeys, mouse_pos, newclicks):
        actions = []
        if self.health <= 0:
            actions.append((C_DEAD, self))
        self.move()
        return actions
