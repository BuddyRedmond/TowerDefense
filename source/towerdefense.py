# TowerDefense game subclass
#
# Stores the items necessary for
# a game of tower defense. Handles
# tower, creep, map, menu, and
# money storage, user input,
# and changing the states of
# the game.
#
# 2014/3/21
# written by Michael Shawn Redmond

import pygame
from config import *
import game
import creep
import world
import tower
import menu

class TowerDefense(game.Game):
    def __init__(self, name, screen_width, screen_height):
        # setup data members and the screen
        game.Game.__init__(self, name, screen_width, screen_width)
        world_pos_x = (screen_width - WORLD_DEFAULT_WIDTH)/2
        world_pos_y = MARGIN
        self.world = world.World((world_pos_x, world_pos_y), \
                                 WORLD_DEFAULT_WIDTH, WORLD_DEFAULT_HEIGHT, WORLD1)
        self.menu = menu.Menu((world_pos_x, \
                               world_pos_y + WORLD_DEFAULT_HEIGHT + MARGIN), \
                              WORLD_DEFAULT_WIDTH, \
                              screen_height - (world_pos_y + WORLD_DEFAULT_HEIGHT + 2*MARGIN), \
                              MENU_COLOR)
        self.towers_types = [tower.Tower]
        self.towers = []#[tower.Tower((16,16), pygame.image.load(TOWER_BASIC_IMAGE), TOWER_BASIC_WIDTH, TOWER_BASIC_HEIGHT)]
        self.money = STARTING_MONEY
        #self.waves = [wave for wave in WAVES]
        self.wave = 0
        #self.creeps_types = [creep.Creep(CREEP_TYPES[i]) for i in range(CREEP_TYPE_COUNT)]
        self.creeps = []#[creep.Creep((0,0), pygame.image.load(CREEP_DEFAULT_IMAGE), CREEP_DEFAULT_WIDTH, CREEP_DEFAULT_HEIGHT)]
        self.state = CLEAR

    def paint(self, surface):
        self.world.paint(surface)
        self.menu.paint(surface)
        for creep in self.creeps:
            creep.paint(surface)
        for tower in self.towers:
            tower.paint(surface)

    def game_logic(self, keys, newkeys):
        pos = pygame.mouse.get_pos()
