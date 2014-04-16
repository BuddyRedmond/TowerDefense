# Screen #
SCREEN_WIDTH = 590
SCREEN_HEIGHT = 650
MARGIN = 5
FRAMES_PER_SECOND = 30
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (200, 200, 200)

# Mouse Buttons #
MOUSE_LEFT = 1
MOUSE_RIGHT = 2
MOUSE_MIDDLE = 3

# enums #

## game_logic actions ##
P_IDLE = 0
P_FOLLOW = 1
P_PLACE = 2
T_SELECTED = 3
T_FIRE = 4

## Sub states ##
TD_IDLE = 5
TD_FOLLOW = 6
TD_SHOW = 7

## States ##
TD_PAUSE = 8
TD_PLAYING = 9 # wave in progress
TD_CLEAR = 10 # in between waves

## Menu Buttons ##
BUTTON_NEW_WAVE_MSG = 11

###########

# instructions #
P_SNAP_LOC = 11

# Menu #
MENU_COLOR = (100, 100, 100)
MENU_ITEM_MARGIN_X = 10
MENU_HEIGHT = 50

# Menu Buttons #
BUTTON_NEW_WAVE_IMG = "../assets/images/buttons/newWave.png"
BUTTON_NEW_WAVE_WIDTH = 64
BUTTON_NEW_WAVE_HEIGHT = 32

# Tower #
RANGE_COLOR = (50, 255, 50, 125)
RANGE_BAD_COLOR = (255, 50, 50, 125)

TOWER_BASIC_IMAGE = "../assets/images/towers/basic.png"
TOWER_BASIC_WIDTH = 32
TOWER_BASIC_HEIGHT = 32
TOWER_BASIC_COST = 25
TOWER_BASIC_RANGE = 75
TOWER_GREEN_IMAGE = "../assets/images/towers/green.png"
TOWER_GREEN_WIDTH = 16
TOWER_GREEN_HEIGHT = 16
TOWER_GREEN_COST = 1
TOWER_GREEN_RANGE = 50

# Money #
STARTING_MONEY = 100

# Wave #
WAVES = [[0], [10]]

# Creep #
CREEP_COUNT = 1
CREEP_DEFAULT_HEALTH = 100
CREEP_DEFAULT_SPEED = 2
CREEP_DEFAULT_IMAGE = "../assets/images/creeps/creep.png"
CREEP_DEFAULT_WIDTH = 16
CREEP_DEFAULT_HEIGHT = 16

# World #
WORLD_DEFAULT_WIDTH = 576
WORLD_DEFAULT_HEIGHT = 528
WORLD1 = "../assets/worlds/world1.txt"
PATH_IMG = "../assets/images/tiles/path.png"
GRASS_IMG = "../assets/images/tiles/grass_outlined.png"
TILE_WIDTH = 16
TILE_HEIGHT = 16
