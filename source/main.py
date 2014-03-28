import towerdefense
from config import *

def main():
    td = towerdefense.TowerDefense("The Number One Tower Defense Game of Our, or Any, Generation", SCREEN_WIDTH, SCREEN_HEIGHT)
    td.main_loop()

main()
