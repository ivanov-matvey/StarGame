import pygame
import random


clock = pygame.time.Clock()

pygame.init()

width = 720
height = 720
screen = pygame.display.set_mode((width, height))
bg = pygame.image.load('images/bg.png').convert()
bg = pygame.transform.scale(bg, (width, height))

pygame.display.set_caption('StarGame')
icon = pygame.image.load('images/icon.png').convert()
pygame.display.set_icon(icon)

bg_sound = pygame.mixer.Sound('sounds/bg.mp3')
bg_sound.play()

player = [
    pygame.image.load('images/player/player1.png').convert_alpha(),
    pygame.image.load('images/player/player2.png').convert_alpha(),
    pygame.image.load('images/player/player3.png').convert_alpha(),
]

player_anim_count = 0
i = 0
bg_y = 0
bg_x = 0

player_x = (width // 2) - 40
player_y = (height // 2) - 40
speed = 8

asteroid = pygame.image.load('images/asteroid.png').convert_alpha()
asteroid_in_game = []
asteroid_timer = pygame.USEREVENT + 1
pygame.time.set_timer(asteroid_timer, 500)


def side():
    rnd = random.randint(1, 2)
    if rnd == 1:
        return -80
    if rnd == 2:
        return width+80


running = True
while running:

    clock.tick(60)

    screen.blit(bg, (bg_x, bg_y))
    screen.blit(bg, (bg_x, bg_y - height))

    screen.blit(player[player_anim_count], (player_x, player_y))
    player_rect = player[0].get_rect(topleft=(player_x, player_y))

    if asteroid_in_game:
        for el in asteroid_in_game:
            screen.blit(asteroid, el)
            el.y += 4

            if el.y >= height+80:
                del asteroid_in_game[asteroid_in_game.index(el)]

            if player_rect.colliderect(el):
                print('lose')

    keys = pygame.key.get_pressed()

    bg_y += 1
    if bg_y == height:
        bg_y = 0

    if i <= 15:
        player_anim_count = 0
        i += 1
    elif i <= 30:
        player_anim_count = 1
        i += 1
    elif i <= 45:
        player_anim_count = 2
        i += 1
    else:
        player_anim_count = 0
        i = 0

    if (keys[pygame.K_UP] or keys[pygame.K_w]) and player_y > 0:
        player_y -= speed
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player_y < height-80:
        player_y += speed
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_x > 0:
        player_x -= speed
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_x < height-80:
        player_x += speed

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == asteroid_timer:
            asteroid_in_game.append(asteroid.get_rect(topleft=(random.randint(0, width-80), -80)))
