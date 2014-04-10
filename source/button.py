from config import *
import pygame
import rectangle

class Button(rectangle.Rectangle):
    def __init__(self, position, width, height, image):
        rectangle.Rectangle.__init__(self, position, width, height, image)
        self.message = None
        self.item = None
        
    def game_logic(self, keys, newkeys, mouse_pos, newclicks):
        actions = []
        if 1 in newclicks: # left mouse click
            if self.is_inside(mouse_pos):
                actions.append((self.message, self.item))
        return actions
                
class NewWave(Button):
    def __init__(self, position):
        Button.__init__(self, position, BUTTON_NEW_WAVE_WIDTH, BUTTON_NEW_WAVE_HEIGHT, BUTTON_NEW_WAVE_IMG)
        self.message = BUTTON_NEW_WAVE_MSG
        self.item = None
