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
leftsidegrass = pygame.image.load("assets/images/leftsidegrass.png").convert()
lefttopcorner = pygame.image.load("assets/images/lefttopcorner.png").convert()
righttopcorner = pygame.image.load("assets/images/righttopcorner.png").convert()
top_grass = pygame.image.load("assets/images/top_grass.png").convert()
rightsidegrass = pygame.image.load("assets/images/rightsidegrass.png").convert()
dirt = pygame.image.load("assets/images/dirt.png").convert()
leftbottomwater = pygame.image.load("assets/images/leftbottomwater.png").convert()
rightbottomwater = pygame.image.load("assets/images/rightbottomwater.png").convert()
bottomwater = pygame.image.load("assets/images/bottomwater.png").convert()
toprightwater = pygame.image.load("assets/images/toprightwater.png").convert()
topleftwater = pygame.image.load("assets/images/topleftwater.png").convert()
topwater = pygame.image.load("assets/images/topwater.png").convert()
leftsidewater = pygame.image.load("assets/images/leftsidewater.png").convert()
rightsidewater = pygame.image.load("assets/images/rightsidewater.png").convert()
water = pygame.image.load("assets/images/water.png").convert()
sunflowerstore = pygame.image.load("assets/images/sunflowerstore.jpg").convert()
rosestore = pygame.image.load("assets/images/rosestore.jpg").convert()
daffodilstore = pygame.image.load("assets/images/daffodilstore.jpg").convert()
snowdropstore = pygame.image.load("assets/images/snowdropstore.jpg").convert()
lotusstore = pygame.image.load("assets/images/lotusstore.jpg").convert()
emptywatercan = pygame.image.load("assets/images/emptywatercan.jfif").convert()
fullwatercan = pygame.image.load("assets/images/fullwatercan.png").convert()


def draw_background():
    background.fill(GRASS_COLOR)
    background.blit(bottomcorner_grass, (0, SCREEN_HEIGHT - TILE_SIZE))
    # grass and dirt
    for i in range(8):
        background.blit(bottom_grass, ((i + 1) * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))
    background.blit(rightbottomcorner, (8 * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))
    background.blit(lefttopcorner, (0, 2 * TILE_SIZE))
    background.blit(righttopcorner, (8 * TILE_SIZE, 2 * TILE_SIZE))
    for i in range(6):
        background.blit(leftsidegrass, (0, (i + 3) * TILE_SIZE))
        background.blit(rightsidegrass, (8 * TILE_SIZE, (i + 3) * TILE_SIZE))
    for i in range(7):
        background.blit(top_grass, ((i + 1) * TILE_SIZE, 2 * TILE_SIZE))
    # change this to be more compact
    for i in range(6):
        background.blit(dirt, (TILE_SIZE, (i + 3) * TILE_SIZE))
        background.blit(dirt, (2 * TILE_SIZE, (i + 3) * TILE_SIZE))
        background.blit(dirt, (3 * TILE_SIZE, (i + 3) * TILE_SIZE))
        background.blit(dirt, (4 * TILE_SIZE, (i + 3) * TILE_SIZE))
        background.blit(dirt, (5 * TILE_SIZE, (i + 3) * TILE_SIZE))
        background.blit(dirt, (6 * TILE_SIZE, (i + 3) * TILE_SIZE))
        background.blit(dirt, (7 * TILE_SIZE, (i + 3) * TILE_SIZE))
    # water
    background.blit(leftbottomwater, (9 * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))
    background.blit(rightbottomwater, (SCREEN_WIDTH - TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))
    background.blit(bottomwater, (10 * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))
    background.blit(toprightwater, (SCREEN_WIDTH - TILE_SIZE, 2 * TILE_SIZE))
    background.blit(topleftwater, (9 * TILE_SIZE, 2 * TILE_SIZE))
    background.blit(topwater, (10 * TILE_SIZE, 2 * TILE_SIZE))
    # store
    background.blit(sunflowerstore, (0, 0))
    background.blit(rosestore, (90, 0))
    background.blit(daffodilstore, (180, 0))
    background.blit(snowdropstore, (268, 0))
    background.blit(lotusstore, (356, 0))
    for i in range(6):
        background.blit(leftsidewater, (9 * TILE_SIZE, (i + 3) * TILE_SIZE))
        background.blit(rightsidewater, (SCREEN_WIDTH - TILE_SIZE, (i + 3) * TILE_SIZE))
        background.blit(water, (10 * TILE_SIZE, (i + 3) * TILE_SIZE))


draw_background()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    pygame.display.flip()
