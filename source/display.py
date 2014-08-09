# Display class
#
# Displays an object to the screep
# along with the objects data
#
# 2014/4/23
# written by Michael Shawn Redmond

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
        self.margin_x = DISPLAY_MARGIN_LEFT
        self.margin_y = DISPLAY_MARGIN_TOP

        # data members for the item's display information
        self.item_image = None
        self.item_image_x = self.margin_x
        self.item_image_y = 0
        self.data_x = self.width/3

        self.font = pygame.font.SysFont(DISPLAY_FONT, DISPLAY_FONT_SIZE)
        self.font_height = self.font.get_height()
        self.font_color = DISPLAY_FONT_COLOR
        self.centered = False

    def format_datum(self, datum):
        lines = [datum]
        width = self.width - self.data_x - self.margin_x
        # format the details to fit in the display area
        while self.font.size(lines[-1])[0] > width:
            # m1 is the next line to be added
            m1 = lines[-1][:]
            # m2 is anything left over after m1 is removed
            m2 = ""

            # while we have room on the line, take a character
            # from m2 and place it in m1
            while self.font.size(m1)[0] > width:
                word = m1[-1]
                m1 = m1[:-1]

                # remove "words" to avoid multi-line words
                # "words" are determined by whitespace
                while not m1[-1].isspace():
                    word = m1[-1] + word
                    m1 = m1[:-1]
                    if len(m1) == 0:
                        break
                m2 = word + ' ' + m2
                m1 = m1[:-1]
            lines[-1] = m1
            lines.append(m2)
        return lines

    def add_data(self, data):
        for datum in data:
            lines = self.format_datum(datum)
            for line in lines:
                self.add_datum(line)

    # adds one piece of data at a time, calculating its positon
    def add_datum(self, datum):
        self.data.append(datum)
        self.data_ys.append(self.margin_y + (len(self.data)-1)*self.font_height)

    # begins showing the item
    def activate(self):
        self.active = True
        if self.item_image is None:
            self.item_image = pygame.image.load("../assets/images/display/no_image.png")
            self.item_image_y = (self.height - DISPLAY_NO_IMG_HEIGHT)/2
        self.centered = False

    # resets data and stops showing anything
    def deactivate(self):
        self.active = False
        self.item_image = None
        self.data = []
        self.data_ys = []

    # centers the content in the y direction
    def center_y(self):
        if not self.active or len(self.data) == 0:
            return

        # calculates the total height of all of the
        # lines of data
        text_height = self.data_ys[-1] - self.data_ys[0] + self.font_height

        # uses total height to place the starting point
        # in a position that will result in centered text
        top = (self.height - text_height) / 2
        offset = top - self.data_ys[0]
        for i in range(len(self.data_ys)):
            self.data_ys[i] += offset
        self.centered = True

    def set_image(self, image, width, height):
        self.item_image = image
        self.item_image_y = (self.height - height)/2
        self.item_image_x = (self.data_x - width)/2

    def paint(self, surface):
        # creates a surface for the display and
        # fills it with the display's background color
        d_surface = pygame.Surface((self.width, self.height))
        d_surface.fill(self.b_color)
        
        # Rectangle covering the area of the display
        r = pygame.Rect((0, 0), (self.width, self.height))
        pygame.draw.rect(d_surface, self.o_color, r, MENU_OUTLINE_WIDTH)

        # displays the item if active
        if self.active:
            # Image
            d_surface.blit(self.item_image, (self.item_image_x, self.item_image_y))

            # Stats
            if not self.centered:
                self.center_y()
            for i in range(len(self.data)):
                temp_surface = self.font.render(self.data[i], 1, self.font_color)
                d_surface.blit(temp_surface, (self.data_x, self.data_ys[i]))
        # draws the display surface onto the given surface      
        surface.blit(d_surface, self.position)
