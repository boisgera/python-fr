# Python Standard Library
import copy
import random

# Third-Party Libraries
import pygame as pg

# Local Modules
from game import Game
from constants import *

# Game state
# ------------------------------------------------------------------------------
def check_direction(direction):
    """
    Check that direction in {(-1, 0), (1, 0), (0, -1), (0, 1)}

    Usage:

    >>> check_direction((1, 0))
    >>> check_direction((-1, 0))
    >>> check_direction((0, 1))
    >>> check_direction((0, -1))

    >>> check_direction((0, 0))
    Traceback (most recent call last):
    ...
    ValueError: (0, 0) is not in [(0, 1), (0, -1), (1, 0), (-1, 0)]
    >>> check_direction((1, 1))
    Traceback (most recent call last):
    ...
    ValueError: (1, 1) is not in [(0, 1), (0, -1), (1, 0), (-1, 0)]
    >>> check_direction((7, 12))
    Traceback (most recent call last):
    ...
    ValueError: (7, 12) is not in [(0, 1), (0, -1), (1, 0), (-1, 0)]

    >>> check_direction([0, 1])
    Traceback (most recent call last):
    ...
    TypeError: [0, 1] is not a pair of integers
    >>> check_direction((0, 1, 2))
    Traceback (most recent call last):
    ...
    TypeError: (0, 1, 2) is not a pair of integers
    >>> check_direction(True)
    Traceback (most recent call last):
    ...
    TypeError: True is not a pair of integers
    >>> check_direction((1.0, 2.0))
    Traceback (most recent call last):
    ...
    TypeError: (1.0, 2.0) is not a pair of integers
    """
    if (
        not isinstance(direction, tuple)
        or len(direction) != 2
        or not isinstance(direction[0], int)
        or not isinstance(direction[1], int)
    ):
        raise TypeError(f"{direction} is not a pair of integers")
    elif direction not in DIRECTIONS.values():
        raise ValueError(f"{direction} is not in {list(DIRECTIONS.values())}")


def is_in_scope(tile):
    x, y = tile
    return 0 <= x < X and 0 <= y < Y


def check_geometry(geometry):
    if not all(
        isinstance(item, tuple)
        and len(item) == 2
        and isinstance(item[0], int)
        and isinstance(item[1], int)
        for item in geometry
    ):
        raise TypeError("all geometry items should be pairs of integers")
    if not geometry:
        raise ValueError("empty geometry")
    for i, item in enumerate(geometry[:-1]):
        next_item = geometry[i + 1]
        diff = (next_item[0] - item[0], next_item[1] - item[1])
        if abs(diff[0]) + abs(diff[1]) != 1:
            raise ValueError("non-connected snake geometry")
    if not all(is_in_scope(item) for item in geometry):
        raise SystemExit("snake out of bounds")
    if len(set(geometry)) != len(geometry):  # at least one repeated item
        raise SystemExit("snake self-collision")


class Snake:
    def __init__(self, geometry, direction):
        self.direction = direction
        self.geometry = geometry

    def get_head(self):
        return self._geometry[-1]

    head = property(get_head)

    def get_direction(self):
        return self._direction

    def set_direction(self, direction):
        check_direction(direction)
        self._direction = direction

    direction = property(get_direction, set_direction)

    def get_geometry(self):
        return copy.copy(self._geometry)

    def set_geometry(self, geometry):
        check_geometry(geometry)
        self._geometry = copy.copy(geometry)

    geometry = property(get_geometry, set_geometry)

    def move(self):
        x, y = self.head
        geometry = self.geometry
        dx, dy = self.direction
        new_head = (x + dx, y + dy)
        if new_head == state.fruit:
            state.fruit = (random.randint(0, X - 1), random.randint(0, Y - 1))
        else:  # remove the tail
            del geometry[0]
        geometry.append(new_head)
        self.geometry = geometry

class State:
    def __init__(self, snake, fruit):
        self.snake = snake
        self.fruit = fruit


state = State(
    snake=Snake([(10, 15), (11, 15), (12, 15)], DIRECTIONS["RIGHT"]), 
    fruit=(10, 10)
)

# Drawing functions
# ------------------------------------------------------------------------------
def draw_tile(screen, x, y, color):
    """
    x and y in tiles coordinates
    translate into pixel coordinates for painting
    """
    rect = pg.Rect(x * W, y * H, W, H)
    pg.draw.rect(screen, color, rect)


def draw_background(screen):
    screen.fill(WHITE)
    for x in range(X):
        for y in range(Y):
            if (x + y) % 2 == 0:
                draw_tile(screen, x, y, BLACK)

class SnakeGame(Game):
    def process_events(self, events):
        snake = state.snake
        for event in events:
            if (
                event.type == pg.QUIT
                or event.type == pg.KEYDOWN
                and event.key == pg.K_q
            ):
                self.quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    snake.direction = DIRECTIONS["DOWN"]
                elif event.key == pg.K_UP:
                    snake.direction = DIRECTIONS["UP"]
                elif event.key == pg.K_RIGHT:
                    snake.direction = DIRECTIONS["RIGHT"]
                elif event.key == pg.K_LEFT:
                    snake.direction = DIRECTIONS["LEFT"]
        try:
            snake.move()
        except SystemExit as error:
            message = error.args[0]
            self.quit(error=message)

    def draw(self):
        snake = state.snake
        fruit_x, fruit_y = state.fruit
        self.caption = f"Score: {len(snake.geometry)}"
        draw_background(self.screen)
        for x, y in snake.geometry:
            draw_tile(self.screen, x, y, SNAKE_COLOR)
        draw_tile(self.screen, fruit_x, fruit_y, FRUIT_COLOR)

if __name__ == "__main__":
    snake_game = SnakeGame(size=(X * W, Y * H), fps=FPS)
    snake_game.start()
