import pygame
import sys
from settings import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(GRASS_COLOR)
background = screen.copy()

# images
bottom_grass = pygame.image.load("assets/images/bottomgrass.png").convert()
bottomcorner_grass = pygame.image.load("assets/images/bottomcorner_grass.png").convert()
rightbottomcorner = pygame.image.load("assets/images/rightbottomcorner.png").convert()


def draw_background():
    background.fill(GRASS_COLOR)
    background.blit(bottomcorner_grass, (0, SCREEN_HEIGHT - TILE_SIZE))

    for i in range(8):
        background.blit(bottom_grass, ((i+1)* TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))

    background.blit(rightbottomcorner, (8*TILE_SIZE, SCREEN_HEIGHT-TILE_SIZE))

    for i in range()


draw_background()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    pygame.display.flip()
