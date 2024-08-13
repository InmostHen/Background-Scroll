import pygame
import os
import math

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 437

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Background scroll")

bg = pygame.image.load("bg.png").convert()
bg_width = bg.get_width()

#define game variables
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1

run = True
while run:

    clock.tick(FPS)

    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    
    scroll -= 5

    if abs(scroll) > bg_width:
        scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
