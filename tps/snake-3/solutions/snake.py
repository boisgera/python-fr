# Python Standard Library
import copy
import random
import sys

# Third-Party Libraries
import pygame

# Local Modules
from game import Game
from constants import *

# Validation
# ------------------------------------------------------------------------------
def check_direction(direction):
    try:
        direction = list(direction)
    except TypeError:
        error = f"{direction} is not list-like"
        raise TypeError(error)
    if (
        len(direction) != 2
        or not isinstance(direction[0], int)
        or not isinstance(direction[1], int)
    ):
        raise TypeError(f"{direction} is not a pair of integers")
    elif direction not in DIRECTIONS:
        raise ValueError(f"{direction} is not in {DIRECTIONS}")


def is_in_scope(tile):
    x, y = tile
    return 0 <= x < WIDTH and 0 <= y < HEIGHT


def check_geometry(geometry):
    try:
        geometry = list(geometry)
    except TypeError:
        error = f"{geometry} is not list-like"
        raise TypeError(error)
    try:
        geometry = [list(item) for item in geometry]
    except TypeError:
        error = f"{item} is not list-like"
        raise TypeError(error)
    if not all(
        len(item) == 2 and isinstance(item[0], int) and isinstance(item[1], int)
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
        if elt in geometry[i + 1 :]:
            # at least one repeated item
            raise SystemExit("snake self-collision")


# Game State
# ------------------------------------------------------------------------------
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
        new_head = [head[0] + self.direction[0], head[1] + self.direction[1]]
        if new_head == state.fruit:
            state.score += 1
            self.geometry = self.geometry + [new_head]
            state.fruit = [random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)]
        else:
            self.geometry = self.geometry[1:] + [new_head]


class State:
    def __init__(self, snake, fruit, score=0):
        self.snake = snake
        self.fruit = fruit
        self.score = score

    def save(self):
        state = {
            "snake": self.snake.geometry,
            "direction": self.snake.direction,
            "fruit": self.fruit,
            "score": self.score,
        }
        with open(SNAPSHOT, mode="w") as file:
            file.write(repr(state))

    def load(self):
        with open(SNAPSHOT, mode="r", encoding="utf-8") as file:
            data = file.read()
        state = eval(data)
        self.state.geometry = state["snake"]
        self.direction = state["direction"]
        self.fruit = state["fruit"]
        self.score = state["score"]


state = State(snake=Snake([[10, 15], [11, 15], [12, 15]], RIGHT,), fruit=[10, 10],)


# Event Management
# ------------------------------------------------------------------------------
def set_direction(direction):
    def action():
        state.snake.direction = direction

    return action


KEY_BINDINGS = {
    "q": sys.exit,
    "up": set_direction(UP),
    "down": set_direction(DOWN),
    "left": set_direction(LEFT),
    "right": set_direction(RIGHT),
    "s": state.save,
    "l": state.load,
}

KEY_EVENT_HANDLER = {pygame.key.key_code(k): v for k, v in KEY_BINDINGS.items()}


# Drawing functions
# ------------------------------------------------------------------------------
def draw_cell(screen, x, y, color):
    rect = [x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE]
    pygame.draw.rect(screen, color, rect)


def draw_snake(screen, snake):
    for x, y in snake.geometry:
        draw_cell(screen, x, y, COLORS["snake"])


def draw_fruit(screen, fruit):
    fruit_x, fruit_y = fruit
    draw_cell(screen, fruit_x, fruit_y, COLORS["fruit"])


def draw_background(screen):
    screen.fill(COLORS["background"])
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (x + y) % 2 == 0:
                draw_cell(screen, x, y, COLORS["background-secondary"])


# Game
# ------------------------------------------------------------------------------
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
