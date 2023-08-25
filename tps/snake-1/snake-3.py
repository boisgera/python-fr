import sys
import pygame

white = [255, 255, 255]
black = [0, 0, 0]
snake = [
[10, 15],
[11, 15],
[12, 15],
]

pygame.init()
screen = pygame.display.set_mode([20*30, 20*30])
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
screen.fill(white)
for x, y in snake:
rect = [x*20, y*20, 20, 20]
pygame.draw.rect(screen, black, rect)  
 pygame.display.update()
clock.tick(1)


