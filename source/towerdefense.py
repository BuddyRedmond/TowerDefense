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
import display
from os import path

class TowerDefense(game.Game):
    def __init__(self, name, screen_width, screen_height, screen = None):
        # setup data members and the screen
        game.Game.__init__(self, name, screen_width, screen_height, screen)

        ### Display setup ###
        self.display = display.Display((DISPLAY_X, DISPLAY_Y), DISPLAY_WIDTH, DISPLAY_HEIGHT, DISPLAY_BG_COLOR, DISPLAY_O_COLOR)

        self.empty_data()

        self.menu = None
        self.towers_types = [tower.Tower, tower.GreenTower]
        self.b_menu = None
        self.buttons = [button.NewWave, button.Upgrade, button.Sell]
        self.creep_types = [creep.Creep]

        ### setup font ###
        self.font = pygame.font.SysFont(FONT, FONT_SIZE)
        self.font_color = FONT_COLOR

        ### Main menu setup ###
        self.mm = menu.Menu(MM_POS, MM_WIDTH, MM_HEIGHT, MM_BG_COLOR, MM_O_COLOR)
        self.mm_buttons = [button.Play, button.Quit]
        for btn in self.mm_buttons:
            self.mm.add_button(btn)
        self.mm.center_x()
        self.mm_img = pygame.image.load(MM_IMG)

        ### Level select setup ###
        self.ls = menu.VerticalMenu(LS_POS, LS_WIDTH, LS_HEIGHT, LS_BG_COLOR, LS_O_COLOR)
        self.ls.set_banner(LS_IMG)
        self.ls_buttons = LEVELS
        for i in range(len(self.ls_buttons)):
            self.ls.add_button(button.Level, self.ls_buttons[i][0], self.ls_buttons[i][1])

        ### setup location for money ###
        self.money_x = MONEY_X
        self.money_y = MONEY_Y

        ### setup location for lives ###
        self.lives_x = LIVES_X
        self.lives_y = LIVES_Y

        ### setup location for wave number ###
        self.wave_x = WAVE_X
        self.wave_y = WAVE_Y

        ###  Purchaser menu setup ###
        self.menu = menu.Menu((MENU_P_X, MENU_P_Y), MENU_P_WIDTH, MENU_P_HEIGHT, MENU_P_BG_COLOR, MENU_P_O_COLOR)
        for tt in self.towers_types:
            self.menu.add_purchaser(tt)

        ### Button menu setup ###
        self.b_menu = menu.Menu((MENU_B_X, MENU_B_Y), MENU_B_WIDTH, MENU_B_HEIGHT, MENU_B_BG_COLOR, MENU_B_O_COLOR)
        
        self.buttons = [button.NewWave, button.Upgrade, button.Sell, button.Quit]                      
        for btn in self.buttons:
            self.b_menu.add_button(btn)
        self.b_menu.center_x()


    def load_level(self, level):
        ### World setup ###
        self.world = world.World((WORLD_X, WORLD_Y), WORLD_WIDTH, WORLD_HEIGHT, level)
        self.towers = []
        self.money = STARTING_MONEY
        self.wave = 0
        self.wave_comp = 0
        self.lives = STARTING_LIVES
        self.creeps = set()
        self.state = TD_CLEAR
        self.sub_state = TD_IDLE
        self.purchaser = None
        self.selected = None
        self.selected_rect = pygame.rect.Rect((0, 0), (0, 0))
        self.selected_rect_set = False
        self.display.deactivate()

    def empty_data(self):
        # initialize empty values #
        self.world = None
        self.towers = []
        self.money = 0
        self.wave = 0
        self.waves_comp = 0
        self.lives = 0
        self.creeps = set()
        self.state = TD_MENU
        self.sub_state = TD_IDLE
        self.purchaser = None
        self.selected = None
        self.selected_rect = pygame.rect.Rect((0, 0), (0, 0))
        self.selected_rect_set = False
        self.display.deactivate()

    def can_start_wave(self):
        return self.state == TD_CLEAR and self.wave+1 <= len(WAVES)-1

    def set_selected_rect(self):
        if self.selected_rect_set:
            return
        dims = self.selected.get_dims()
        dims = (dims[0] + SELECTED_O_WIDTH*2, dims[1] + SELECTED_O_WIDTH*2)
        pos = self.selected.get_position()
        pos = (pos[0] - SELECTED_O_WIDTH, pos[1] - SELECTED_O_WIDTH)
        self.selected_rect = pygame.rect.Rect(pos, dims)

    def paint(self, surface):
        surface.fill(BG_COLOR)
        if self.state == TD_MENU:
            surface.blit(self.mm_img, MM_IMG_POS)
            self.mm.paint(surface)
        elif self.state == TD_LEVEL_SELECT:
            self.mm.paint(surface)
            self.ls.paint(surface)
        else:
            self.world.paint(surface)
            self.menu.paint(surface)
            self.b_menu.paint(surface)
            self.display.paint(surface)

            ### show money ###
            currency = "Current money: $%s" %(self.money)
            temp_surface = self.font.render(currency, 1, self.font_color)
            surface.blit(temp_surface, (self.money_x, self.money_y))

            ### show lives ###
            lives = "Number of Lives: %d" %(self.lives)
            temp_surface = self.font.render(lives, 1, self.font_color)
            surface.blit(temp_surface, (self.lives_x, self.lives_y))

            ### show wave number ###
            wave = "Waves completed: %d" %(self.waves_comp)
            temp_surface = self.font.render(wave, 1, self.font_color)
            surface.blit(temp_surface, (self.wave_x, self.wave_y))

            # paint all of the creeps
            for creep in self.creeps:
                if self.selected != creep:
                    creep.paint(surface)

            # paint health bars of the creeps
            for creep in self.creeps:
                creep.paint_health(surface)

            # paint the purchaser if there is one
            if self.sub_state == TD_FOLLOW:
                if self.purchaser is not None:
                    self.purchaser.paint(surface)

            for tower in self.towers:
                if self.selected !=tower:
                    tower.paint(surface)

            if self.selected is not None:
                self.selected.paint(surface)
                self.set_selected_rect()
                pygame.draw.rect(surface, SELECTED_O_COLOR, self.selected_rect, SELECTED_O_WIDTH)

            for tower in self.towers:
                tower.paint_bullets(surface)
            
    def begin_wave(self):
        if not self.can_start_wave():
            return
        self.wave += 1
        for i in range(CREEP_COUNT):
            for j in range(WAVES[self.wave][i]):
                c = self.creep_types[i]((0, 0))
                x, y = self.world.get_start()
                c.set_position((-(j+1)*(c.get_width() + CREEP_GAP), y))
                c.set_destination(self.world.next_waypoint(0))
                self.creeps.add(c)
        self.state = TD_PLAYING

    def calc_snap_loc(self, pos):
        if self.world.is_inside(pos):
                cell_num = self.world.get_cell_at(pos)
                snap_loc = self.world.get_cell_top_left(cell_num)
        else:
                snap_loc = pos
        return snap_loc

    def display_item(self, item):
        # clear display
        self.display.deactivate()
        # setup display
        self.display.set_image(item.get_image(), item.get_width(), item.get_height())
        self.display.add_data(item.get_info())
        self.display.activate()

    def game_logic(self, keys, newkeys, mouse_pos, newclicks):
        if self.state == TD_MENU:
            # collect actions for main menu
            actions = []
            mm_actions = self.mm.game_logic(keys, newkeys, mouse_pos, newclicks)
            for action in mm_actions:
                if action is not None:
                    actions.append(action)
            # handle actions #
            for action in actions:
                if action[0] == BUTTON_PLAY_MSG:
                    self.state = TD_LEVEL_SELECT
                elif action[0] == BUTTON_QUIT_MSG:
                    self.quit = True
                    return
        elif self.state == TD_LEVEL_SELECT:
            # collect actions for main menu
            actions = []
            mm_actions = self.mm.game_logic(keys, newkeys, mouse_pos, newclicks)
            for action in mm_actions:
                if action is not None:
                    actions.append(action)
            # collect actions for level select
            ls_actions = self.ls.game_logic(keys, newkeys, mouse_pos, newclicks)
            for action in ls_actions:
                if action is not None:
                    actions.append(action)
                    
            # handle actions #
            for action in actions:
                if action[0] == BUTTON_PLAY_MSG:
                    if len(self.ls_buttons) > 0:
                        self.load_level(self.ls_buttons[0])
                    else:
                        return
                elif action[0] == BUTTON_QUIT_MSG:
                    self.quit = True
                    return
                elif action[0] == BUTTON_LEVEL_MSG:
                    self.load_level(action[1])
        elif self.state == TD_FAILURE or self.state == TD_SUCCESS:
            self.empty_data()
        elif self.state == TD_CLEAR and not self.can_start_wave():
            print "Victory"
            self.state = TD_SUCCESS
        else:
            if self.lives <= 0:
                print "Defeat"
                self.state = TD_FAILURE
            # if we finished the wave
            # change the state
            if self.state == TD_PLAYING and len(self.creeps) == 0:
                self.waves_comp += 1
                self.state = TD_CLEAR
            
            # if we are displaying an object
            # update the display
            if self.selected is not None:
                self.display_item(self.selected)
            
            if MOUSE_LEFT in newclicks: # left mouse click
                # if we clicked on an empty cell
                # stop showing the previously
                # selected tower's range
                cell_num = self.world.get_cell_at(mouse_pos)
                if self.sub_state == TD_SHOW:
                    if self.world.has_cell(cell_num) and not self.world.is_occupied(cell_num):
                        if self.selected is not None and self.selected.get_kind() == KIND_TOWER:
                            self.selected.deactivate()
                        self.selected = None
                        self.sub_state = TD_IDLE
                        self.display.deactivate() # possible refactoring 2
            elif MOUSE_RIGHT in newclicks: # right mouse click
                if self.sub_state == TD_FOLLOW:
                    self.purchaser.deactivate()
                    self.purchaser = None
                    self.selected = None
                    self.sub_state = TD_IDLE
                    pygame.mouse.set_visible(True)
                    self.display.deactivate()
            
            for creep in self.creeps:
                if not creep.has_destination():
                    dest = self.world.next_waypoint(creep.get_visited())
                    if dest is not None:
                        creep.set_destination(self.world.next_waypoint(creep.get_visited()))
                    else:
                        dest = self.world.next_waypoint(creep.get_visited())
                    if dest is not None:
                        creep.set_destination(self.world.next_waypoint(creep.get_visited()))
                    else:
                        self.lives -= 1
                        if self.lives <= 0:
                            self.lives = 0
                        creep.health = 0
            if self.sub_state == TD_FOLLOW:
                # if we are placing a tower
                # snap its location to the
                # cells of the world
                self.purchaser.set_position(self.calc_snap_loc(mouse_pos))
            
            # collect actions for menu
            actions = []
            menu_actions = self.menu.game_logic(keys, newkeys, mouse_pos, newclicks)
            for action in menu_actions:
                if action is not None:
                    actions.append(action)

            b_menu_actions = self.b_menu.game_logic(keys, newkeys, mouse_pos, newclicks)
            for action in b_menu_actions:
                if action is not None:
                    actions.append(action)
            
            # collect actions for towers
            for tower in self.towers:
                tower_actions = tower.game_logic(keys, newkeys, mouse_pos, newclicks, self.creeps)
                for action in tower_actions:
                    if action is not None:
                        actions.append(action)

            # collect actions for creeps
            for creep in self.creeps:
                creep_actions = creep.game_logic(keys, newkeys, mouse_pos, newclicks)
                for action in creep_actions:
                    if action is not None:
                        actions.append(action)
            
            # handle actions
            for action in actions:
                if action[0] == P_FOLLOW:
                    # if we clicked on a menu item
                    # to start placing a tower
                    # keep track of that tower
                    if self.sub_state == TD_SHOW:
                        if self.selected is not None and self.selected.get_kind() == KIND_TOWER:
                            self.selected.deactivate()
                        self.display.deactivate() # possible refactoring 2
                        self.selected = None
                    self.sub_state = TD_FOLLOW
                    self.purchaser = action[1]
                    self.purchaser.activate()
                    pygame.mouse.set_visible(False)
                    self.display_item(self.purchaser)
                elif action[0] == P_PLACE:
                    if self.purchaser is None:
                        break
                    # verify ability to place tower
                    f_pos = self.calc_snap_loc(mouse_pos)
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
                                self.sub_state = TD_SHOW # show new tower
                                self.display_item(self.selected)
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
                    if self.selected is not None and self.selected.get_kind() == KIND_TOWER:
                        self.selected.deactivate()
                    self.selected = None
                    self.selected = action[1]
                    self.selected.activate()
                    self.display_item(self.selected)
                    self.sub_state = TD_SHOW # show new tower
                    self.display_item(self.selected)
                elif action[0] == C_SELECTED:
                    self.selected = action[1]
                    self.sub_state = TD_SHOW
                    self.display_item(self.selected)
                elif action[0] == C_DEAD:
                    if action[1] == self.selected:
                        self.display.deactivate()
                        self.selected = None
                        self.sub_state = TD_IDLE
                    self.creeps.remove(action[1])
                elif action[0] == B_KILL:
                    self.money += action[1]
                elif action[0] == BUTTON_NEW_WAVE_MSG:
                    self.begin_wave()
                elif action[0] == BUTTON_UPGRADE_MSG:
                    if self.sub_state == TD_SHOW:
                        if self.selected is not None:
                            if self.selected.can_be_upgraded():
                                cost = self.selected.get_upgrade_cost()
                                if self.money >= cost:
                                    self.selected.upgrade()
                                    self.money -= cost
                                    self.display_item(self.selected)
                elif action[0] == BUTTON_SELL_MSG:
                    if self.sub_state == TD_SHOW:
                        if self.selected is not None:
                            # return the money
                            self.money += self.selected.get_sell_amount()
                            # free the space
                            self.world.free_area(self.selected.get_position(), self.selected.get_dims())
                            # delete the tower
                            for i in range(len(self.towers)):
                                if self.towers[i].get_position() == self.selected.get_position():
                                    self.towers.pop(i)
                                    break
                            self.selected = None
                            # change the game mode
                            self.sub_state = TD_IDLE
                            # update display
                            self.display.deactivate()
                elif action[0] == BUTTON_QUIT_MSG:
                    self.empty_data()
            # update the tower-to-be-placed's range based
            # on whether or not it can be placed currently
            if self.purchaser is not None:
                if not self.world.can_build(self.purchaser.get_position(), self.purchaser.get_dims()):
                    self.purchaser.bad_pos()
                else:
                    self.purchaser.good_pos()
