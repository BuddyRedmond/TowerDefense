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
import time

class Tower(rectangle.Rectangle):
    # tower identifier used for reading map file
    ident = "".join(TOWER_DEFAULT_NAME.split()).lower()
    
    def __init__(self, position, width=TOWER_DEFAULT_WIDTH, height=TOWER_DEFAULT_HEIGHT, image=TOWER_DEFAULT_IMAGE, name=TOWER_DEFAULT_NAME, rng=TOWER_DEFAULT_RANGE, cost=TOWER_DEFAULT_COST, atk_speed=TOWER_DEFAULT_ATK_SPEED):
        rectangle.Rectangle.__init__(self, KIND_TOWER, position, width, height, image)
        self.cost = cost
        self.range = rng
        self.active = False
        self.level = 0

        ### bullet info ###
        self.bullet_damage = TOWER_DEFAULT_DAMAGE
        self.bullet_width = BULLET_DEFAULT_WIDTH
        self.bullet_height = BULLET_DEFAULT_HEIGHT
        self.bullet_image = BULLET_DEFAULT_IMAGE
        self.bullet_speed = BULLET_DEFAULT_SPEED
        
        self.atk_speed = atk_speed
        # frames since last attack
        self.last_attack = self.atk_speed[self.level]

        # true if the tower is in a good
        # (placable) location, else: false
        self.is_good = False

        # calculate the range once and store the
        # two different surfaces to avoid
        # unnecessary repetitive computation
        self.range_surface_good = pygame.Surface((self.range[self.level]*2, self.range[self.level]*2), pygame.SRCALPHA)
        self.range_surface_bad = pygame.Surface((self.range[self.level]*2, self.range[self.level]*2), pygame.SRCALPHA)
        self.generate_range()

        self.bullet_type = bullet.Bullet
        self.target = None
        self.bullets = set()
        self.name = name

    def can_be_upgraded(self):
        return self.level+1 < len(self.cost)

    def get_upgrade_cost(self):
        # sum up each level's cost
        if self.can_be_upgraded():
            return self.cost[self.level+1]
        else:
            return 0

    def get_total_cost(self):
        total_cost = 0
        for i in range(self.level+1):
            total_cost += self.cost[i]
        return total_cost

    def get_sell_amount(self):
        rounded = "%.2f" %(self.get_total_cost()*TOWER_SELL_RATE)
        return float(rounded)

    def upgrade(self):
        if self.can_be_upgraded():
            self.level += 1
            # recalculate the range areas and surfaces
            self.range_surface_good = pygame.Surface((self.range[self.level]*2, self.range[self.level]*2), pygame.SRCALPHA)
            self.range_surface_bad = pygame.Surface((self.range[self.level]*2, self.range[self.level]*2), pygame.SRCALPHA)
            self.generate_range()

    def get_hover_message(self):
        message = ""
        message += "%s" %(self.name)
        message += "\nDamage: %.2f" %(self.bullet_damage[self.level])
        message += "\nRange: %.2f" %(self.range[self.level])
        message += "\nAS: %.2f/sec" %(self.atk_speed[self.level])
        message += "\nCost: $%.2f" %(self.cost[self.level])
        return message

    def get_info(self):
        info = []
        line = "%s" %(self.name)
        info.append(line)
        line = "Level: %d" %(self.level+1)
        info.append(line)

##        line = "Cost to current level: %s" %(self.get_total_cost())
##        info.append(line)

        # only show the stats of the next level
        # if the tower can be upgraded
        if not self.can_be_upgraded():
            line = "Damage: %.2f" %(self.bullet_damage[self.level])
            info.append(line)
            line = "Range: %.2f" %(self.range[self.level])
            info.append(line)
            line = "AS: %.2f/sec" %(self.atk_speed[self.level])
            info.append(line)
            line = "Cost to upgrade: N/A"
            info.append(line)
        else:
            line = "Damage: %.2f (->%.2f)" %(self.bullet_damage[self.level], self.bullet_damage[self.level+1])
            info.append(line)
            line = "Range: %.2f (->%.2f)" %(self.range[self.level], self.range[self.level+1])
            info.append(line)
            line = "AS: %.2f/sec (->%.2f)" %(self.atk_speed[self.level], self.atk_speed[self.level+1])
            info.append(line)
            line = "Cost to upgrade: $%.2f" %(self.cost[self.level+1])
            info.append(line)
        line = "Sell value: $%.2f" %(self.get_sell_amount())
        info.append(line)
        return info

    def get_cost(self):
        return self.cost[self.level]
        
    def get_range(self):
        return self.range[self.level]
    
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
        return distance <= self.range[self.level]

    def generate_range(self, color_good=RANGE_COLOR, color_bad=RANGE_BAD_COLOR):
        self.range_surface_good.fill((255, 255, 255, 0))
        self.range_surface_bad.fill((255, 255, 255, 0))
        # loop through each pixel in the rectangle
        # that contains the range and change its
        # color if it is inside the range
        # (excludes the corners of the rectangle)
        cx, cy = self.get_center()
        topleft = (cx - self.range[self.level], cy - self.range[self.level])
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
            topleft = (cx - self.range[self.level], cy - self.range[self.level])
            if self.is_good:
                surface.blit(self.range_surface_good, topleft)
            else:
                surface.blit(self.range_surface_bad, topleft)
                
    def can_attack(self):
        return time.time() - self.last_attack >= 1.0/self.atk_speed[self.level]

    # create a bullet and set its target
    def attack(self, target):
        b = self.bullet_type(self.get_center(), self.bullet_width, self.bullet_height, self.bullet_image, self.bullet_damage[self.level], self.bullet_speed)
        b.set_target(target)
        self.bullets.add(b)
        self.last_attack = time.time()
     
    def paint(self, surface):
        if self.is_active():
            self.paint_range(surface)
        surface.blit(self.image, self.position)

    def paint_bullets(self, surface):
        for bullet in self.bullets:
            bullet.paint(surface)
        
    def game_logic(self, keys, newkeys, mouse_pos, newclicks, creeps):
        # if the target no longer exists, forget about it
        if self.target is not None and self.target.is_dead():
            self.target = None

        # call the tower's bullets' game logic methods
        # and collect the actions
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
        
        if self.is_inside(mouse_pos):
            if MOUSE_LEFT in newclicks:
                actions.append((T_SELECTED, self))

        # attacks a target, finds a target if none exist
        # assumes that creeps is a list
        # of objects that have a position
        if self.can_attack():
            if self.target is not None and self.is_in_range(self.target.get_center()):
                self.attack(self.target)
            else:
                for creep in creeps:
                    if self.is_in_range(creep.get_center()):
                        self.target = creep
                        self.attack(creep)
                        self.fs_last_attack = 0
                        break # only attack one creep at a time
        return actions

# Tower specific child classes
# Only changes needed are dimensions, name, range, image, cost and attack speed
class RedTower(Tower):
    ident = "".join(TOWER_RED_NAME.split()).lower()
    def __init__(self, position):
        Tower.__init__(self, position, TOWER_RED_WIDTH, TOWER_RED_HEIGHT, TOWER_RED_IMAGE, TOWER_RED_NAME, TOWER_RED_RANGE, TOWER_RED_COST, TOWER_RED_ATK_SPEED)
        self.bullet_type = bullet.Bullet
        ### bullet info ###
        self.bullet_damage = TOWER_RED_DAMAGE
        self.bullet_width = BULLET_RED_WIDTH
        self.bullet_height = BULLET_RED_HEIGHT
        self.bullet_image = BULLET_RED_IMAGE
        self.bullet_speed = BULLET_RED_SPEED
   
class GreenTower(Tower):
    ident = "".join(TOWER_GREEN_NAME.split()).lower()
    def __init__(self, position):
        Tower.__init__(self, position, TOWER_GREEN_WIDTH, TOWER_GREEN_HEIGHT, TOWER_GREEN_IMAGE, TOWER_GREEN_NAME, TOWER_GREEN_RANGE, TOWER_GREEN_COST, TOWER_GREEN_ATK_SPEED)
        self.bullet_type = bullet.Bullet
        ### bullet info ###
        self.bullet_damage = TOWER_GREEN_DAMAGE
        self.bullet_width = BULLET_GREEN_WIDTH
        self.bullet_height = BULLET_GREEN_HEIGHT
        self.bullet_image = BULLET_GREEN_IMAGE
        self.bullet_speed = BULLET_GREEN_SPEED

class BlueTower(Tower):
    ident = "".join(TOWER_BLUE_NAME.split()).lower()
    def __init__(self, position):
        Tower.__init__(self, position, TOWER_BLUE_WIDTH, TOWER_BLUE_HEIGHT, TOWER_BLUE_IMAGE, TOWER_BLUE_NAME, TOWER_BLUE_RANGE, TOWER_BLUE_COST, TOWER_BLUE_ATK_SPEED)
        self.bullet_type = bullet.Bullet
        ### bullet info ###
        self.bullet_damage = TOWER_BLUE_DAMAGE
        self.bullet_width = BULLET_GREEN_WIDTH
        self.bullet_height = BULLET_GREEN_HEIGHT
        self.bullet_image = BULLET_GREEN_IMAGE
        self.bullet_speed = BULLET_GREEN_SPEED
