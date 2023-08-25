# Python Standard Library
import random
import sys

# Pygame
import pygame

# Setup
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
snake = [
    [10, 15],
    [11, 15],
    [12, 15],
]
direction = DOWN
fruit = [10, 10]
score = 0

# Init
pygame.init()
screen = pygame.display.set_mode([CELL_SIZE*WIDTH, CELL_SIZE*HEIGHT])
clock = pygame.time.Clock()

# Main Loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
              sys.exit()
            if event.key == pygame.K_UP:
                direction = UP
            elif event.key == pygame.K_LEFT:
                direction = LEFT
            elif event.key == pygame.K_DOWN:
                direction = DOWN
            elif event.key == pygame.K_RIGHT:
                direction = RIGHT

    # Move the snake
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
            random.randint(0, WIDTH - 1), 
            random.randint(0, HEIGHT-1)
        ]
    else:
        snake = snake[1:] + [new_head]

    # Draw & update the screen
    screen.fill(COLORS["background"])
    for x, y in snake:
        rect = [x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE]
        pygame.draw.rect(screen, COLORS["snake"], rect)
    rect = [fruit[0]*CELL_SIZE, fruit[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE]
    pygame.draw.rect(screen, COLORS["fruit"], rect)
    pygame.display.set_caption(f"Score : {score}")
    pygame.display.update()

    # Time management
    clock.tick(FPS)