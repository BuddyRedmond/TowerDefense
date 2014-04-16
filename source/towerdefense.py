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
import button

class TowerDefense(game.Game):
    def __init__(self, name, screen_width, screen_height):
        # setup data members and the screen
        game.Game.__init__(self, name, screen_width, screen_height)

        ### World setup ###
        world_pos_x = (self.width - WORLD_DEFAULT_WIDTH)/2
        if world_pos_x < 0:
            world_pos_x = MARGIN
        world_pos_y = MARGIN
        self.world = world.World((world_pos_x, world_pos_y), WORLD_DEFAULT_WIDTH, WORLD_DEFAULT_HEIGHT, WORLD1)

        ### Menu setup ###
        self.menu = menu.Menu((world_pos_x, world_pos_y + WORLD_DEFAULT_HEIGHT + MARGIN), WORLD_DEFAULT_WIDTH*.5, MENU_HEIGHT, MENU_COLOR)
        
        #self.buttons = [button.NewWave]                      
        #for btn in self.buttons:
        #    self.menu.add_button(btn)
            
        self.towers_types = [tower.Tower, tower.GreenTower]
        for tt in self.towers_types:
            self.menu.add_purchaser(tt)
        
        self.towers = []
        self.money = STARTING_MONEY
        self.wave = 0
        self.creep_types = [creep.Creep]
        self.creeps = []
        self.state = TD_CLEAR
        self.sub_state = TD_IDLE
        self.purchaser = None
        self.selected = None
        
        self.count = 0

    def paint(self, surface):
        surface.fill(BACKGROUND_COLOR)
        self.world.paint(surface)
        self.menu.paint(surface)
        for creep in self.creeps:
            creep.paint(surface)
        if self.sub_state == TD_SHOW:
            if self.selected is not None:
                self.selected.paint_range(surface)
        elif self.sub_state == TD_FOLLOW:
            if self.purchaser is not None:
                if not self.world.can_build(self.purchaser.get_position(), self.purchaser.get_dims()):
                    self.purchaser.bad_pos()
                    self.purchaser.paint_range(surface)
                else:
                    self.purchaser.good_pos()
                    self.purchaser.paint_range(surface)
                self.purchaser.paint(surface)
        for tower in self.towers:
            tower.paint(surface)
            
    def begin_wave(self):
        self.wave += 1
        if self.wave > len(WAVES)-1:
            return
        for i in range(CREEP_COUNT):
            for j in range(WAVES[self.wave][i]):
                c = self.creep_types[i]((0, 0))
                x, y = self.world.get_start()
                c.set_position((-(j+1)*c.get_width(), y))
                c.set_destination(self.world.next_waypoint(0))
                self.creeps.append(c)

    def game_logic(self, keys, newkeys, mouse_pos, newclicks):
        remaining_creeps = []
        for creep in self.creeps:
            if not creep.has_destination():
                dest = self.world.next_waypoint(creep.get_visited())
                if dest is not None:
                    creep.set_destination(self.world.next_waypoint(creep.get_visited()))
                    remaining_creeps.append(creep)
            else:
                remaining_creeps.append(creep)
        self.creeps = remaining_creeps[:]
        if self.sub_state == TD_FOLLOW:
            # if we are placing a tower
            # snap its location to the
            # cells of the world
            if self.world.is_inside(mouse_pos):
                cell_num = self.world.get_cell_at(mouse_pos)
                snap_loc = self.world.get_cell_top_left(cell_num)
            else:
                snap_loc = mouse_pos
            self.purchaser.set_position(snap_loc)
        
        # collect actions for menu
        actions = []
        menu_actions = self.menu.game_logic(keys, newkeys, mouse_pos, newclicks)
        for action in menu_actions:
            if action is not None:
                actions.append(action)
        
        # collect actions for towers
        for tower in self.towers:
            tower_actions = tower.game_logic(keys, newkeys, mouse_pos, newclicks, self.creeps)
            for action in tower_actions:
                if action is not None:
                    actions.append(action)
        
        # handle actions
        for action in actions:
            if action[0] == P_FOLLOW:
                # if we clicked on a menu item
                # to start placing a tower
                # keep track of that tower
                if self.sub_state == TD_SHOW:
                    self.selected.deactivate()
                    self.selected = None
                self.sub_state = TD_FOLLOW
                self.purchaser = action[1]
                self.purchaser.activate()
                pygame.mouse.set_visible(False)
            elif action[0] == P_PLACE:
                # verify ability to place tower
                f_pos = self.purchaser.get_position()
                f_dims = self.purchaser.get_dims()
                cell_num = self.world.get_cell_at(f_pos)
                placed = False
                if self.world.has_cell(cell_num):
                    if self.purchaser.get_cost() <= self.money:
                        if self.world.can_build(f_pos, f_dims):
                            self.world.occupy_area(f_pos, f_dims)
                            self.purchaser.activate()
                            self.towers.append(self.purchaser)
                            self.money -= self.purchaser.get_cost()
                            self.selected = self.purchaser
                            self.sub_state = TD_SHOW
                            placed = True
                if not placed:
                    self.sub_state = TD_IDLE
                self.purchaser = None
                pygame.mouse.set_visible(True)
            elif action[0] == T_SELECTED:
                # if we clicked on a tower
                # stop showing the range
                # of the previously selected
                # tower and show this tower's
                # range
                if self.sub_state == TD_FOLLOW:
                    self.purchaser = None
                if self.selected is not None:
                    self.selected.deactivate()
                    self.selected = None
                self.selected = action[1]
                self.selected.activate()
                self.sub_state = TD_SHOW
            elif action[0] == T_FIRE:
                self.count += 1
                print action[1]
                print self.count
        if 1 in newclicks: # left mouse click
            # if we clicked on an empty cell
            # stop showing the previously
            # selected tower's range
            cell_num = self.world.get_cell_at(mouse_pos)
            if self.sub_state == TD_SHOW:
                if self.world.has_cell(cell_num) and not self.world.is_occupied(cell_num):
                    self.selected.deactivate()
                    self.selected = None
                    self.sub_state = TD_IDLE
                    
        for creep in self.creeps:
            creep.game_logic(keys, newkeys, mouse_pos, newclicks)
                    
        if len(self.creeps) == 0:
            self.begin_wave()
