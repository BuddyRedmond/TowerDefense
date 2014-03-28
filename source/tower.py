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
    def __init__(self, position, image, width, height):
        rectangle.Rectangle.__init__(self, position, image, width, height)
