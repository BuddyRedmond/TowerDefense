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
import healthbar

class Creep(rectangle.Rectangle):
    def __init__(self, position, width=CREEP_DEFAULT_WIDTH, height=CREEP_DEFAULT_HEIGHT, image=CREEP_DEFAULT_IMAGE, value=CREEP_DEFAULT_VALUE):
        rectangle.Rectangle.__init__(self, KIND_CREEP, position, width, height, image)
        self.health = self.max_health = CREEP_DEFAULT_HEALTH
        self.speed = CREEP_DEFAULT_SPEED
        self.value = value
        self.speed_modifier = 1
        self.destination = None
        self.visited = 0
        self.name = CREEP_DEFAULT_NAME

        health_pos = self.position[0] + .5* self.width - .5*HEALTH_BAR_WIDTH, self.position[1] - HEALTH_BAR_HEIGHT - HEALTH_BAR_MARGIN
        self.healthbar = healthbar.Healthbar(health_pos, self.max_health)
        #self.resistances = CREEP_DEFAULT_RESISTANCES

    def paint_health(self, surface):
        self.healthbar.paint(surface)

    def set_health_pos(self):
        self.healthbar.set_position((self.position[0] + .5* self.width - .5*HEALTH_BAR_WIDTH, self.position[1] - HEALTH_BAR_HEIGHT - HEALTH_BAR_MARGIN))

    def get_info(self):
        info = []
        line = "Creep: %s" %(self.name)
        info.append(line)
        line = "Health: %s" %(self.health)
        info.append(line)
        line = "Value: $%s" %(self.value)
        info.append(line)
        return info

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
        self.set_health_pos()

    def game_logic(self, keys, newkeys, mouse_pos, newclicks):
        self.healthbar.update_health(self.health)
        actions = []
        # if the creep was clicked, report it
        if MOUSE_LEFT in newclicks:
            if self.is_inside(mouse_pos):
                actions.append((C_SELECTED, self))
        if self.health <= 0:
            actions.append((C_DEAD, self))
        self.move()
        return actions
