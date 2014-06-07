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
        self.data = []
        self.active = False
        self.left_margin = DISPLAY_MARGIN_LEFT
        self.top_margin = DISPLAY_MARGIN_TOP
        self.item_image = None
        self.item_image_x = self.left_margin
        self.item_image_y = 0
        self.data_x = self.width/3
        self.font = pygame.font.SysFont(DISPLAY_FONT, DISPLAY_FONT_SIZE)
        self.font_height = self.font.get_height()
        self.font_color = DISPLAY_FONT_COLOR

    def add_data(self, data): # data is a list: [(key1, val1), (key2, val2)...]
        for datum in data:
            self.add_datum(datum)

    def add_datum(self, datum):
        self.data.append(datum)
        self.data_ys.append(self.top_margin + (len(self.data)-1)*self.font_height)

    def activate(self):
        self.active = True
        if self.item_image is None:
            self.item_image = pygame.image.load("../assets/images/display/no_image.png")
            self.item_image_y = (self.height - DISPLAY_NO_IMG_HEIGHT)/2

    def deactivate(self):
        self.active = False
        self.item_image = None
        self.data = []
        self.data_ys = []

    def set_image(self, image, width, height):
        self.item_image = image
        self.item_image_y = (self.height - height)/2
        self.item_image_x = (self.data_x - width)/2

    def paint(self, surface):
        d_surface = pygame.Surface((self.width, self.height))
        d_surface.fill(self.b_color)
        
        # Rectangle covering the area of the display
        r = pygame.Rect((0, 0), (self.width, self.height))
        pygame.draw.rect(d_surface, self.o_color, r, MENU_OUTLINE_WIDTH)

        if self.active:
            # Image
            d_surface.blit(self.item_image, (self.item_image_x, self.item_image_y))

            # Stats
##            test = self.font.render("Testing", 1, self.font_color)
##            d_surface.blit(test, (self.data_x, self.top_margin))
            for i in range(len(self.data)):
                temp_surface = self.font.render(self.data[i], 1, self.font_color)
                d_surface.blit(temp_surface, (self.data_x, self.data_ys[i]))
                
        surface.blit(d_surface, self.position)
