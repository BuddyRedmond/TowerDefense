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
import time

class Creep(rectangle.Rectangle):
    # the creep's identifier used when reading the map file
    ident = "".join(CREEP_DEFAULT_NAME.split()).lower()
    def __init__(self, position, health=CREEP_DEFAULT_HEALTH, name=CREEP_DEFAULT_NAME, speed=CREEP_DEFAULT_SPEED, width=CREEP_DEFAULT_WIDTH, height=CREEP_DEFAULT_HEIGHT, image=CREEP_DEFAULT_IMAGE, value=CREEP_DEFAULT_VALUE):
        rectangle.Rectangle.__init__(self, KIND_CREEP, position, width, height, image)

        # setup the attributes of the creep
        self.health = self.max_health = health
        self.speed = speed
        self.value = value
        self.speed_modifier = 1

        self.destination = None

        # tracks the number of destinations reached
        self.visited = 0

        self.name = name

        # frame rate independent data
        self.last_frame = time.time()
        self.dt = 0

        # health bar data
        self.setup_healthbar()
        #self.resistances = CREEP_DEFAULT_RESISTANCES

    def setup_healthbar(self):
        health_pos = self.position[0] + .5* self.width - .5*HEALTH_BAR_WIDTH, self.position[1] - HEALTH_BAR_HEIGHT - HEALTH_BAR_MARGIN
        self.healthbar = healthbar.Healthbar(health_pos, self.max_health)

    def paint_health(self, surface):
        self.healthbar.paint(surface)

    def set_health_pos(self):
        # the health bar is set to be centered above the creep
        self.healthbar.set_position((self.position[0] + .5* self.width - .5*HEALTH_BAR_WIDTH, self.position[1] - HEALTH_BAR_HEIGHT - HEALTH_BAR_MARGIN))

    # return a list of the data to be displayed when
    # the creep is selected
    def get_info(self):
        info = []
        line = "Creep: %s" %(self.name)
        info.append(line)
        line = "Health: %s" %(self.health)
        info.append(line)
        line = "Value: $%s" %(self.value)
        info.append(line)
        line = "Speed: %.2f" %(self.speed*self.speed_modifier)
        info.append(line)
        return info

    # scales the creep's attributes
    def set_mod(self, mod):
        self.max_health *= mod
        self.health = self.max_health
        self.setup_healthbar()
        self.value *= mod

    def slow(self, amount):
        self.speed_modifier *= amount

    # handles collision
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

    # moves the creep to a destination if one is available    
    def move(self):
        if not self.has_destination():
            return

        # if we have a destination, calculate its
        # difference in position with the creep
        x, y = self.position
        dx = self.destination[0]-x
        dy = self.destination[1]-y
        on_left = dx < 0
        above = dy < 0
        # move as much as possible to the destination
        # without passing it
        dx = min(abs(dx), self.speed*self.speed_modifier*self.dt)
        dy = min(abs(dy), self.speed*self.speed_modifier*self.dt)
        if on_left:
            dx *= -1
        if above:
            dy *= -1
        self.position = (x + dx, y + dy)

        # visit the destination if it was reached
        if self.position == self.destination:
            self.visited += 1
            self.destination = None

    def game_logic(self, keys, newkeys, mouse_pos, newclicks):
        # frame rate independend calculations
        t = time.time()
        self.dt = t - self.last_frame
        self.last_frame = t

        # update the health bar
        self.healthbar.update_health(self.health)
        self.set_health_pos()
        
        actions = []
        # if the creep was clicked, report it
        if MOUSE_LEFT in newclicks:
            if self.is_inside(mouse_pos):
                actions.append((C_SELECTED, self))
        # if the creep died, report it
        if self.health <= 0:
            actions.append((C_DEAD, self))
        self.move()
        self.speed_modifier = 1
        return actions

# Creep specific child classes
# Only changes required are health, name, dimensions, image, speed, and value
class RedCreep(Creep):
    ident = "".join(CREEP_RED_NAME.split()).lower()
    def __init__(self, position):
        Creep.__init__(self, position, CREEP_RED_HEALTH, CREEP_RED_NAME, CREEP_RED_SPEED, CREEP_RED_WIDTH, CREEP_RED_HEIGHT, CREEP_RED_IMAGE, CREEP_RED_VALUE)

class YellowCreep(Creep):
    ident = "".join(CREEP_YELLOW_NAME.split()).lower()
    def __init__(self, position):
        Creep.__init__(self, position, CREEP_YELLOW_HEALTH, CREEP_YELLOW_NAME, CREEP_YELLOW_SPEED, CREEP_YELLOW_WIDTH, CREEP_YELLOW_HEIGHT, CREEP_YELLOW_IMAGE, CREEP_YELLOW_VALUE)

class BlueCreep(Creep):
    ident = "".join(CREEP_BLUE_NAME.split()).lower()
    def __init__(self, position):
        Creep.__init__(self, position, CREEP_BLUE_HEALTH, CREEP_BLUE_NAME, CREEP_BLUE_SPEED, CREEP_BLUE_WIDTH, CREEP_BLUE_HEIGHT, CREEP_BLUE_IMAGE, CREEP_BLUE_VALUE)
