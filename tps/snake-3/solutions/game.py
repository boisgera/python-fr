# Python Standard Library
import sys

# Third-party Libraries
import pygame

# Local
from constants import *


class Game:
    def __init__(self, size=(WIDTH*CELL_SIZE, HEIGHT*CELL_SIZE), fps=FPS, caption=""):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.caption = caption

    def start(self):
        while True:
            events = pygame.event.get()
            self.process_events(events)
            self.draw()
            pygame.display.update()
            pygame.display.set_caption(self.caption)

            self.clock.tick(self.fps)

    def process_events(self, events):
        raise NotImplementedError()

    def draw(self):
        raise NotImplementedError()

    def quit(self, error=None):
        pygame.quit()
        sys.exit(error)
