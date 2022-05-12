#!/usr/bin/env python

# Third-Party Libraries
import pygame as pg

# Local Modules
from constants import *
from snake import state, SnakeGame

# ------------------------------------------------------------------------------

class AutoSnakeGame(SnakeGame):
    def process_events(self, events):
        if not events:
            snake = state.snake
            snake_head = snake.head
            direction = snake.direction
            fruit = state.fruit
            aim = (fruit[0] - snake_head[0], fruit[1] - snake_head[1])
            key = None
            if aim[0] > 0 and direction != DIRECTIONS["LEFT"]:
                key = pg.K_RIGHT
            elif aim[0] < 0 and direction != DIRECTIONS["RIGHT"]:
                key = pg.K_LEFT
            elif aim[1] > 0 and direction != DIRECTIONS["UP"]:
                key = pg.K_DOWN
            elif aim[1] < 0 and direction != DIRECTIONS["DOWN"]:
                key = pg.K_UP
            if key is not None:
                event = pg.event.Event(pg.KEYDOWN, key=key)
                events.append(event)
        super().process_events(events)

if __name__ == "__main__":
    snake_game = AutoSnakeGame(size=(X * W, Y * H), fps=FPS)
    snake_game.start()
