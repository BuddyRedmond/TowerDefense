# Menu Class
#
# Handles menu for buttons and
# purchasing icons.
#
# 2014/3/27
# written by Michael Shawn Redmond

import rectangle
import towerpurchaser
import button
import pygame
from config import *

class Menu(rectangle.Rectangle):
    def __init__(self, position, width, height, b_color = MENU_BG_COLOR, o_color = MENU_O_COLOR):
        self.position = position
        self.width = width
        self.height = height
        self.b_color = b_color
        self.o_color = o_color
        self.items = []
        self.margin_x = MENU_ITEM_MARGIN_X
        self.margin_y = height/2

    def next_item_position(self, item):
        # calculates the next position in
        # the menu for an item
        y = .5*(self.height - item.get_height())#self.position[1] + .5*(self.height - item.get_height())
        x = self.margin_x#self.position[0] + self.margin_x
        for item in self.items:
            x += item.get_width() + self.margin_x
        return (x, y)

    def center_x(self):
        used_width = 0
        for item in self.items:
            used_width += item.get_width()
        used_width += (len(self.items)-1)*self.margin_x # width used to space buttons
        starting_x = (self.width-used_width)/2
        current_x = starting_x
        for item in self.items:
            x, y = item.get_position()
            x = current_x
            current_x += (item.get_width()+self.margin_x)
            item.set_position((x, y))

    def game_logic(self, keys, newkeys, mouse_pos, newclicks,):
        mx, my = mouse_pos[0] - self.position[0], mouse_pos[1] - self.position[1]
        actions = []
        for item in self.items:
            # collect all of the actions of the
            # menu's items
            item_actions = item.game_logic(keys, newkeys, (mx, my), newclicks)
            for action in item_actions:
                # filter out empty actions (just in case)
                if action is not None:
                    actions.append(action)
        return actions
        
    def add_button(self, buttontype):
        btn = buttontype((0, 0))
        pos = self.next_item_position(btn)
        btn.set_position(pos)
        self.items.append(btn)

    def add_purchaser(self, towertype):
        # add a specific item to the menu
        # of type purchaser
        tower = towertype((0, 0))
        pos = self.next_item_position(tower)
        self.items.append(towerpurchaser.TowerPurchaser(pos, towertype, tower.get_width(), tower.get_height()))

    def paint(self, surface):
        m_surface = pygame.Surface((self.width, self.height))
        m_surface.fill(self.b_color)
        
        r = pygame.Rect((0, 0), (self.width, self.height))
        pygame.draw.rect(m_surface, self.o_color, r, MENU_OUTLINE_WIDTH)
        for item in self.items:
            item.paint(m_surface)

        surface.blit(m_surface, self.position)
