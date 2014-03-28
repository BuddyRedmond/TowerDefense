# Menu Class
#
# Handles menu for buttons and
# purchasing icons.
#
# 2014/3/27
# written by Michael Shawn Redmond

import rectangle
import pygame

class Menu(rectangle.Rectangle):
    def __init__(self, position, width, height, color):
        self.position = position
        self.width = width
        self.height = height
        self.color = color
        self.items = []

    def next_item_position(self):
        x = self.position[0]
        for item in self.items:
            x += item.get_width() + self.margin
        y = self.position[1] + self.margin
        return (x, y)

    def add_item(self, item):
        item.set_position(self.next_item_position())
        self.items.append(item)

    def paint(self, surface):
        r = pygame.Rect(self.position, (self.width, self.height))
        pygame.draw.rect(surface, self.color, r)
        for item in self.items:
            item.paint(surface)
