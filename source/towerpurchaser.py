# Towerpurchaser Class
#
# Displays a picture of a given
# tower and, when clicked, has
# a copy of the image follow the
# cursor, when clicked again,
# creates a tower matching the
# one displayed.
#
# 2014/3/27
# written by Michael Shawn Redmond

import rectangle

class TowerPurchaser(rectangle.Rectangle):
    def __init__(self, position, image, width, height, towerType):
        rectangle.Rectangle.__init__(self, position, image, width, height)
        self.towerType = towerType
        self.status = "idle" # status can be "idle" or "follow"

    def onClick(self):
        if self.status == "idle":
            self.status = "follow"
