import towerdefense
import pygame
import pygame.locals
from config import *

def main():
    # Setup the window
    screen = pygame.display.set_mode(
                # set the size
                (SCREEN_WIDTH, SCREEN_HEIGHT),

                # use double-buffering for smooth animation
                pygame.locals.DOUBLEBUF |

                # apply alpha blending
                pygame.locals.SRCALPHA)
    # set the title of the window
    pygame.display.set_caption(NAME)
    
    td = towerdefense.TowerDefense(NAME, SCREEN_WIDTH, SCREEN_HEIGHT, screen)
    td.main_loop()

main()
