# Screen #
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MARGIN = 5
FRAMES_PER_SECOND = 30
WHITE = (255, 255, 255)
BACKGROUND_COLOR = WHITE

# game_logic actions #
P_IDLE = 0
P_FOLLOW = P_IDLE + 1
P_PLACE = P_FOLLOW + 1
T_SELECTED = P_PLACE + 1

# instructions #
P_SNAP_LOC = T_SELECTED + 1

# Menu #
MENU_COLOR = (100, 100, 100)
MENU_ITEM_MARGIN_X = 10

# Tower #
RANGE_COLOR = (50, 255, 50, 125)

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
STARTING_MONEY = 10000

# Wave #
WAVES = []

# Creep #
CREEP_TYPES = []
CREEP_COUNT = 0
# Default #
CREEP_DEFAULT_HEALTH = 100
CREEP_DEFAULT_SPEED = 1
CREEP_DEFAULT_IMAGE = "../assets/images/creeps/default.png"
CREEP_DEFAULT_WIDTH = 8
CREEP_DEFAULT_HEIGHT = 8

# World #
WORLD_DEFAULT_WIDTH = 576
WORLD_DEFAULT_HEIGHT = 528
WORLD1 = "../assets/worlds/world1.txt"
PATH_IMG = "../assets/images/tiles/path.png"
GRASS_IMG = "../assets/images/tiles/grass_outlined.png"
TILE_WIDTH = 16
TILE_HEIGHT = 16

# Buttons #
MOUSE_LEFT = 0
MOUSE_RIGHT = 1
MOUSE_MIDDLE = 2

# States #
TD_PAUSE = 1
TD_PLAYING = 2 # wave in progress
TD_CLEAR = 3 # in between waves

# Sub states #
TD_IDLE = TD_CLEAR + 1
TD_FOLLOW = TD_IDLE + 1
TD_SHOW = TD_FOLLOW + 1
