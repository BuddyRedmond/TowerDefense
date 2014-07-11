import pygame
import pygame.locals

import config

class Game:
    def __init__(self, name, width, height, screen = None):
        self.width = width
        self.height = height
        self.on = True
        self.quit = False
        self.name = name
        if screen is None:
            self.new_screen(width, height)
        else:
            self.screen = screen
        pygame.font.init()

    def new_screen(self, width, height):
        self.screen = pygame.display.set_mode(
                # set the size
                (width, height),

                # use double-buffering for smooth animation
                pygame.locals.DOUBLEBUF |

                # apply alpha blending
                pygame.locals.SRCALPHA |

                # allow the window to be resizable
                pygame.locals.RESIZABLE)
        # set the title of the window
        pygame.display.set_caption(self.name)

    def game_logic(self, keys, newkeys):
        raise NotImplementedError()

    def paint(self, surface):
        raise NotImplementedError()

    def main_loop(self):
        clock = pygame.time.Clock()
        keys = set()
        mouse_pos = (0, 0)
        while True:
            clock.tick(config.FRAMES_PER_SECOND)

            newkeys = set()
            newclicks = set()
            for e in pygame.event.get():
                # did the user try to close the window?
                if e.type == pygame.QUIT:
                    pygame.quit()
                    return

                # did the user just press the escape key?
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

                # track which keys are currently set
                if e.type == pygame.KEYDOWN:
                    keys.add(e.key)
                    newkeys.add(e.key)
                if e.type == pygame.KEYUP:
                    keys.discard(e.key)

                # track which mouse buttons were pressed
                if e.type == pygame.MOUSEBUTTONUP:
                    newclicks.add(e.button)

                # track the mouse's position
                if e.type == pygame.MOUSEMOTION:
                    mouse_pos = e.pos

                # update window size if resized
                if e.type == pygame.VIDEORESIZE:
                    self.new_screen(e.w, e.h)
                    self.screen.fill(config.BG_COLOR)

            if self.on:
                self.game_logic(keys, newkeys, mouse_pos, newclicks)
                if self.quit == True:
                    pygame.quit()
                    return
                self.paint(self.screen)

            pygame.display.flip()

