# Menu Class
#
# Handles menu for buttons and
# purchasing icons.
#
# 2014/3/27
# written by Michael Shawn Redmond

import rectangle
import towerpurchaser
import pygame
from config import *

class Menu(rectangle.Rectangle):
    def __init__(self, position, width, height, color):
        self.position = position
        self.width = width
        self.height = height
        self.color = color
        self.items = []
        self.margin_x = MENU_ITEM_MARGIN_X
        self.margin_y = height/2

    def next_item_position(self, item):
        # calculates the next position in
        # the menu for an item
        x = self.position[0] + self.margin_x
        for item in self.items:
            x += item.get_width() + self.margin_x
        y = self.position[1] + self.margin_y - .5*item.get_height()
        return (x, y)

    def game_logic(self, keys, newkeys, mouse_pos, newclicks,):
        actions = []
        for item in self.items:
            # collect all of the actions of the
            # menu's items
            item_actions = item.game_logic(keys, newkeys, mouse_pos, newclicks)
            for action in item_actions:
                # filter out empty actions (just in case)
                if action is not None:
                    actions.append(action)
        return actions

    def add_purchaser(self, towertype):
        # add a specific item to the menu
        # of type purchaser
        tower = towertype((0, 0))
        pos = self.next_item_position(tower)
        self.items.append(towerpurchaser.TowerPurchaser(pos, towertype, tower.get_width(), tower.get_height()))

    def paint(self, surface):
        r = pygame.Rect(self.position, (self.width, self.height))
        pygame.draw.rect(surface, self.color, r)
        for item in self.items:
            item.paint(surface)
