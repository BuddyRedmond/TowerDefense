# Purchaser Class
#
# Displays a picture of a given
# object and alerts the menu when
# the image is clicked to signal
# an the beginning of a purchase
# of a specific obj
#
# 2014/3/27
# written by Michael Shawn Redmond

import rectangle
from config import *

class Purchaser():
    def __init__(self, position, objtype, obj_width, obj_height):
        self.position = position
        self.objtype = objtype
        self.obj = objtype(position)
        self.status = P_IDLE
        #self.follower = None
        self.width = obj_width
        self.height = obj_height
        
    def get_width(self):
        return self.width
        
    def get_height(self):
        return self.height
        
    def get_dims(self):
        return (self.get_width(), self.get_height())

    def paint(self, surface):
        self.obj.paint(surface)

    def toggle_status(self):
        if self.status == P_IDLE:
            self.status = P_FOLLOW
        else:
            self.status =  P_IDLE
            self.follower = None

    def game_logic(self, keys, newkeys, mouse_pos, newclicks):
        actions = []
        hover = self.obj.is_inside(mouse_pos)
        if hover:
            actions.append((P_HOVER, (self.position, self.obj.get_width(), self.obj.get_height(), self.obj.get_cost(), self.obj.kind)))
        if MOUSE_LEFT in newclicks:
            if self.status == P_IDLE and hover:
                # if we were idle but the obj was clicked
                # tell the game that we want to start placing
                # a obj
                actions.append((P_FOLLOW, (self, self.objtype(self.position))))
                self.toggle_status()
            elif self.status == P_FOLLOW:
                # if we were following a obj and the user
                # just clicked, tell the game to try and
                # place the obj
                actions.append((P_PLACE, (self, self.objtype(self.position))))
                self.toggle_status()
        if MOUSE_RIGHT in newclicks:
            if self.status == P_FOLLOW:
                self.toggle_status()
        return actions
