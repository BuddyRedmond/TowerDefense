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

class Tower(rectangle.Rectangle):
    def __init__(self, position, width=TOWER_BASIC_WIDTH, height=TOWER_BASIC_HEIGHT, image=TOWER_BASIC_IMAGE):
        rectangle.Rectangle.__init__(self, position, image, width, height)
        self.cost = 50

    def get_image(self):
        return self.image

    def get_cost(self):
        return self.cost
