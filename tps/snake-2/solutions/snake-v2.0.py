
# Python Standard Library
import random
import sys

# Pygame
import pygame

# Setup
white = [255, 255, 255]
black = [0, 0, 0]
red = [255, 0, 0]

# State
snake = [
    [10, 15],
    [11, 15],
    [12, 15],
]
direction = [1, 0]
fruit = [10, 10]
score = 0

# Init
pygame.init()
screen = pygame.display.set_mode([20*30, 20*30])
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
                direction = [0.0, -1.0]
            elif event.key == pygame.K_LEFT:
                direction = [-1.0, 0.0]
            elif event.key == pygame.K_DOWN:
                direction = [0.0, 1.0]
            elif event.key == pygame.K_RIGHT:
                direction = [1.0, 0.0]

    # Move the snake
    head = snake[-1]
    new_head = [
      head[0] + direction[0], 
      head[1] + direction[1]
    ]
    if new_head in snake:
        sys.exit()
    elif new_head[0] < 0 or new_head[0] >= 30:
        sys.exit()
    elif new_head[1] < 0 or new_head[1] >= 30:
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

    # Draw & update the screen
    screen.fill(white)
    for x, y in snake:
        rect = [x*20, y*20, 20, 20]
        pygame.draw.rect(screen, black, rect)
    rect = [fruit[0]*20, fruit[1]*20, 20, 20]
    pygame.draw.rect(screen, red, rect)
    pygame.display.set_caption(f"Score: {score}")
    pygame.display.update()

    # Time management
    clock.tick(1.0)