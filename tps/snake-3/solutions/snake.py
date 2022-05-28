# Python Standard Library
import copy
import doctest
import random
import sys

# Third-Party Libraries
import pygame

# Local Modules
from game import Game
from constants import *

# Game state
# ------------------------------------------------------------------------------
def check_direction(direction):
    """
    Check that direction is either [-1, 0], [1, 0], [0, -1] or [0, 1]

    Usage:

    >>> check_direction([1, 0])
    >>> check_direction([-1, 0])
    >>> check_direction([0, 1])
    >>> check_direction([0, -1])

    >>> check_direction([0, 0])
    Traceback (most recent call last):
    ...
    ValueError: [0, 0] is not in [[0, 1], [0, -1], [1, 0], [-1, 0]]
    >>> check_direction([1, 1])
    Traceback (most recent call last):
    ...
    ValueError: [1, 1] is not in [[0, 1], [0, -1], [1, 0], [-1, 0]]
    >>> check_direction([7, 12])
    Traceback (most recent call last):
    ...
    ValueError: [7, 12] is not in [[0, 1], [0, -1], [1, 0], [-1, 0]]

    >>> check_direction([0, "Hello"])
    Traceback (most recent call last):
    ...
    TypeError: [0, 'Hello'] is not a pair of integers
    >>> check_direction([0, 1, 2])
    Traceback (most recent call last):
    ...
    TypeError: [0, 1, 2] is not a pair of integers
    >>> check_direction(True)
    Traceback (most recent call last):
    ...
    TypeError: True is not a pair of integers
    >>> check_direction([1.0, 2.0])
    Traceback (most recent call last):
    ...
    TypeError: [1.0, 2.0] is not a pair of integers
    """
    if (
        not isinstance(direction, list)
        or len(direction) != 2
        or not isinstance(direction[0], int)
        or not isinstance(direction[1], int)
    ):
        raise TypeError(f"{direction} is not a pair of integers")
    elif direction not in DIRECTIONS:
        raise ValueError(f"{direction} is not in {valid_directions}")


def is_in_scope(tile):
    x, y = tile
    return 0 <= x < WIDTH and 0 <= y < HEIGHT


def check_geometry(geometry):
    if not all(
        isinstance(item, list)
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

    for i, elt in enumerate(geometry):
        if elt in geometry[i+1:]:
            # at least one repeated item
            raise SystemExit("snake self-collision")

class Snake:
    def __init__(self, geometry, direction):
        self.direction = direction
        self.geometry = geometry

    def get_direction(self):
        return copy.deepcopy(self._direction)

    def set_direction(self, direction):
        check_direction(direction)
        self._direction = copy.deepcopy(direction)

    direction = property(get_direction, set_direction)

    def get_geometry(self):
        return copy.deepcopy(self._geometry)

    def set_geometry(self, geometry):
        check_geometry(geometry)
        self._geometry = copy.deepcopy(geometry)

    geometry = property(get_geometry, set_geometry)

    def get_head(self):
        return self.geometry[-1]

    head = property(get_head)


    def move(self):
        head = self.head
        new_head = [
            head[0] + self.direction[0], 
            head[1] + self.direction[1]
        ]
        if new_head == state.fruit:
            state.score += 1
            self.geometry = self.geometry + [new_head]
            state.fruit = [
                random.randint(0, WIDTH-1), 
                random.randint(0, HEIGHT-1)
            ]
        else:
            self.geometry = self.geometry[1:] + [new_head]

class State:
    def __init__(self, snake, fruit, score=0):
        self.snake = snake
        self.fruit = fruit
        self.score = score

state = State(
    snake=Snake([[10, 15], [11, 15], [12, 15]], RIGHT), 
    fruit=[10, 10]
)

# ------------------------------------------------------------------------------
def set_direction(direction):
    def action():
        state.snake.direction = direction
    return action

# Event Management
# ------------------------------------------------------------
KEY_BINDINGS = {
    "q": sys.exit,
    "up": set_direction(UP),
    "down": set_direction(DOWN),
    "left": set_direction(LEFT),
    "right": set_direction(RIGHT),
}

KEY_EVENT_HANDLER = {pygame.key.key_code(k): v for k, v in KEY_BINDINGS.items()}


# Drawing functions
# ------------------------------------------------------------------------------
def draw_tile(screen, x, y, color):
    """
    x and y in tiles coordinates
    translate into pixel coordinates for painting
    """
    rect = [x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE]
    pygame.draw.rect(screen, color, rect)

def draw_snake(screen, snake):
    for x, y in snake.geometry:
        draw_tile(screen, x, y, COLORS["snake"])

def draw_fruit(screen, fruit):
    fruit_x, fruit_y = fruit
    draw_tile(screen, fruit_x, fruit_y, COLORS["fruit"])

def draw_background(screen):
    screen.fill(COLORS["background"])
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (x + y) % 2 == 0:
                draw_tile(screen, x, y, COLORS["background-secondary"])

class SnakeGame(Game):
    def process_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                event_handler = KEY_EVENT_HANDLER.get(event.key)
                if event_handler:
                    event_handler()
        state.snake.move()

    def draw(self):
        screen = self.screen
        self.caption = f"Score: {state.score}"
        draw_background(screen)
        draw_snake(screen, state.snake)
        draw_fruit(screen, state.fruit)


if __name__ == "__main__":
    snake_game = SnakeGame()
    snake_game.start()
    