# Screen #
NAME = "Tower Defense Game"
SCREEN_WIDTH = 590
SCREEN_HEIGHT = 695
MARGIN = 5
FRAMES_PER_SECOND = 30
WHITE = (255, 255, 255)
BG_COLOR = (221, 198, 89)#(200, 200, 200)
O_COLOR = (27, 143, 30)#(100, 100, 100)
FONT = "helvetica"
FONT_SIZE = 14
FONT_COLOR = (27, 143, 30)#(0, 200, 0)
SELECTED_O_COLOR = (225, 225, 55)
SELECTED_O_WIDTH = 2
WORLD_PATH = "../assets/worlds/"
SPLASH_PATH = "../assets/images/splash/"
BUTTON_PATH = "../assets/images/buttons/"
TOWER_PATH = "../assets/images/towers/"
BULLET_PATH = "../assets/images/bullets/"
CREEP_PATH = "../assets/images/creeps/"
TILE_PATH = "../assets/images/tiles/"
TRAP_PATH = "../assets/images/traps/"

# Alert #
ALERT_O_COLOR = O_COLOR
ALERT_BG_COLOR = BG_COLOR
ALERT_MARGIN_X = 5
ALERT_MARGIN_Y = 5
ALERT_OUTLINE_WIDTH = 3
ALERT_FONT = FONT
ALERT_FONT_SIZE = FONT_SIZE
ALERT_FONT_COLOR = FONT_COLOR
### wave cleared ###
ALERT_WAVE_CLEARED_WIDTH = 400
ALERT_WAVE_CLEARED_HEIGHT = 25
ALERT_WAVE_CLEARED_POS = ((SCREEN_WIDTH - ALERT_WAVE_CLEARED_WIDTH)/2.0, (SCREEN_HEIGHT - ALERT_WAVE_CLEARED_HEIGHT)/3.0)
ALERT_WAVE_CLEARED_MESSAGE = "WAVE %d CLEARED!"
ALERT_WAVE_CLEARED_DURATION = 2
### purchaser hover ###
ALERT_P_HOVER_WIDTH = 140
ALERT_P_HOVER_HEIGHT = 115
ALERT_P_HOVER_MESSAGE = "$%.2f"
ALERT_P_HOVER_DURATION = .01
### life lost ###
ALERT_LIFE_LOST_WIDTH = 175
ALERT_LIFE_LOST_HEIGHT = 25
ALERT_LIFE_LOST_MESSAGE = "Life lost! %d remaining."
ALERT_LIFE_LOST_DURATION = 1
### failure ###
ALERT_FAILURE_WIDTH = 400
ALERT_FAILURE_HEIGHT = 50
ALERT_FAILURE_POS = ((SCREEN_WIDTH - ALERT_FAILURE_WIDTH)/2.0, (SCREEN_HEIGHT - ALERT_FAILURE_HEIGHT)/3.0)
ALERT_FAILURE_MESSAGE = "Failure! You have failed to complete all of the waves on this level. Click anywhere to return to the main menu."
### success ###
ALERT_SUCCESS_WIDTH = 400
ALERT_SUCCESS_HEIGHT = 50
ALERT_SUCCESS_POS = ((SCREEN_WIDTH - ALERT_SUCCESS_WIDTH)/2.0, (SCREEN_HEIGHT - ALERT_SUCCESS_HEIGHT)/3.0)
ALERT_SUCCESS_MESSAGE = "Congratulations! You have completed this level! Click anywhere to return to main menu."

# Menu #
MENU_O_COLOR = O_COLOR
MENU_BG_COLOR = BG_COLOR
MENU_P_X = 7
MENU_P_Y = 538
MENU_P_WIDTH = (351 - MARGIN) / 2.0
MENU_P_HEIGHT = 50
MENU_TRAP_O_COLOR = O_COLOR
MENU_TRAP_BG_COLOR = BG_COLOR
MENU_TRAP_X = 184
MENU_TRAP_Y = 538
MENU_TRAP_WIDTH = (348 - MARGIN) / 2.0
MENU_TRAP_HEIGHT = 50
MENU_B_X = 7
MENU_B_Y = 593
MENU_B_WIDTH = 348
MENU_B_HEIGHT = 77
MENU_P_O_COLOR = O_COLOR
MENU_P_BG_COLOR = BG_COLOR
MENU_B_O_COLOR = O_COLOR
MENU_B_BG_COLOR = BG_COLOR
MENU_ITEM_MARGIN_X = 10
MENU_ITEM_MARGIN_Y = 10
MENU_OUTLINE_WIDTH = 3
### Main menu ###
MM_WIDTH = SCREEN_WIDTH - 2*MARGIN
MM_HEIGHT = 75
MM_POS = (MARGIN, SCREEN_HEIGHT-MM_HEIGHT)
MM_BG_COLOR = (221, 198, 89)
MM_O_COLOR = (27, 143, 30)
MM_IMG = SPLASH_PATH + "logo.png"
MM_IMG_POS = (0, 0)
### Level select ###
LS_IMG = SPLASH_PATH + "level_select.png"
LS_IMG_WIDTH = 580
LS_IMG_HEIGHT = 110
LS_WIDTH = SCREEN_WIDTH - 2*MARGIN
LS_HEIGHT = SCREEN_HEIGHT - MARGIN - MM_HEIGHT
LS_POS = (MARGIN, MARGIN)
LS_BG_COLOR = (221, 198, 89)
LS_O_COLOR = (27, 143, 30)

# Display #
DISPLAY_FONT = "helvetica"
DISPLAY_FONT_SIZE = 12
DISPLAY_FONT_COLOR = (27, 143, 30)
DISPLAY_X = 360
DISPLAY_Y = 538
DISPLAY_O_COLOR = O_COLOR
DISPLAY_BG_COLOR = BG_COLOR
DISPLAY_HEIGHT = 132
DISPLAY_WIDTH = 223
DISPLAY_MARGIN_LEFT = 5
DISPLAY_MARGIN_TOP = 5
DISPLAY_NO_IMG_HEIGHT = 32
DISPLAY_NO_IMG_WIDTH = 32

# Button menu #
MENU_BUTTON_HEIGHT = 77

# Menu Buttons #
BUTTON_NEW_WAVE_IMG = BUTTON_PATH + "nextWave.png"
BUTTON_NEW_WAVE_HOVER_IMG = BUTTON_PATH + "nextWave_hover.png"
BUTTON_NEW_WAVE_WIDTH = 75
BUTTON_NEW_WAVE_HEIGHT = 45
BUTTON_UPGRADE_IMG = BUTTON_PATH + "upgrade.png"
BUTTON_UPGRADE_HOVER_IMG = BUTTON_PATH + "upgrade_hover.png"
BUTTON_UPGRADE_WIDTH = 75
BUTTON_UPGRADE_HEIGHT = 45
BUTTON_SELL_IMG = BUTTON_PATH + "sell.png"
BUTTON_SELL_HOVER_IMG = BUTTON_PATH + "sell_hover.png"
BUTTON_SELL_WIDTH = 75
BUTTON_SELL_HEIGHT = 45
BUTTON_PLAY_IMG = BUTTON_PATH + "play.png"
BUTTON_PLAY_HOVER_IMG = BUTTON_PATH + "play_hover.png"
BUTTON_PLAY_WIDTH = 75
BUTTON_PLAY_HEIGHT = 45
BUTTON_QUIT_IMG = BUTTON_PATH + "quit.png"
BUTTON_QUIT_HOVER_IMG = BUTTON_PATH + "quit_hover.png"
BUTTON_QUIT_WIDTH = 75
BUTTON_QUIT_HEIGHT = 45
BUTTON_HELP_IMG = BUTTON_PATH + "help.png"
BUTTON_HELP_HOVER_IMG = BUTTON_PATH + "help_hover.png"
BUTTON_HELP_WIDTH = 75
BUTTON_HELP_HEIGHT = 45
BUTTON_LEVEL_IMG = BUTTON_PATH + "level.png"
BUTTON_LEVEL_HOVER_IMG = BUTTON_PATH + "level_hover.png"
BUTTON_LEVEL_WIDTH = 75
BUTTON_LEVEL_HEIGHT = 45

# Hardware Buttons #
DUPLICATE_BUTTONS = [303, 304] # left and right shift buttons
MOUSE_LEFT = 1
MOUSE_MIDDLE = 2
MOUSE_RIGHT = 3

# enums #

## game_logic actions ##
P_IDLE = 4
P_FOLLOW = 5
P_PLACE = 6
P_HOVER = 7
T_SELECTED = 8
T_FIRE = 9
B_DONE = 10
B_KILL = 11
C_DEAD = 12
C_SELECTED = 13

## Sub states ##
TD_IDLE = 14
TD_FOLLOW = 15
TD_SHOW = 16

## States ##
TD_MENU = 17
TD_LEVEL_SELECT = 18
TD_TUTORIAL = 19
TD_PAUSE = 20
TD_PLAYING = 21 # wave in progress
TD_CLEAR = 22 # in between waves
TD_FAILURE = 23
TD_SUCCESS = 24

## Menu Buttons ##
BUTTON_NEW_WAVE_MSG = 25
BUTTON_UPGRADE_MSG = 26
BUTTON_SELL_MSG = 27
BUTTON_PLAY_MSG = 28
BUTTON_QUIT_MSG = 29
BUTTON_HELP_MSG = 30
BUTTON_LEVEL_MSG = 31

# instructions #
P_SNAP_LOC = 32

# kinds #
KIND_TOWER = 33
KIND_CREEP = 34
KIND_TILE = 35
KIND_BUTTON = 36
KIND_BULLET = 37
KIND_TRAP = 38

# alert #
ALERT_EXP_MESSAGE = 39

################

# Healthbar #
HEALTH_BAR_WIDTH = 20
HEALTH_BAR_HEIGHT = 5
HEALTH_BAR_BG_COLOR = (225, 0, 0)
HEALTH_BAR_COLOR = (0, 225, 0)
HEALTH_BAR_MARGIN = 3

# Tower #
RANGE_COLOR = (50, 255, 50, 125)
RANGE_BAD_COLOR = (255, 50, 50, 125)
TOWER_SELL_RATE = .85

TOWER_RED_IMAGE = TOWER_PATH + "basic.png"
TOWER_RED_NAME = "Red Tower"
TOWER_RED_WIDTH = 32
TOWER_RED_HEIGHT = 32
TOWER_RED_COST = [50, 150, 300, 500]
TOWER_RED_RANGE = [70, 80, 90, 100]
TOWER_RED_ATK_SPEED = [2, 2.5, 2.75, 3]
TOWER_RED_DAMAGE = [25, 50, 100, 175]

TOWER_DEFAULT_IMAGE = TOWER_RED_IMAGE
TOWER_DEFAULT_NAME = TOWER_RED_NAME
TOWER_DEFAULT_WIDTH = TOWER_RED_WIDTH
TOWER_DEFAULT_HEIGHT = TOWER_RED_HEIGHT
TOWER_DEFAULT_COST = TOWER_RED_COST
TOWER_DEFAULT_RANGE = TOWER_RED_RANGE
TOWER_DEFAULT_ATK_SPEED = TOWER_RED_ATK_SPEED
TOWER_DEFAULT_DAMAGE = TOWER_RED_DAMAGE

TOWER_GREEN_IMAGE = TOWER_PATH + "green.png"
TOWER_GREEN_NAME = "Green Tower"
TOWER_GREEN_WIDTH = 16
TOWER_GREEN_HEIGHT = 16
TOWER_GREEN_COST = [25, 100, 250, 400]
TOWER_GREEN_RANGE = [50, 60, 70, 80]
TOWER_GREEN_ATK_SPEED = [7, 7.5, 8, 8.5]
TOWER_GREEN_DAMAGE = [8, 16, 32, 64]

TOWER_BLUE_IMAGE = TOWER_PATH + "blue.png"
TOWER_BLUE_NAME = "Blue Tower"
TOWER_BLUE_WIDTH = 32
TOWER_BLUE_HEIGHT = 32
TOWER_BLUE_COST = [100, 200, 500, 1000]
TOWER_BLUE_RANGE = [75, 100, 125, 150]
TOWER_BLUE_ATK_SPEED = [1, 1, 2, 2]
TOWER_BLUE_DAMAGE = [75, 150, 500, 1000]

# Bullet #
BULLET_RED_IMAGE = BULLET_PATH + "red.png"
BULLET_RED_WIDTH = 8
BULLET_RED_HEIGHT = 8
BULLET_RED_SPEED = 300
BULLET_DEFAULT_IMAGE = BULLET_RED_IMAGE
BULLET_DEFAULT_WIDTH = BULLET_RED_WIDTH
BULLET_DEFAULT_HEIGHT = BULLET_RED_HEIGHT
BULLET_DEFAULT_SPEED = BULLET_RED_SPEED
BULLET_GREEN_IMAGE = BULLET_PATH + "green.png"
BULLET_GREEN_WIDTH = 4
BULLET_GREEN_HEIGHT = 4
BULLET_GREEN_SPEED = 300

# Money #
STARTING_MONEY = 1000
MONEY_X = MARGIN
MONEY_Y = 675

# Lives #
STARTING_LIVES = 10
LIVES_X = MARGIN + 217
LIVES_Y = 675

# Wave #
WAVE_X = MARGIN*2 + 434
WAVE_Y = 675

# Creep #
CREEP_GAP = 15
CREEP_COUNT = 4

CREEP_RED_HEALTH = 100
CREEP_RED_NAME = "Red Creep"
CREEP_RED_SPEED = 75
CREEP_RED_IMAGE = CREEP_PATH + "creep.png"
CREEP_RED_WIDTH = 16
CREEP_RED_HEIGHT = 16
CREEP_RED_VALUE = 10

CREEP_DEFAULT_HEALTH = CREEP_RED_HEALTH
CREEP_DEFAULT_NAME = CREEP_RED_NAME
CREEP_DEFAULT_SPEED = CREEP_RED_SPEED
CREEP_DEFAULT_IMAGE = CREEP_RED_IMAGE
CREEP_DEFAULT_WIDTH = CREEP_RED_WIDTH
CREEP_DEFAULT_HEIGHT = CREEP_RED_HEIGHT
CREEP_DEFAULT_VALUE = CREEP_RED_VALUE

CREEP_YELLOW_HEALTH = 500
CREEP_YELLOW_NAME = "Yellow Creep"
CREEP_YELLOW_SPEED = 50
CREEP_YELLOW_IMAGE = CREEP_PATH + "yellow.png"
CREEP_YELLOW_WIDTH = 16
CREEP_YELLOW_HEIGHT = 16
CREEP_YELLOW_VALUE = 50

CREEP_BLUE_HEALTH = 1500
CREEP_BLUE_NAME = "Blue Creep"
CREEP_BLUE_SPEED = 65
CREEP_BLUE_IMAGE = CREEP_PATH + "blue.png"
CREEP_BLUE_WIDTH = 16
CREEP_BLUE_HEIGHT = 16
CREEP_BLUE_VALUE = 200

# Trap #
TRAP_SELL_RATE = .9

TRAP_MUD_NAME = "Mud Trap"
TRAP_MUD_IMAGE = TRAP_PATH + "mud.png"
TRAP_MUD_BAD_IMAGE = TRAP_PATH + "bad_mud.png"
TRAP_MUD_WIDTH = 16
TRAP_MUD_HEIGHT = 16
TRAP_MUD_SPEED_MOD = .5
TRAP_MUD_COST = 100.0
TRAP_MUD_DETAILS = ["Slows creeps as they pass through the mud"]

TRAP_DEFAULT_NAME = TRAP_MUD_NAME
TRAP_DEFAULT_IMAGE = TRAP_MUD_IMAGE
TRAP_DEFAULT_BAD_IMAGE = TRAP_MUD_BAD_IMAGE
TRAP_DEFAULT_WIDTH = TRAP_MUD_WIDTH
TRAP_DEFAULT_HEIGHT = TRAP_MUD_HEIGHT
TRAP_DEFAULT_COST = TRAP_MUD_COST

TRAP_LAVA_NAME = "Lava Trap"
TRAP_LAVA_IMAGE = TRAP_PATH + "lava.png"
TRAP_LAVA_BAD_IMAGE = TRAP_PATH + "bad_lava.png"
TRAP_LAVA_WIDTH = 16
TRAP_LAVA_HEIGHT = 16
TRAP_LAVA_DAMAGE = 100
TRAP_LAVA_PERCENT = .03
TRAP_LAVA_DURATION = 3
TRAP_LAVA_COST = 75.0
TRAP_LAVA_DETAILS = ["Damages creeps that pass over the lava over time"]

# Tutorial #
TUTORIAL_PATH = WORLD_PATH + "tutorial.txt"
### Welcome ###
TWELCOME_WIDTH = 400
TWELCOME_HEIGHT = 70
TWELCOME_POS = ((SCREEN_WIDTH - TWELCOME_WIDTH)/2.0, (SCREEN_HEIGHT - TWELCOME_HEIGHT)/3.0)
TWELCOME_MESSAGE = "Welcome to the Tower Defense tutorial\n\
                    Left-click to move to the next message\n\
                    Right-click to move the the previous message"
### Objective ###
TOBJECTIVE_WIDTH = 400
TOBJECTIVE_HEIGHT = 70
TOBJECTIVE_POS = ((SCREEN_WIDTH - TOBJECTIVE_WIDTH)/2.0, (SCREEN_HEIGHT - TOBJECTIVE_HEIGHT)/3.0)
TOBJECTIVE_MESSAGE = "The objective of the game is to place towers and traps\
                            strategically to prevent the creeps from making it\
                            through the level."
### Controls ###
TCONTROLS_WIDTH = 400
TCONTROLS_HEIGHT = 150
TCONTROLS_POS = ((SCREEN_WIDTH - TCONTROLS_WIDTH)/2.0, (SCREEN_HEIGHT - TCONTROLS_HEIGHT)/3.0)
TCONTROLS_MESSAGE = "Here are the controls for the game:\n\
                        Left-click - Select an object, build a tower/trap,\
                        or press a button\n\
                        Right-click - Deselect an object\n\
                        Shift-Left-click - When building a tower/trap and holding the shift key, builds the object and goes back to building mode for fast placing"
### Tiles ###
TTILES_WIDTH = 400
TTILES_HEIGHT = 70
TTILES_POS = ((SCREEN_WIDTH - TTILES_WIDTH)/2.0, (SCREEN_HEIGHT - TTILES_HEIGHT)/3.0)
TTILES_MESSAGE = "The world is made up of tiles: Grass, Rocks, and Path\n\
                    Grass tiles are green, Rocks are green with gray specs,\
                    and Path tiles are tan"
### Money ###
TMONEY_WIDTH = 400
TMONEY_HEIGHT = 70
TMONEY_POS = (MONEY_X, MONEY_Y - TMONEY_HEIGHT - MARGIN)
TMONEY_MESSAGE = "Money is displayed here in the bottom left corner\n\
                    Money is earned by killing creeps and is used to purchase\
                    towers, traps, and upgrades"
### Lives ###
TLIVES_WIDTH = 400
TLIVES_HEIGHT = 70
TLIVES_POS = ((SCREEN_WIDTH - TLIVES_WIDTH)/2.0, LIVES_Y - TLIVES_HEIGHT - MARGIN)
TLIVES_MESSAGE = "Lives are displayed here on the bottom of the screen\n\
                    Lives are lost when a creep makes it through the level\
                    When all lives are lost, you lose the game"
### Wave ###
TWAVE_WIDTH = 400
TWAVE_HEIGHT = 50
TWAVE_POS = (SCREEN_WIDTH - MARGIN - TWAVE_WIDTH, WAVE_Y - TWAVE_HEIGHT - MARGIN)
TWAVE_MESSAGE = "The number of complete waves is displayed here in the \
                    bottom right corner"
### Towers ###
TTOWERS1_WIDTH = 200
TTOWERS1_HEIGHT = 25
TTOWERS1_POS = (MENU_P_X, MENU_P_Y - TTOWERS1_HEIGHT - MARGIN)
TTOWERS1_MESSAGE = "This is the tower menu (left)"
TTOWERS2_WIDTH = 300
TTOWERS2_HEIGHT = 70
TTOWERS2_POS = (MENU_P_X, MENU_P_Y - TTOWERS2_HEIGHT - MARGIN)
TTOWERS2_MESSAGE = "Hovering over a tower will display its stats\
                    Left click a tower to select it. The tower\
                    will then be moved by the mouse"
TTOWERS3_WIDTH = 300
TTOWERS3_HEIGHT = 90
TTOWERS3_POS = (MENU_P_X, MENU_P_Y - TTOWERS3_HEIGHT - MARGIN)
TTOWERS3_MESSAGE = "When a tower is selected you can deselect\
                        it by right clicking or you can buy\
                        and place the tower by left clicking\
                        on a buildable area (grass)"
### Traps ###
TTRAPS_WIDTH = 300
TTRAPS_HEIGHT = 90
TTRAPS_POS = (MENU_TRAP_X, MENU_TRAP_Y - TTRAPS_HEIGHT - MARGIN)
TTRAPS_MESSAGE = "This is the trap menu. Traps behave\
                    similarly to towers with two differences\
                    Traps are placed on path tiles and they\
                    affect creeps that walk over them."
### Display ###
TDISPLAY_WIDTH = 300
TDISPLAY_HEIGHT = 50
TDISPLAY_POS = (SCREEN_WIDTH - TDISPLAY_WIDTH - MARGIN, DISPLAY_Y - TDISPLAY_HEIGHT - MARGIN)
TDISPLAY_MESSAGE = "This is the display area. When a trap, creep, or tower is clicked it shows its stats"
### Buttons ###
TBUTTONS_WIDTH = 400
TBUTTONS_HEIGHT = 110
TBUTTONS_POS = (MENU_B_X, MENU_B_Y - TBUTTONS_HEIGHT - MARGIN)
TBUTTONS_MESSAGE = "These buttons help you interact with the game.\n\
                        The first button begins a wave.\n\
                        The second upgrades a selected tower.\n\
                        The third sells a selected tower or trap.\n\
                        And the fourth returns to the main menu."
### Creeps ###
TCREEPS_WIDTH = 400
TCREEPS_HEIGHT = 110
TCREEPS_POS = (110, 90)
TCREEPS_MESSAGE = "These red things are creeps.\n Creeps come in different\
                    sizes, shapes, colors, speeds, and strengths.\n\
                    Creeps walk the path until they reach the end.\n\
                    If they reach the end, you lose a life."
### Done ###
TDONE_WIDTH = 400
TDONE_HEIGHT = 50
TDONE_POS = ((SCREEN_WIDTH - TDONE_WIDTH)/2.0, (SCREEN_HEIGHT - TDONE_HEIGHT)/3.0)
TDONE_MESSAGE = "This is the end of the tutorial, click to go back\
                    to the main menu and start playing"
TUTORIAL_ALERTS = [(TWELCOME_POS, TWELCOME_WIDTH, TWELCOME_HEIGHT, TWELCOME_MESSAGE),
                   (TOBJECTIVE_POS, TOBJECTIVE_WIDTH, TOBJECTIVE_HEIGHT, TOBJECTIVE_MESSAGE),
                   (TCONTROLS_POS, TCONTROLS_WIDTH, TCONTROLS_HEIGHT, TCONTROLS_MESSAGE),
                   (TTILES_POS, TTILES_WIDTH, TTILES_HEIGHT, TTILES_MESSAGE),
                   (TMONEY_POS, TMONEY_WIDTH, TMONEY_HEIGHT, TMONEY_MESSAGE),
                   (TLIVES_POS, TLIVES_WIDTH, TLIVES_HEIGHT, TLIVES_MESSAGE),
                   (TWAVE_POS, TWAVE_WIDTH, TWAVE_HEIGHT, TWAVE_MESSAGE),
                   (TTOWERS1_POS, TTOWERS1_WIDTH, TTOWERS1_HEIGHT, TTOWERS1_MESSAGE),
                   (TTOWERS2_POS, TTOWERS2_WIDTH, TTOWERS2_HEIGHT, TTOWERS2_MESSAGE),
                   (TTOWERS3_POS, TTOWERS3_WIDTH, TTOWERS3_HEIGHT, TTOWERS3_MESSAGE),
                   (TTRAPS_POS, TTRAPS_WIDTH, TTRAPS_HEIGHT, TTRAPS_MESSAGE),
                   (TDISPLAY_POS, TDISPLAY_WIDTH, TDISPLAY_HEIGHT, TDISPLAY_MESSAGE),
                   (TBUTTONS_POS, TBUTTONS_WIDTH, TBUTTONS_HEIGHT, TBUTTONS_MESSAGE),
                   (TCREEPS_POS, TCREEPS_WIDTH, TCREEPS_HEIGHT, TCREEPS_MESSAGE),
                   (TDONE_POS, TDONE_WIDTH, TDONE_HEIGHT, TDONE_MESSAGE)]

# World #
WORLD_X = 7
WORLD_Y = 5
WORLD_WIDTH = 576
WORLD_HEIGHT = 528
GRASS = 0
ROCK = 1
PATH = 2
WAYPOINT = 3
WORLD1_PATH = WORLD_PATH + "world1.txt"
WORLD1_NAME = "Level 1"
WORLD2_PATH = WORLD_PATH + "world2.txt"
WORLD2_NAME = "Level 2"
PATH_IMG = TILE_PATH + "path.png"
GRASS_IMG = TILE_PATH + "grass_outlined.png"
ROCK_IMG = TILE_PATH + "rock_on_grass.png"
TILE_WIDTH = 16
TILE_HEIGHT = 16
WORLD_DEFAULT_WIDTH = 576
WORLD_DEFAULT_HEIGHT = 528

LEVELS = [(WORLD1_PATH, WORLD1_NAME), (WORLD2_PATH, WORLD2_NAME)]
