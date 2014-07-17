# Towerpurchaser Class
#
# Displays a picture of a given
# tower and alerts the menu when
# the image is clicked to signal
# an the beginning of a purchase
# of a specific tower
#
# 2014/3/27
# written by Michael Shawn Redmond

import rectangle
from config import *

class TowerPurchaser():
    def __init__(self, position, towertype, tower_width, tower_height):
        self.position = position
        self.towertype = towertype
        self.tower = towertype(position)
        self.status = P_IDLE
        #self.follower = None
        self.width = tower_width
        self.height = tower_height
        
    def get_width(self):
        return self.width
        
    def get_height(self):
        return self.height
        
    def get_dims(self):
        return (self.get_width(), self.get_height())

    def paint(self, surface):
        self.tower.paint(surface)

    def toggle_status(self):
        if self.status == P_IDLE:
            self.status = P_FOLLOW
        else:
            self.status =  P_IDLE
            self.follower = None

    def game_logic(self, keys, newkeys, mouse_pos, newclicks):
        actions = []
        hover = self.tower.is_inside(mouse_pos)
        if hover:
            actions.append((P_HOVER, (self.position, self.tower.get_width(), self.tower.get_height(), self.tower.get_cost())))
        if MOUSE_LEFT in newclicks:
            if self.status == P_IDLE and hover:
                # if we were idle but the tower was clicked
                # tell the game that we want to start placing
                # a tower
                actions.append((P_FOLLOW, (self, self.towertype(self.position))))
                self.toggle_status()
            elif self.status == P_FOLLOW:
                # if we were following a tower and the user
                # just clicked, tell the game to try and
                # place the tower
                actions.append((P_PLACE, (self, self.towertype(self.position))))
                self.toggle_status()
        if MOUSE_RIGHT in newclicks:
            if self.status == P_FOLLOW:
                self.toggle_status()
        return actions
