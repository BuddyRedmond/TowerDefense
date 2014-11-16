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
import trap
import menu
import button
import display
import alert
from os import path

class TowerDefense(game.Game):
    def __init__(self, name, screen_width, screen_height, screen = None):
        # setup data members and the screen
        game.Game.__init__(self, name, screen_width, screen_height, screen)

        ### Display setup ###
        self.display = display.Display((DISPLAY_X, DISPLAY_Y), DISPLAY_WIDTH, DISPLAY_HEIGHT, DISPLAY_BG_COLOR, DISPLAY_O_COLOR)

        ### Purchaser menu setup ###
        self.menu = menu.Menu((MENU_P_X, MENU_P_Y), MENU_P_WIDTH, MENU_P_HEIGHT, MENU_P_BG_COLOR, MENU_P_O_COLOR)
            
        self.tower_types = [tower.Tower, tower.RedTower, tower.GreenTower, tower.BlueTower]

        ### Trap menu setup ###
        self.trap_menu = menu.Menu((MENU_TRAP_X, MENU_TRAP_Y), MENU_TRAP_WIDTH, MENU_TRAP_HEIGHT, MENU_TRAP_BG_COLOR, MENU_TRAP_O_COLOR)

        self.trap_types = [trap.Mud, trap.Lava]
        
        ### Button menu setup ###
        self.b_menu = menu.Menu((MENU_B_X, MENU_B_Y), MENU_B_WIDTH, MENU_B_HEIGHT, MENU_B_BG_COLOR, MENU_B_O_COLOR)
        
        self.buttons = [button.NewWave, button.Upgrade, button.Sell]
        self.creep_types = [creep.Creep, creep.RedCreep, creep.YellowCreep, creep.BlueCreep]

        ### setup font ###
        self.font = pygame.font.SysFont(FONT, FONT_SIZE)
        self.font_color = FONT_COLOR

        ### Main menu setup ###
        self.mm = menu.Menu(MM_POS, MM_WIDTH, MM_HEIGHT, MM_BG_COLOR, MM_O_COLOR)
        self.mm_buttons = [button.Play, button.Help, button.Quit]
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
        
        self.buttons = [button.NewWave, button.Upgrade, button.Sell, button.Quit]                      
        for btn in self.buttons:
            self.b_menu.add_button(btn)
        self.b_menu.center_x()

        # tracks progress through tutorial
        self.tut_progress = -1

        self.alerts = set()
        self.empty_data()

    # given a creep identifier, find the index
    # of that creep type in self.creep_types
    def get_creep_number(self, identifier):
        for i in range(len(self.creep_types)):
            if identifier == self.creep_types[i].ident:
                return i
        return 0

    # given a tower identifier, find the index
    # of that tower type in self.tower_types
    def get_tower_number(self, identifier):
        for i in range(len(self.tower_types)):
            if identifier == self.tower_types[i].ident:
                return i
        return 0

    # given a trap identifier, find the index
    # of that trap type in self.trap_types
    def get_trap_number(self, identifier):
        for i in range(len(self.trap_types)):
            if identifier == self.trap_types[i].ident:
                return i
        return 0

    # reset data members for a new game
    def load_level(self, level):
        ### World setup ###
        self.world = world.World((WORLD_X, WORLD_Y), WORLD_WIDTH, WORLD_HEIGHT, level)

        # reset data members
        self.towers = []
        self.traps = []
        self.money = STARTING_MONEY
        self.wave = 0
        self.wave_comp = 0
        self.lives = STARTING_LIVES
        self.creeps = set()
        self.state = TD_CLEAR
        self.sub_state = TD_IDLE
        self.purchaser_object = None
        self.purchaser = None
        self.selected = None
        self.selected_rect = pygame.rect.Rect((0, 0), (0, 0))
        self.selected_rect_set = False
        self.display.deactivate()
        self.alerts = set()

        # calculate the life lost alert position
        x = self.width - 2*MARGIN - ALERT_LIFE_LOST_WIDTH
        y = MARGIN
        self.alert_life_lost_pos = (x, y)

        # open and read the world file
        f = open(level, 'rb')
        fin = [line.strip() for line in f.readlines()]
        f.close()
        
        # retrieve money value
        self.money = float(fin[0])
        self.lives = int(fin[1])

        # setup towers
        self.menu.clear()
        towers = fin[2].split()
        for identifier in towers:
            tower_number = self.get_tower_number(identifier)
            self.menu.add_purchaser(self.tower_types[tower_number])
        fin = fin[3:]

        # setup traps
        self.trap_menu.clear()
        traps = fin[0].split()
        for identifier in traps:
            trap_number = self.get_trap_number(identifier)
            self.trap_menu.add_purchaser(self.trap_types[trap_number])
        fin = fin[1:]

        # setup waves
        self.waves = [None]
        # parse waves
        num_waves = int(fin[0])
        fin = fin[1:num_waves+1]
        for line in fin:
            wave = []
            for c in self.creep_types:
                wave.append(0)
            line = line.split()
            mod = float(line[0])
            line = line[1:]
            for identifier in line:
                creep_number = self.get_creep_number(identifier)
                wave[creep_number] += 1
            self.waves.append((mod, wave))

    def empty_data(self):
        # initialize empty values #
        self.world = None
        self.towers = []
        self.traps = []
        self.money = 0
        self.wave = 0
        self.waves_comp = 0
        self.lives = 0
        self.creeps = set()
        self.state = TD_MENU
        self.sub_state = TD_IDLE
        self.purchaser_object = None
        self.purchaser = None
        self.selected = None
        self.selected_rect = pygame.rect.Rect((0, 0), (0, 0))
        self.selected_rect_set = False
        self.display.deactivate()
        self.alerts = set()
        self.alert_life_lost_pos = (0, 0)
        self.waves = [None]
        self.menu.clear()

    # waves can be started while playing, another
    # wave exists, and the field is clear
    def can_start_wave(self):
        return self.state == TD_CLEAR and self.wave+1 <= len(self.waves)-1

    # setup a rectangle to be drawn around the
    # currently selected object
    def set_selected_rect(self):
        if self.selected_rect_set:
            return

        # calculate the dimensions and the
        # position of the selected rectangle
        dims = self.selected.get_dims()
        dims = (dims[0] + SELECTED_O_WIDTH*2, dims[1] + SELECTED_O_WIDTH*2)
        pos = self.selected.get_position()
        pos = (pos[0] - SELECTED_O_WIDTH, pos[1] - SELECTED_O_WIDTH)
        self.selected_rect = pygame.rect.Rect(pos, dims)

    # paints all of the objects of the game
    def paint(self, surface):
        # fill the screen with the background color
        surface.fill(BG_COLOR)

        # if the state is set to menu
        # draw the main menu
        if self.state == TD_MENU:
            surface.blit(self.mm_img, MM_IMG_POS)
            self.mm.paint(surface)

        # if the state is set to level select
        # draw the main menu and the level
        # select screen
        elif self.state == TD_LEVEL_SELECT:
            self.mm.paint(surface)
            self.ls.paint(surface)

        # if the game is being played
        # draw the world, creeps, towers,
        # and menus
        else:
            self.world.paint(surface)

            # paint the bullets, display, and menu
            for tower in self.towers:
                tower.paint_bullets(surface)
            self.menu.paint(surface)
            self.trap_menu.paint(surface)
            self.display.paint(surface)
            self.b_menu.paint(surface)

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

            # paint all of the traps
            for trap in self.traps:
                if self.selected != trap:
                    trap.paint(surface)
            
            # paint all of the creeps
            for creep in self.creeps:
                if self.selected != creep:
                    creep.paint(surface)

            # paint health bars of the creeps
            for creep in self.creeps:
                creep.paint_health(surface)

            # paint the purchaser if there is one
            if self.sub_state == TD_FOLLOW:
                if self.purchaser_object is not None:
                    self.purchaser_object.paint(surface)

            # paint all of the towers
            for tower in self.towers:
                if self.selected != tower:
                    tower.paint(surface)

            # paint the selected object and
            # the selected rectangle
            if self.selected is not None:
                self.selected.paint(surface)
                self.set_selected_rect()
                pygame.draw.rect(surface, SELECTED_O_COLOR, self.selected_rect, SELECTED_O_WIDTH)

        # paint all of the alerts
        for alert in self.alerts:
            alert.paint(surface)

    # creates and places all of the creeps
    # and changes the state
    def begin_wave(self):
        if not self.can_start_wave():
            return
        self.wave += 1

        # create and place the creeps
        x, y = self.world.get_start()
        mod = self.waves[self.wave][0]
        wave = self.waves[self.wave][1]
        for i in range(CREEP_COUNT):
            for j in range(wave[i]):
                c = self.creep_types[i]((0, 0))
                c.set_mod(mod)
                x -= c.get_width() + CREEP_GAP
                c.set_position((x, y))
                destinations = [self.world.get_start()] + self.world.get_waypoints()
                c.set_destinations(destinations)
                self.creeps.add(c)
        
        self.state = TD_PLAYING

    # returns the top-left position
    # of the tile that the given
    # position is on, if any
    def calc_snap_loc(self, pos):
        # if the position is in the world
        # find the top-left of the cell it's in
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

    # handles all of the logic of the game and
    # its pieces
    def game_logic(self, keys, newkeys, mouse_pos, newclicks):
        # collect actions for alerts
        alerts_actions = []
        for a in self.alerts:
            alert_actions = a.game_logic(keys, newkeys, mouse_pos, newclicks)
            for action in alert_actions:
                if action is not None:
                    alerts_actions.append(action)
        for action in alerts_actions:
            # if the alert expired, remove it
            if action[0] == ALERT_EXP_MESSAGE:
                self.alerts.remove(action[1])

        # only collect actions from the menu if needed
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
                elif action[0] == BUTTON_HELP_MSG:
                    self.load_level(TUTORIAL_PATH)
                    self.state = TD_TUTORIAL
                    self.tut_progress = -1
                    # create and place some creeps
                    x, y = self.world.get_waypoints()[0]
                    c = self.creep_types[0]((0, 0))
                    for j in range(5):
                        y += c.get_height() + CREEP_GAP
                        c.set_position((x, y))
                        self.creeps.add(c)
                        c = self.creep_types[0]((0, 0))
                    self.display_item(c)
                    return
                elif action[0] == BUTTON_QUIT_MSG:
                    self.quit = True
                    return

        # only collect actions from the level select
        # if needed
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
                # load the level according to which button was pressed
                if action[0] == BUTTON_PLAY_MSG:
                    if len(self.ls_buttons) > 0:
                        self.load_level(self.ls_buttons[0][0])
                    else:
                        return
                elif action[0] == BUTTON_QUIT_MSG:
                    self.state = TD_MENU
                    return
                elif action[0] == BUTTON_LEVEL_MSG:
                    self.load_level(action[1])
        elif self.state == TD_TUTORIAL:
            temp = self.tut_progress
            # first time
            if self.tut_progress == -1:
                self.tut_progress = 0
            if MOUSE_LEFT in newclicks:
                self.tut_progress += 1
            elif MOUSE_RIGHT in newclicks:
                self.tut_progress -= 1
                if self.tut_progress < 0:
                    self.tut_progress = 0
            if self.tut_progress != temp:
                self.alerts.clear()
                if self.tut_progress >= len(TUTORIAL_ALERTS):
                    self.state = TD_MENU
                    return
                a = TUTORIAL_ALERTS[self.tut_progress]
                self.alerts.add(alert.Alert(a[0], a[1], a[2], a[3]))

        # end the game upon failure or success
        elif self.state == TD_FAILURE or self.state == TD_SUCCESS:
            if MOUSE_LEFT in newclicks:
                self.empty_data()

        # report success if all waves were cleared
        elif self.state == TD_CLEAR and not self.can_start_wave():
            self.state = TD_SUCCESS
            self.alerts.add(alert.Alert(ALERT_SUCCESS_POS, ALERT_SUCCESS_WIDTH, ALERT_SUCCESS_HEIGHT, ALERT_SUCCESS_MESSAGE))

        # continue the game
        else:
            # report failure when all lives are lost
            if self.lives <= 0:
                self.state = TD_FAILURE
                self.alerts.add(alert.Alert(ALERT_FAILURE_POS, ALERT_FAILURE_WIDTH, ALERT_FAILURE_HEIGHT, ALERT_FAILURE_MESSAGE))
            # if we finished the wave
            # change the state
            if self.state == TD_PLAYING and len(self.creeps) == 0:
                self.waves_comp += 1
                message = ALERT_WAVE_CLEARED_MESSAGE %(self.waves_comp)
                self.alerts.add(alert.Alert(ALERT_WAVE_CLEARED_POS, ALERT_WAVE_CLEARED_WIDTH, ALERT_WAVE_CLEARED_HEIGHT, message, True, ALERT_WAVE_CLEARED_DURATION))
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
                        self.display.deactivate()

            # stops a tower placement
            elif MOUSE_RIGHT in newclicks:
                if self.sub_state == TD_FOLLOW:
                    self.purchaser_object.deactivate()
                    self.purchaser_object = None
                    self.selected = None
                    self.sub_state = TD_IDLE
                    pygame.mouse.set_visible(True)
                    self.display.deactivate()

            # handles life losing
            for creep in self.creeps:
                if not creep.has_destination():
                    self.lives -= 1
                    if self.lives <= 0:
                        self.lives = 0
                    creep.health = 0
                    creep.set_mod(0.0)
                    message = ALERT_LIFE_LOST_MESSAGE %(self.lives)
                    self.alerts.add(alert.Alert(self.alert_life_lost_pos, ALERT_LIFE_LOST_WIDTH, ALERT_LIFE_LOST_HEIGHT, message, True, ALERT_LIFE_LOST_DURATION))

            # if we are placing a tower
            # snap its location to the
            # cells of the world
            if self.sub_state == TD_FOLLOW:
                self.purchaser_object.set_position(self.calc_snap_loc(mouse_pos))
            
            # collect actions for tower menu
            actions = []
            # separate list for placing items
            actions_placing = []
            menu_actions = self.menu.game_logic(keys, newkeys, mouse_pos, newclicks)
            for action in menu_actions:
                if action is not None:
                    if action[0] == P_PLACE:
                        actions_placing.append(action)
                    else:
                        actions.append(action)

            # collect actions for trap menu
            trap_menu_actions = self.trap_menu.game_logic(keys, newkeys, mouse_pos, newclicks)
            for action in trap_menu_actions:
                if action is not None:
                    if action[0] == P_PLACE:
                        actions_placing.append(action)
                    else:
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

            # collect actions for traps
            for trap in self.traps:
                trap_actions = trap.game_logic(keys, newkeys, mouse_pos, newclicks, self.creeps)
                for action in trap_actions:
                    if action is not None:
                        actions.append(action)

            # when not placing a tower, the cursor is visible
            if self.sub_state != TD_FOLLOW:
                pygame.mouse.set_visible(True)
            
            # handle actions
            for action in actions_placing:
                if self.purchaser_object is None:
                        break
                placed = False
                # placing a tower
                if self.purchaser_object.kind == KIND_TOWER:
                    # verify ability to place tower
                    f_pos = self.calc_snap_loc(mouse_pos)
                    f_dims = self.purchaser_object.get_dims()
                    cell_num = self.world.get_cell_at(f_pos)
                    if self.world.has_cell(cell_num):
                        if self.purchaser_object.get_cost() <= self.money:
                            if self.world.can_build_tower(f_pos, f_dims):
                                self.world.occupy_area(f_pos, f_dims)
                                self.purchaser_object.activate()
                                self.towers.append(self.purchaser_object)
                                self.money -= self.purchaser_object.get_cost()
                                self.selected = self.purchaser_object
                                self.sub_state = TD_SHOW # show new tower
                                self.display_item(self.selected)
                                placed = True

                # placing a trap
                elif self.purchaser_object.kind == KIND_TRAP:
                    # verify ability to place tower
                    f_pos = self.calc_snap_loc(mouse_pos)
                    f_dims = self.purchaser_object.get_dims()
                    cell_num = self.world.get_cell_at(f_pos)
                    if self.world.has_cell(cell_num):
                        if self.purchaser_object.get_cost() <= self.money:
                            if self.world.can_build_trap(f_pos, f_dims):
                                self.world.occupy_area(f_pos, f_dims)
                                self.purchaser_object.activate()
                                self.traps.append(self.purchaser_object)
                                self.money -= self.purchaser_object.get_cost()
                                self.selected = self.purchaser_object
                                self.sub_state = TD_SHOW # show new trap
                                self.display_item(self.selected)
                                placed = True
                    
                if not placed:
                    self.sub_state = TD_IDLE
                    self.display.deactivate()

                # handles placing the same type of tower
                # multiple times when pressing certain
                # buttons
                dupe = False
                for btn in DUPLICATE_BUTTONS:
                    if btn in keys:
                        dupe = True
                        break
                if not dupe:
                    self.purchaser_object = None
                    pygame.mouse.set_visible(True)
                else:
                    if self.selected is not None and self.selected.get_kind() == KIND_TOWER:
                        self.selected.deactivate()

                    # creates another, identical purchaser
                    # of the last placed tower
                    self.display.deactivate()
                    self.selected = None
                    self.sub_state = TD_FOLLOW
                    self.purchaser_object = action[1][1]
                    self.purchaser_object.activate()
                    self.purchaser.toggle_status()
                    pygame.mouse.set_visible(False)
                    self.display_item(self.purchaser_object)
                
            for action in actions:
                if action[0] == P_FOLLOW:
                    # if we clicked on a menu item
                    # to start placing a tower
                    # keep track of that tower
                    if self.sub_state == TD_SHOW:
                        if self.selected is not None and self.selected.get_kind() == KIND_TOWER:
                            self.selected.deactivate()
                        self.display.deactivate()
                        self.selected = None
                    self.sub_state = TD_FOLLOW
                    self.purchaser = action[1][0]
                    self.purchaser_object = action[1][1]
                    self.purchaser_object.activate()
                    pygame.mouse.set_visible(False)
                    self.display_item(self.purchaser_object)

                # shows prices of each object in the
                # purchaser menu
                elif action[0] == P_HOVER:
                    alert_w, alert_h = ALERT_P_HOVER_WIDTH, ALERT_P_HOVER_HEIGHT
                    # grab the purchaser's position relative
                    # to the menu
                    x, y = action[1].get_position()
                    # grab the menu's position
                    if action[1].kind == KIND_TRAP:
                        mx, my = self.trap_menu.get_position()
                    else:
                        mx, my = self.menu.get_position()
                    # use the menu and purchaser positions
                    # to properly place the alert
                    w, h = action[1].get_dims()
                    x += mx - .5*ALERT_P_HOVER_WIDTH + .5*w
                    y = my - ALERT_P_HOVER_HEIGHT
                    # if the alert is off of the screen
                    # move it to the edge
                    if x < 0:
                        x = 0
                    if x+alert_w > self.width:
                        x = self.width - alert_w
                    if y < 0:
                        y = 0
                    if y+alert_h > self.height:
                        y = self.height - alert_h
                    # substitute the dollar amount of the tower
                    # into the alert's message
                    message = action[1].get_hover_message()
                    #ALERT_P_HOVER_MESSAGE %(action[1][3])
                    a = alert.Alert((x, y), alert_w, alert_h, message, True, ALERT_P_HOVER_DURATION)
                    self.alerts.add(a)

                # if we clicked on a tower stop showing the range
                # of the previously selected tower and show this
                # tower's range
                elif action[0] == T_SELECTED:
                    if self.sub_state == TD_FOLLOW:
                        self.purchaser_object = None
                    if self.selected is not None and self.selected.get_kind() == KIND_TOWER:
                        self.selected.deactivate()
                    self.selected = None
                    self.selected = action[1]
                    self.selected.activate()
                    self.display_item(self.selected)
                    self.sub_state = TD_SHOW # show new tower
                    self.display_item(self.selected)

                # if a creep was clicked, display it
                elif action[0] == C_SELECTED:
                    self.selected = action[1]
                    self.sub_state = TD_SHOW
                    self.display_item(self.selected)

                # if a creep died, remove it from the game
                elif action[0] == C_DEAD:
                    if action[1] == self.selected:
                        self.display.deactivate()
                        self.selected = None
                        self.sub_state = TD_IDLE
                    self.money += action[1].get_value()
                    self.creeps.remove(action[1])

                # start a new wave when the new wave button is clicked
                elif action[0] == BUTTON_NEW_WAVE_MSG:
                    self.begin_wave()

                # upgrade the selected tower, if any, when
                # the upgrade button is clicked
                elif action[0] == BUTTON_UPGRADE_MSG:
                    if self.sub_state == TD_SHOW:
                        if self.selected is not None and self.selected.kind == KIND_TOWER:
                            if self.selected.can_be_upgraded():
                                cost = self.selected.get_upgrade_cost()
                                if self.money >= cost:
                                    self.selected.upgrade()
                                    self.money -= cost
                                    self.display_item(self.selected)

                # sell the selected tower, if any, when
                # the sell button is clicked
                elif action[0] == BUTTON_SELL_MSG:
                    if self.sub_state == TD_SHOW:
                        if self.selected is not None and self.selected.kind != KIND_CREEP:
                            # return the money
                            self.money += self.selected.get_sell_amount()
                            # free the space
                            self.world.free_area(self.selected.get_position(), self.selected.get_dims())
                            if self.selected.kind == KIND_TOWER:
                                # delete the tower
                                for i in range(len(self.towers)):
                                    if self.towers[i].get_position() == self.selected.get_position():
                                        self.towers.pop(i)
                                        break

                            elif self.selected.kind == KIND_TRAP:
                                # delete the trap
                                for i in range(len(self.traps)):
                                    if self.traps[i].get_position() == self.selected.get_position():
                                        self.traps.pop(i)
                                        break
                            self.selected = None
                            # change the game mode
                            self.sub_state = TD_IDLE
                            # update display
                            self.display.deactivate()

                # reset the data when the quit button
                # is clicked
                elif action[0] == BUTTON_QUIT_MSG:
                    self.empty_data()
                    
            # update the tower-to-be-placed's range based
            # on whether or not it can be placed currently
            if self.purchaser_object is not None:
                if self.purchaser_object.kind == KIND_TOWER:
                    if not self.world.can_build_tower(self.purchaser_object.get_position(), self.purchaser_object.get_dims()):
                        self.purchaser_object.bad_pos()
                    else:
                        self.purchaser_object.good_pos()
                elif self.purchaser_object.kind == KIND_TRAP:
                    if not self.world.can_build_trap(self.purchaser_object.get_position(), self.purchaser_object.get_dims()):
                        self.purchaser_object.bad_pos()
                    else:
                        self.purchaser_object.good_pos()
