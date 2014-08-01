# Healthbar class
#
# Displays the health of an object
# with a red rectangle, representing
# the total health, under a green
# rectangle, representing the current
# health
#
# 2014/6/12
# written by Michael Shawn Redmond

import pygame
from config import *

class Healthbar:
    def __init__(self, pos, max_health, width = HEALTH_BAR_WIDTH, height = HEALTH_BAR_HEIGHT):
        self.max_health = max_health
        self.position = pos
        self.current_health = max_health
        self.width = width
        self.height = height
        self.current_width = width
        self.bg_color = HEALTH_BAR_BG_COLOR
        self.color = HEALTH_BAR_COLOR
        self.place_bar()

    # creates the rectangles that represent the health
    def place_bar(self):
        self.bg = pygame.rect.Rect(self.position, (self.width, self.height))
        self.current = pygame.rect.Rect(self.position, (self.current_width, self.height))

    # updates the current healthbar's width
    # to show the appropriate percentage
    # of health remaining
    def update_health(self, value):
        if self.current_health != value:
            self.current_health = value
            perc = float(self.current_health) / self.max_health
            self.current_width = min(self.width, self.width*perc)

    def set_position(self, pos):
        self.position = pos
        self.place_bar()

    def paint(self, surface):
        pygame.draw.rect(surface, self.bg_color, self.bg)
        pygame.draw.rect(surface, self.color, self.current)
