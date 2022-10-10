import random
import sys
import pygame

white = [255, 255, 255]
black = [0, 0, 0]
red = [255, 0, 0]
snake = [
    [10, 15],
    [11, 15],
    [12, 15],
]
direction = [1, 0]
fruit = [10, 10]

pygame.init()
screen = pygame.display.set_mode([20 * 30, 20 * 30])
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                direction = [0, -1]
            elif event.key == pygame.K_LEFT:
                direction = [-1, 0]
            elif event.key == pygame.K_DOWN:
                direction = [0, 1]
            elif event.key == pygame.K_RIGHT:
                direction = [1, 0]
    head = snake[-1]
    new_head = [head[0] + direction[0], head[1] + direction[1]]
    if new_head == fruit:
        snake = snake + [new_head]
        fruit = [random.randint(0, 29), random.randint(0, 29)]
    else:
        snake = snake[1:] + [new_head]
    screen.fill(white)
    for x, y in snake:
        rect = [x * 20, y * 20, 20, 20]
        pygame.draw.rect(screen, black, rect)
    rect = [fruit[0] * 20, fruit[1] * 20, 20, 20]
    pygame.draw.rect(screen, red, rect)
    pygame.display.update()
    clock.tick(1)
