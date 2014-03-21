# TowerDefense game subclass
# 2014/3/21
# written by Michael Shawn Redmond

import game
from config import *

class TowerDefense(game.Game):
    def __init__(self, name, screen_width, screen_height):
        # setup data members and the screen
        game.Game.__init__(self, name, screen_width, screen_width)
        self.world = world.World(WORLD_WIDTH, WORLD_HEIGHT, WORLD1)
        self.towers_types = [tower.Tower(TOWER_TYPES[i]) for i in range(TOWER_TYPE_COUNT)]
        self.towers_purchased = []
        self.money = STARTING_MONEY
        self.waves = [wave for wave in WAVES]
        self.wave = 0
        self.creeps_types = [creep.Creep(CREEP_TYPES[i]) for i in range(CREEP_TYPE_COUNT)]
        self.creeps_alive = []
        self.state = CLEAR
