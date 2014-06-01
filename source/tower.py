# Tower Class
#
# Stores tower attributes and handles
# attacking, upgrading, selling, and
# drawing.
#
# 2014/3/21
# written by Michael Shawn Redmond

import pygame
from config import *
import rectangle
import math
import bullet

class Tower(rectangle.Rectangle):
    def __init__(self, position, width=TOWER_BASIC_WIDTH, height=TOWER_BASIC_HEIGHT, image=TOWER_BASIC_IMAGE, rng=TOWER_BASIC_RANGE, cost=TOWER_BASIC_COST, atk_speed=TOWER_BASIC_ATK_SPEED):
        rectangle.Rectangle.__init__(self, position, width, height, image)
        self.cost = cost
        self.range = rng
        self.active = False
        
        self.atk_speed = atk_speed
        # frames since last attack
        self.fs_last_attack = float(FRAMES_PER_SECOND)/self.atk_speed

        # true if the tower is in a good
        # (placable) location, else: false
        self.is_good = False

        # calculate the range once and store the
        # two different surfaces to avoid
        # unnecessary repetitive computation
        self.range_surface_good = pygame.Surface((self.range*2, self.range*2), pygame.SRCALPHA)
        self.range_surface_bad = pygame.Surface((self.range*2, self.range*2), pygame.SRCALPHA)
        self.generate_range()

        self.bullet_type = bullet.Bullet
        self.target = None
        self.bullets = set()
        self.name = "Basic Tower"

    def get_info(self):
        info = []
        line = "Tower: %s" %(self.name)
        info.append(line)
        line = "Cost: $%s" %(self.cost)
        info.append(line)
        line = "Range: %s" %(self.range)
        info.append(line)
        line = "AS: %s/sec" %(self.atk_speed)
        info.append(line)
        temp_bullet = self.bullet_type((0, 0))
        line = "Damage: %s" %(temp_bullet.get_damage())
        info.append(line)
        del temp_bullet
        return info

    def get_cost(self):
        return self.cost
        
    def set_range(self, new_range):
        self.range = new_range
        
    def get_range(self):
        return self.range
    
    def is_active(self):
        return self.active
        
    def activate(self):
        self.active = True
        
    def deactivate(self):
        self.active = False
        
    def is_in_range(self, position):
        px, py = position
        #cx, cy = self.get_position()
        cx, cy = self.get_center()
        distance = math.sqrt((px-cx)**2 + (py-cy)**2)
        return distance <= self.range

    def generate_range(self, color_good=RANGE_COLOR, color_bad=RANGE_BAD_COLOR):
        self.range_surface_good.fill((255, 255, 255, 0))
        self.range_surface_bad.fill((255, 255, 255, 0))
        # loop through each pixel in the rectangle
        # that contains the range and change its
        # color if it is inside the range
        # (excludes the corners of the rectangle)
        cx, cy = self.get_center()
        topleft = (cx - self.range, cy - self.range)
        for i in range(self.range_surface_good.get_width()):
            for j in range(self.range_surface_good.get_height()):
                if self.is_in_range((i + topleft[0], j + topleft[1])):
                    self.range_surface_good.set_at((i, j), color_good)
                    self.range_surface_bad.set_at((i, j), color_bad)

    def bad_pos(self):
        if self.is_good:
            self.is_good = False

    def good_pos(self):
        if not self.is_good:
            self.is_good = True
        
    def paint_range(self, surface):
        if self.is_active():
            # if the tower is selected
            # draw a partially transparent
            # circle to indicate its range
            # green if the tower is in a
            # good location, red otherwise
            cx, cy = self.get_center()
            topleft = (cx - self.range, cy - self.range)
            if self.is_good:
                surface.blit(self.range_surface_good, topleft)
            else:
                surface.blit(self.range_surface_bad, topleft)
                
    def can_attack(self):
        return self.fs_last_attack >= float(FRAMES_PER_SECOND)/self.atk_speed

    def attack(self, target):
        b = self.bullet_type(self.get_center())
        b.set_target(target)
        self.bullets.add(b)
     
    def paint(self, surface):
        surface.blit(self.image, self.position)

    def paint_bullets(self, surface):
        for bullet in self.bullets:
            bullet.paint(surface)
        
    def game_logic(self, keys, newkeys, mouse_pos, newclicks, creeps):
        self.fs_last_attack += 1 # frame count since last attack

        if self.target is not None and self.target.is_dead():
            self.target = None

        bullets_actions = []
        for bullet in self.bullets:
            bullet_actions = bullet.game_logic(keys, newkeys, mouse_pos, newclicks)
            for a in bullet_actions:
                if a is not None:
                    bullets_actions.append(a)
        actions = []
        for action in bullets_actions:
            if action[0] == B_DONE:
                self.bullets.remove(action[1])
            if action[0] == B_KILL:
                actions.append(action)
        
        # assumes that creeps is a list
        # of objects that have a position
        if self.is_inside(mouse_pos):
            if MOUSE_LEFT in newclicks:
                actions.append((T_SELECTED, self))

        if self.can_attack():
            if self.target is not None and self.is_in_range(self.target.get_center()):
                self.attack(self.target)
                self.fs_last_attack = 0
            else:
                for creep in creeps:
                    if self.is_in_range(creep.get_center()):
                        self.target = creep
                        self.attack(creep)
                        self.fs_last_attack = 0
                        break # only attack one creep at a time
        return actions
        
class GreenTower(Tower):
    def __init__(self, position):
        Tower.__init__(self, position, TOWER_GREEN_WIDTH, TOWER_GREEN_HEIGHT, TOWER_GREEN_IMAGE, TOWER_GREEN_RANGE, TOWER_GREEN_COST, TOWER_GREEN_ATK_SPEED)
        self.bullet_type = bullet.GreenBullet
        self.name = "Green Tower"
