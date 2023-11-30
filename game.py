import pygame
import sys
from settings import *

pygame.init()

# screen
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("this town ain't big enough for the both of us")
screen.fill(BACKGROUND)
background = screen.copy()

# spaceships
yellow_spaceship = pygame.image.load("assets/images/spaceship_yellow.png")
yellow_spaceship = pygame.transform.rotate(
    pygame.transform.scale(yellow_spaceship, (spaceship_width, spaceship_height)), 90)
red_spaceship = pygame.image.load("assets/images/spaceship_red.png")
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship, (spaceship_width, spaceship_height)), 270)
speed = 5


def move_yellow_spaceship(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]:
        yellow.x -= speed
    if keys_pressed[pygame.K_d]:
        yellow.x += speed
    if keys_pressed[pygame.K_w]:
        yellow.y -= speed
    if keys_pressed[pygame.K_s]:
        yellow.y += speed


def move_red_spaceship(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]:
        red.x -= speed
    if keys_pressed[pygame.K_RIGHT]:
        red.x += speed
    if keys_pressed[pygame.K_UP]:
        red.y -= speed
    if keys_pressed[pygame.K_DOWN]:
        red.y += speed


def main():
    red = pygame.Rect(700, 300, spaceship_width, spaceship_height)
    yellow = pygame.Rect(100, 300, spaceship_width, spaceship_height)

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys_pressed = pygame.key.get_pressed()
        move_yellow_spaceship(keys_pressed, yellow)
        move_red_spaceship(keys_pressed, red)
    
        # screen
        screen.fill(BACKGROUND)
        screen.blit(yellow_spaceship, (yellow.x, yellow.y))
        screen.blit(red_spaceship, (red.x, red.y))
        pygame.display.update()


main()
