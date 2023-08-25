import random
import sys
import pygame

# Constants
WIDTH = 30      # number of cells
HEIGHT = 30     # number of cells
CELL_SIZE = 20  # number of pixels
FPS = 1  # frames per second
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]
COLORS = {
    "background": WHITE,
    "snake": BLACK,
    "fruit": RED
}
UP = [0, -1]
DOWN = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]
SNAPSHOT = "snapshot.py"

# Game State
snake = [
    [10, 15],
    [11, 15],
    [12, 15],
]
direction = [1, 0]
fruit = [10, 10]
score = 0

def save_state():
    state = {
        "snake": snake,
        "direction": direction,
        "fruit": fruit,
        "score": score
    }
    with open(SNAPSHOT, mode="w", encoding="utf-8") as file:
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
def setup():
    pygame.init()
    width_height = [WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE]
    screen = pygame.display.set_mode(width_height)
    clock = pygame.time.Clock()
    return screen, clock

def handle_events():
    global direction
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          exit()
      elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
              exit()
          elif event.key == pygame.K_s:
              save_state()
          elif event.key == pygame.K_l:
              load_state()
          if event.key == pygame.K_UP:
              direction = UP
          elif event.key == pygame.K_LEFT:
              direction = LEFT
          elif event.key == pygame.K_DOWN:
              direction = DOWN
          elif event.key == pygame.K_RIGHT:
              direction = RIGHT

def move_snake():
    global fruit, score, snake
    head = snake[-1]
    new_head = [
      head[0] + direction[0],
      head[1] + direction[1]
    ]
    if (
        new_head in snake
        or new_head[0] < 0
        or new_head[0] >= 30
        or new_head[1] < 0
        or new_head[1] >= 30
    ):
        pygame.quit()
        sys.exit()
    if new_head == fruit:
        score = score + 1
        snake = snake + [new_head]
        fruit = [
            random.randint(0, 29),
            random.randint(0, 29)
        ]
    else:
        snake = snake[1:] + [new_head]

def draw_frame(screen):
    screen.fill(COLORS["background"])
    for x, y in snake:
        rect = [x*20, y*20, 20, 20]
        pygame.draw.rect(screen, COLORS["snake"], rect)
    rect = [fruit[0]*20, fruit[1]*20, 20, 20]
    pygame.draw.rect(screen, COLORS["fruit"], rect)
    pygame.display.update()
    pygame.display.set_caption(f"🐍 Score: {score}")

def wait_for_next_frame(clock):
    clock.tick(FPS)

def exit():
    pygame.quit()
    sys.exit()

# Setup & Main Loop
screen, clock = setup()
while True:
    handle_events()
    move_snake()
    draw_frame(screen)
    wait_for_next_frame(clock) 

