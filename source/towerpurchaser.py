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
    def __init__(self, position, towertype):
        self.position = position
        self.towertype = towertype
        self.tower = towertype(position)
        self.status = P_IDLE
        self.follower = None

    def paint(self, surface):
        self.tower.paint(surface)
        if self.status == P_FOLLOW:
            self.follower.paint(surface)

    def toggle_status(self):
        if self.status == P_IDLE:
            self.status = P_FOLLOW
        else:
            self.status =  P_IDLE

    def game_logic(self, keys, newkeys, mouse_pos, newclicks):
        actions = []
        if self.status == P_FOLLOW:
            self.follower.set_center(mouse_pos)
        if 1 in newclicks: # left click
            if self.status == P_IDLE and self.tower.is_inside(mouse_pos):
                self.follower = self.towertype(self.position)
                actions.append((P_FOLLOW, self.towertype))
                self.toggle_status()
            elif self.status == P_FOLLOW :
                actions.append((P_PLACE, self.towertype))
                self.follower = None
                self.toggle_status()
        return actions
