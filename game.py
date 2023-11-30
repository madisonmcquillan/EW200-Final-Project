import pygame
import sys
from settings import *

pygame.init()

# screen
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("this town ain't big enough for the both of us")
screen.fill(BACKGROUND)
clock = pygame.time.Clock()
background = screen.copy()

# spaceships
yellow_spaceship = pygame.image.load("assets/images/spaceship_yellow.png")
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship, (spaceship_width, spaceship_height)), 90)
red_spaceship = pygame.image.load("assets/images/spaceship_red.png")
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship, (spaceship_width, spaceship_height)), 270)


def draw_background(red, yellow):
    background.blit(yellow_spaceship, (100, 100))
    background.blit(red_spaceship, (800, 100))


draw_background()

def move_spaceships():
    red = pygame.Rect(100, 300, spaceship_width, spaceship_height)
    yellow = pygame.Rect(700, 300, spaceship_width, spaceship_height)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    pygame.display.update()
    clock.tick(60)
