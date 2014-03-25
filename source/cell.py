import pygame
from config import *
import rectangle

class Cell(rectangle.Rectangle):
    def __init__(self, position, image, width, height):
        rectangle.Rectangle.__init__(self, position, image, width, height)
