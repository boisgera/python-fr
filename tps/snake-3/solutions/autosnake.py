#!/usr/bin/env python

# Third-Party Libraries
import pygame as pg

# Local Modules
from constants import *
from snake import state, SnakeGame

# Game
# ------------------------------------------------------------------------------
class AutoSnakeGame(SnakeGame):
    def process_events(self, events):
        if not events:
            snake = state.snake
            snake_head = snake.head
            direction = snake.direction
            fruit = state.fruit
            aim = [fruit[0] - snake_head[0], fruit[1] - snake_head[1]]
            key = None
            if aim[0] > 0 and direction != LEFT:
                key = pg.K_RIGHT
            elif aim[0] < 0 and direction != RIGHT:
                key = pg.K_LEFT
            elif aim[1] > 0 and direction != UP:
                key = pg.K_DOWN
            elif aim[1] < 0 and direction != DOWN:
                key = pg.K_UP
            if key is not None:
                event = pg.event.Event(pg.KEYDOWN, key=key)
                events.append(event)
        super().process_events(events)


if __name__ == "__main__":
    snake_game = AutoSnakeGame()
    snake_game.start()
