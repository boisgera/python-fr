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

# Game State
snake = [
    [10, 15],
    [11, 15],
    [12, 15],
]
direction = [1, 0]
fruit = [10, 10]
score = 0

# Setup
pygame.init()
width_height = [WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE]
screen = pygame.display.set_mode(width_height)
clock = pygame.time.Clock()

# Helper Function
def exit():
    pygame.quit()
    sys.exit()

# Main Loop
while True:
    # Event Management
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                exit()
            if event.key == pygame.K_UP:
                direction = UP
            elif event.key == pygame.K_LEFT:
                direction = LEFT
            elif event.key == pygame.K_DOWN:
                direction = DOWN
            elif event.key == pygame.K_RIGHT:
                direction = RIGHT

    # Game Logic (move snake)
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
        exit()
    if new_head == fruit:
        score = score + 1
        snake = snake + [new_head]
        fruit = [
            random.randint(0, 29),
            random.randint(0, 29)
        ]
    else:
        snake = snake[1:] + [new_head]

    # Frame Update
    screen.fill(COLORS["background"])
    for x, y in snake:
        rect = [x*20, y*20, 20, 20]
        pygame.draw.rect(screen, COLORS["snake"], rect)
    rect = [fruit[0]*20, fruit[1]*20, 20, 20]
    pygame.draw.rect(screen, COLORS["fruit"], rect)
    pygame.display.update()
    pygame.display.set_caption(f"🐍 Score: {score}")

    # Wait for next frame ... wait for it! 
    # (📺 https://www.youtube.com/watch?v=O_mlJwQ1_ZM)
    clock.tick(FPS)

