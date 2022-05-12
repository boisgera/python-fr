# Python Standard Library
import sys

# Third-party Libraries
import pygame as pg


class Game:
    def __init__(self, size=(640, 480), fps=1, caption=""):
        pg.init()
        self.screen = pg.display.set_mode(size)
        self.clock = pg.time.Clock()
        self.fps = fps
        self.caption = caption

    def start(self):
        while True:
            self.clock.tick(self.fps)
            events = pg.event.get()
            self.process_events(events)

            self.draw()
            pg.display.set_caption(self.caption)
            pg.display.update()

    def process_events(self, events):
        raise NotImplementedError()

    def draw(self):
        raise NotImplementedError()

    def quit(self, error=None):
        pg.quit()
        sys.exit(error)
