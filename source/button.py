# Button class
#
# Rectangular object that displays an image,
# can respond to mouse-overs, and
# send a message on click
#
# 2014/4/9
# written by Michael Shawn Redmond

from config import *
import pygame
import rectangle

class Button(rectangle.Rectangle):
    def __init__(self, position, width, height, image, image_hover):
        # image shown when the mouse is on the button
        self.image_hover = pygame.image.load(image_hover)
        
        rectangle.Rectangle.__init__(self, KIND_BUTTON, position, width, height, image)

        # mouse-over data
        self.message = None
        self.hover = False

        # message shown on mouse-over
        self.description = ""

        # object to be sent on click
        self.item = None

    def paint(self, surface):
        # display the hover image on mouse-overs
        if self.hover:
            surface.blit(self.image_hover, self.position)
        # otherwise use the normal image
        else:
            surface.blit(self.image, self.position)
        
    def game_logic(self, keys, newkeys, mouse_pos, newclicks):
        actions = []
        # if the mouse is on the button, set the hover data member
        if self.is_inside(mouse_pos):
            self.hover = True

            # if the button was clicked, send a message with the applicable item
            if MOUSE_LEFT in newclicks:
                actions.append((self.message, self.item))
        # reset the hover data member if the mouse is not on the button
        else:
            self.hover = False
        return actions

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_item(self):
        return self.item

    def set_item(self, item):
        self.item = item

# Button-specific child classes
# Only changes needed are the message, image, dimensions, message, and item
class NewWave(Button):
    def __init__(self, position = (0, 0)):
        Button.__init__(self, position, BUTTON_NEW_WAVE_WIDTH, BUTTON_NEW_WAVE_HEIGHT, BUTTON_NEW_WAVE_IMG, BUTTON_NEW_WAVE_HOVER_IMG)
        self.message = BUTTON_NEW_WAVE_MSG
        self.item = None

class Upgrade(Button):
    def __init__(self, position = (0, 0)):
        Button.__init__(self, position, BUTTON_UPGRADE_WIDTH, BUTTON_UPGRADE_HEIGHT, BUTTON_UPGRADE_IMG, BUTTON_UPGRADE_HOVER_IMG)
        self.message = BUTTON_UPGRADE_MSG
        self.item = None

class Sell(Button):
    def __init__(self, position = (0, 0)):
        Button.__init__(self, position, BUTTON_SELL_WIDTH, BUTTON_SELL_HEIGHT, BUTTON_SELL_IMG, BUTTON_SELL_HOVER_IMG)
        self.message = BUTTON_SELL_MSG
        self.item = None

class Play(Button):
    def __init__(self, position = (0, 0)):
        Button.__init__(self, position, BUTTON_PLAY_WIDTH, BUTTON_PLAY_HEIGHT, BUTTON_PLAY_IMG, BUTTON_PLAY_HOVER_IMG)
        self.message = BUTTON_PLAY_MSG
        self.item = None

class Quit(Button):
    def __init__(self, position = (0, 0)):
        Button.__init__(self, position, BUTTON_QUIT_WIDTH, BUTTON_QUIT_HEIGHT, BUTTON_QUIT_IMG, BUTTON_QUIT_HOVER_IMG)
        self.message = BUTTON_QUIT_MSG
        self.item = None

class Level(Button):
    def __init__(self, position = (0, 0), name = ""):
        Button.__init__(self, position, BUTTON_LEVEL_WIDTH, BUTTON_LEVEL_HEIGHT, BUTTON_LEVEL_IMG, BUTTON_LEVEL_HOVER_IMG)
        self.message = BUTTON_LEVEL_MSG
        # where self.item is the name of the map file
        self.item = name
