# Python Standard Library
import random
import sys

# Pygame
import pygame

# Setup
# ------------------------------------------------------------------------------
WIDTH = 30
HEIGHT = 30
CELL_SIZE = 20
FPS = 1.0
COLORS = {
    "background": [255, 255, 255],
    "snake": [0, 0, 0],
    "fruit": [255, 0, 0]
}
UP = [0, -1]
DOWN = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]
SNAPSHOT="snapshot.py"

# State
# ------------------------------------------------------------------------------
snake = [
    [10, 15],
    [11, 15],
    [12, 15],
]
direction = DOWN
fruit = [10, 10]
score = 0

def save_state():
    state = {
        "snake": snake,
        "direction": direction,
        "fruit": fruit,
        "score": score
    }
    with open(SNAPSHOT, mode="w") as file:
        file.write(repr(state))

def load_state():
    global snake, direction, fruit, score
    with open(SNAPSHOT, mode="r", encoding="utf-8") as file:
        data = file.read()
    state = eval(data)
    snake = state["snake"]
    direction = state["direction"]
    fruit = state["fruit"]
    score = state["score"]    


# Helper Functions
# ------------------------------------------------------------------------------
def init():
    global clock, screen
    pygame.init()
    screen = pygame.display.set_mode([CELL_SIZE*WIDTH, CELL_SIZE*HEIGHT])
    clock = pygame.time.Clock()

def draw(screen):
    screen.fill(COLORS["background"])
    for x, y in snake:
        rect = [x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE]
        pygame.draw.rect(screen, COLORS["snake"], rect)
    rect = [fruit[0]*CELL_SIZE, fruit[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE]
    pygame.draw.rect(screen, COLORS["fruit"], rect)  
    pygame.display.set_caption(f"Score : {score}")

def set_direction(d):
    def action():
        global direction
        direction = d
    return action

def move_snake():
    global snake, score, fruit
    head = snake[-1]
    new_head = [
      head[0] + direction[0], 
      head[1] + direction[1]
    ]
    if new_head in snake:
        sys.exit()
    elif new_head[0] < 0 or new_head[0] >= WIDTH:
        sys.exit()
    elif new_head[1] < 0 or new_head[1] >= HEIGHT:
        sys.exit()
    if new_head == fruit:
        score = score + 1
        snake = snake + [new_head]
        fruit = [
            random.randint(0, WIDTH-1), 
            random.randint(0, HEIGHT-1)
        ]
    else:
        snake = snake[1:] + [new_head]

# Event Management
# ------------------------------------------------------------------------------
KEY_MAP = {
    "q": sys.exit,
    "up": set_direction(UP),
    "down": set_direction(DOWN),
    "left": set_direction(LEFT),
    "right": set_direction(RIGHT),
    "s": save_state,
    "l": load_state,
}

KEYCODE_MAP = {pygame.key.key_code(k): v for k, v in KEY_MAP.items()}

def handle_events(events):
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            event_handler = KEYCODE_MAP.get(event.key)
            if event_handler:
                event_handler()

def wait_for_next_frame():
    clock.tick(FPS)

# Main Loop
# ------------------------------------------------------------------------------
try:
    load_state()
except FileNotFoundError:
    pass

init()
while True:
    events = pygame.event.get()
    handle_events(events)
    move_snake()
    draw(screen)
    pygame.display.update()
    wait_for_next_frame()
