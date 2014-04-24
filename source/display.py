from config import *
import pygame
import rectangle

class Display(rectangle.Rectangle):
    def __init__(self, position, width, height, color):
        self.position = position
        self.width = width
        self.height = height
        self.color = color
        self.data = {}
        self.active = True 
        self.item_image = None

    def add_data(self, name, value):
        self.data[name] = value # overwrites any existing data

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False
        self.item_image = None
        self.data = {}

    def add_image(self, image):
        self.item_image = image

    def paint(self, surface):
        r = pygame.Rect(self.position, (self.width, self.height))
        pygame.draw.rect(surface, self.color, r, MENU_OUTLINE_WIDTH)
