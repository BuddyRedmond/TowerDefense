from config import *
import pygame
import rectangle

class Display(rectangle.Rectangle):
    def __init__(self, position, width, height, b_color = DISPLAY_BG_COLOR, o_color = DISPLAY_O_COLOR):
        self.position = position
        self.width = width
        self.height = height
        self.b_color = b_color
        self.o_color = o_color
        self.data = {}
        self.active = True
        self.left_margin = DISPLAY_MARGIN_LEFT
        self.item_image = None
        self.item_image_x = self.left_margin
        self.item_image_y = 0

    def add_data(self, data): # data is a list: [(key1, val1), (key2, val2)...]
        for pair in data:
            self.data[pair[0]] = pair[1]

    def add_datum(self, name, value):
        self.data[name] = value # overwrites any existing key-value pair

    def activate(self):
        self.active = True
        print "Activated"

    def deactivate(self):
        self.active = False
        self.item_image = None
        self.data = {}
        print "Deactivated"

    def set_image(self, image):
        self.item_image = image

    def paint(self, surface):
        d_surface = pygame.Surface((self.width, self.height))
        d_surface.fill(self.b_color)
        
        # Rectangle covering the area of the display
        r = pygame.Rect((0, 0), (self.width, self.height))
        pygame.draw.rect(d_surface, self.o_color, r, MENU_OUTLINE_WIDTH)

        # Image
        i = pygame.image.load("../assets/images/display/no_image.png")
        d_surface.blit(i, (self.item_image_x, self.item_image_y))

        # Stats

        surface.blit(d_surface, self.position)
