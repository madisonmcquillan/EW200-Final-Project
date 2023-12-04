import pygame
import sys
from settings import *

pygame.mixer.init()

pygame.init()

# screen
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("this town ain't big enough for the both of us")
screen.fill(BACKGROUND)
background = screen.copy()
border = pygame.Rect((WIDTH // 2) - 5, 0, 10, HEIGTH)
health_font = pygame.font.Font("assets/fonts/QuirkyRobot.ttf", 75)
winner_font = pygame.font.Font("assets/fonts/QuirkyRobot.ttf", 80)
bullet_hit_sound = pygame.mixer.Sound("assets/sounds/Grenade+1.mp3")
bullet_fire_sound = pygame.mixer.Sound("assets/sounds/Gun+Silencer.mp3")

# music
pygame.mixer.music.load("assets/sounds/music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

# collisions
yellow_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2

# spaceships
yellow_spaceship = pygame.image.load("assets/images/spaceship_yellow.png")
yellow_spaceship = pygame.transform.rotate(
    pygame.transform.scale(yellow_spaceship, (spaceship_width, spaceship_height)), 90)
red_spaceship = pygame.image.load("assets/images/spaceship_red.png")
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship, (spaceship_width, spaceship_height)), 270)
red_speed = 5
yellow_speed = 5
bullet_speed = 7
max_bullets = 5

space = pygame.transform.scale(pygame.image.load("assets/images/space.png"), (WIDTH, HEIGTH))


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    pygame.draw.rect(screen, BORDER_COLOR, border)

    red_health_text = health_font.render("Health: " + str(red_health), 1, FONT_COLOR)
    yellow_health_text = health_font.render("Health: " + str(yellow_health), 1, FONT_COLOR)
    screen.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    screen.blit(yellow_health_text, (10, 10))

    for bullet in red_bullets:
        pygame.draw.rect(screen, BULLET_COLOR_RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(screen, BULLET_COLOR_YELLOW, bullet)

    pygame.display.update()


def move_yellow_spaceship(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x > 0:
        yellow.x -= yellow_speed
    if keys_pressed[pygame.K_d] and yellow.x < border.x - yellow.width:
        yellow.x += yellow_speed
    if keys_pressed[pygame.K_w] and yellow.y > 0:
        yellow.y -= yellow_speed
    if keys_pressed[pygame.K_s] and yellow.y < HEIGTH - yellow.height - 15:
        yellow.y += yellow_speed


def move_red_spaceship(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x > border.x + 25:
        red.x -= red_speed
    if keys_pressed[pygame.K_RIGHT] and red.x < WIDTH - 40:
        red.x += red_speed
    if keys_pressed[pygame.K_UP] and red.y > 0:
        red.y -= red_speed
    if keys_pressed[pygame.K_DOWN] and red.y < HEIGTH - red.height - 15:
        red.y += red_speed


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += bullet_speed
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= bullet_speed
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellow_hit))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw_winner(text):
    text = winner_font.render(text, 1, FONT_COLOR)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGTH / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    global red_speed
    global yellow_speed

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
                    bullet_fire_sound.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < max_bullets:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    bullet_fire_sound.play()

            if event.type == red_hit:
                red_health -= 1
                red_speed += 0.5
                bullet_hit_sound.play()

            if event.type == yellow_hit:
                yellow_health -= 1
                yellow_speed += 0.5
                bullet_hit_sound.play()

        winner = ""
        if red_health <= 0:
            winner = "Yellow Wins! and Red Loses :("
            red_speed = 5
            yellow_speed = 5

        if yellow_health <= 0:
            winner = "Red Wins! and Yellow Loses :("
            yellow_speed = 5
            red_speed = 5

        if winner != "":
            draw_winner(winner)
            break

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


main()
