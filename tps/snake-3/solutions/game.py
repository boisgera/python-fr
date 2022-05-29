# Python Standard Library
import sys

# Third-party Libraries
import pygame

# Local
from constants import *


class Game:
    def __init__(
        self, size=(WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE), fps=FPS, caption=""
    ):
        self.size = size
        self.fps = fps
        self.caption = caption

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
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

