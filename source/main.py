import towerdefense
from config import *

def main():
    td = towerdefense.TowerDefense("Test", SCREEN_WIDTH, SCREEN_HEIGHT)
    td.main_loop()

main()
