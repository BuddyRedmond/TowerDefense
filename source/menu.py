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
        self.margin_y = MENU_ITEM_MARGIN_Y

    def clear(self):
        self.items = []

    # calculates the next position in
    # the menu for an item
    def next_item_position(self, item):
        y = .5*(self.height - item.get_height())
        x = self.margin_x
        for item in self.items:
            x += item.get_width() + self.margin_x
        return (x, y)

    # centers the menu in the x direction
    def center_x(self):
        # calculate the total width needed for all
        # of the items
        used_width = 0
        for item in self.items:
            used_width += item.get_width()
        used_width += (len(self.items)-1)*self.margin_x # width used to space buttons

        # reposition the items based on the
        # starting position that will center
        # the entire menu
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
        btn = buttontype()
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
        # create a surface for the menu and fill
        # it with the menu's background color
        m_surface = pygame.Surface((self.width, self.height))
        m_surface.fill(self.b_color)

        # draw all of the items onto the menu's surface
        r = pygame.Rect((0, 0), (self.width, self.height))
        pygame.draw.rect(m_surface, self.o_color, r, MENU_OUTLINE_WIDTH)
        for item in self.items:
            item.paint(m_surface)

        # draw the menu's surface to the given surface
        surface.blit(m_surface, self.position)

# A child class of Menu that is centered vertically, and has a banner
class VerticalMenu(Menu):
    def __init__(self, position, width, height, b_color = MENU_BG_COLOR, o_color = MENU_O_COLOR):
        Menu.__init__(self, position, width, height, b_color, o_color)

        # the banner is an optional image to be place at the top
        # of the menu. Must have same width and smaller or same
        # height as the menu
        self.banner = None
        self.banner_height = 0
        ### setup font ###
        self.font = pygame.font.SysFont(FONT, FONT_SIZE)
        self.font_color = FONT_COLOR

    def paint(self, surface):
        # create a surface for the menu and fill
        # it with the menu's background color
        m_surface = pygame.Surface((self.width, self.height))
        m_surface.fill(self.b_color)

        # draw the banner, if there is one
        if self.banner is not None:
            m_surface.blit(self.banner, (0, 0))

        # draw all of the items onto the menu's surface
        r = pygame.Rect((0, 0), (self.width, self.height))
        pygame.draw.rect(m_surface, self.o_color, r, MENU_OUTLINE_WIDTH)
        for item in self.items:
            item.paint(m_surface)
            ### show description ###
            description= "%s" %(item.get_description())
            msg_dims = self.font.size(description)
            temp_surface = self.font.render(description, 1, self.font_color)
            item_pos = item.get_position()
            msg_x = item_pos[0] + item.get_width() + self.margin_x
            msg_y = item_pos[1] + .5*(item.get_height() - msg_dims[1])
            m_surface.blit(temp_surface, (msg_x, msg_y))

        # draw the menu's surface to the given surface
        surface.blit(m_surface, self.position)

    # calculates the next position in
    # the menu for an item   
    def next_item_position(self, item):
        x = self.margin_x
        y = self.margin_y + self.banner_height
        for item in self.items:
            y += item.get_height() + self.margin_y
        return (x, y)

    def set_banner(self, img):
        self.banner = pygame.image.load(img)
        if self.banner.get_width() != self.width:
            self.banner = None
            return
        self.banner_height = self.banner.get_height()
        # reposition items

    def remove_banner(self):
        self.banner = None
        self.banner_height = 0
        # reposition items
        temp_items = self.items[:]
        self.items = []
        for item in self.items:
            item.set_position(self.next_item_position(item))
            self.items.append(item)

    # adds a button to the menu given its
    # type, data, and description
    def add_button(self, buttontype, item = None, description = ""):
        btn = buttontype()
        btn.set_item(item)
        btn.set_description(description)
        pos = self.next_item_position(btn)
        btn.set_position(pos)
        self.items.append(btn)
