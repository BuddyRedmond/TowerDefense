# World Class (includes the playing spaces, creeps, and towers)
# 2014/3/21
# written by Michael Shawn Redmond

from config import *

class World:
    def __init__(self, width, height, layout):
        self.width = width
        self.height = height
        self.creeps = []
        self.towers = []
        self.layout = self.parse_world(layout)

    def parse_world(self, layout_file):
        f = open(layout_file, 'rb')
        fin = f.readlines()
        f.close()
        
        return fin

w = World(200, 200, WORLD1)
print w.layout
