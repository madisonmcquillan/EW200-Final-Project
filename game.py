import pygame
import sys
from settings import *

pygame.init()

# screen
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("this town ain't big enough for the both of us")
screen.fill(BACKGROUND)
background = screen.copy()
border = pygame.Rect((WIDTH // 2) - 5, 0, 10, HEIGTH)
health_font = pygame.font.Font("assets/fonts/QuirkyRobot.ttf", 100)

# collisions
yellow_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2

# spaceships
yellow_spaceship = pygame.image.load("assets/images/spaceship_yellow.png")
yellow_spaceship = pygame.transform.rotate(
    pygame.transform.scale(yellow_spaceship, (spaceship_width, spaceship_height)), 90)
red_spaceship = pygame.image.load("assets/images/spaceship_red.png")
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship, (spaceship_width, spaceship_height)), 270)
speed = 5
bullet_speed = 7
max_bullets = 5

space = pygame.transform.scale(pygame.image.load("assets/images/space.png"), (WIDTH, HEIGTH))


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    pygame.draw.rect(screen, BORDER_COLOR, border)

    red_health_text = health_font.render("Health: " + str(red_health), 1, BORDER_COLOR)
    yellow_health_text = health_font.render("Health: " + str(yellow_health), 1, BORDER_COLOR)
    screen.blit(red_health_text, (WIDTH-red_health_text.get_width()-10))


    for bullet in red_bullets:
        pygame.draw.rect(screen, BULLET_COLOR_RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(screen, BULLET_COLOR_YELLOW, bullet)

    pygame.display.update()


def move_yellow_spaceship(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x > 0:
        yellow.x -= speed
    if keys_pressed[pygame.K_d] and yellow.x < border.x - yellow.width:
        yellow.x += speed
    if keys_pressed[pygame.K_w] and yellow.y > 0:
        yellow.y -= speed
    if keys_pressed[pygame.K_s] and yellow.y < HEIGTH - yellow.height - 15:
        yellow.y += speed


def move_red_spaceship(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x > border.x + 25:
        red.x -= speed
    if keys_pressed[pygame.K_RIGHT] and red.x < WIDTH - 40:
        red.x += speed
    if keys_pressed[pygame.K_UP] and red.y > 0:
        red.y -= speed
    if keys_pressed[pygame.K_DOWN] and red.y < HEIGTH - red.height - 15:
        red.y += speed


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += speed
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= speed
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellow_hit))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def main():
    red = pygame.Rect(700, 300, spaceship_width, spaceship_height)
    yellow = pygame.Rect(100, 300, spaceship_width, spaceship_height)

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < max_bullets:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(red_bullets) < max_bullets:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)

            if event.type == red_hit:
                red_health -=1

            if event.type == yellow_hit:
                yellow_health -= 1

        winner = ""
        if red_health <= 0:
            winner = "Yellow Wins! and You Lose!"

        if yellow_health <= 0:
            winner = "Red Wins! and You Lose!"

        if winner != "":
            pass

        keys_pressed = pygame.key.get_pressed()
        move_yellow_spaceship(keys_pressed, yellow)
        move_red_spaceship(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        # screen
        screen.blit(space, (0, 0))
        screen.blit(yellow_spaceship, (yellow.x, yellow.y))
        screen.blit(red_spaceship, (red.x, red.y))
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)


main()
