import pygame
import random


clock = pygame.time.Clock()

pygame.init()

width = 720
height = 720
screen = pygame.display.set_mode((width, height))
bg = pygame.image.load('images/bg/bg.png').convert()
bg = pygame.transform.scale(bg, (width, height))
stars = pygame.image.load('images/bg/stars.png').convert_alpha()
stars = pygame.transform.scale(stars, (width, height))

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
anim = 0

bg_y = 0
stars_y = 0

player_x = (width // 2) - 40
player_y = (height // 2) - 40
speed = 8

asteroid = pygame.image.load('images/asteroid.png').convert_alpha()
asteroid_in_game = []

bullet = pygame.image.load('images/bullet.png').convert_alpha()
bullet_in_game = []

score = 0

asteroid_timer = pygame.USEREVENT + 1
pygame.time.set_timer(asteroid_timer, 750)

bullet_timer = pygame.USEREVENT + 2
pygame.time.set_timer(bullet_timer, 500)

label = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 40)
lose_label = label.render('YOU LOSE!', False, (75, 75, 248))
lose_label_rect = lose_label.get_rect(center=(width//2, height//2-100))

button = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 32)
restart_button = button.render('RESTART', False,
                               (195, 195, 222), (100, 100, 233))
restart_button_rect = restart_button.get_rect(center=(width//2, height//2))

score_text = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 24)


gameplay = True

running = True
while running:

    screen.blit(bg, (0, bg_y))
    screen.blit(bg, (0, bg_y - height))
    screen.blit(stars, (0, stars_y))
    screen.blit(stars, (0, stars_y - height))

    if gameplay:

        player_rect = player[0].get_rect(topleft=(player_x, player_y))

        bg_y += 1
        if bg_y >= height:
            bg_y = 0
        stars_y += 1.1
        if stars_y >= height:
            stars_y = 0

        if asteroid_in_game:
            for (i, el) in enumerate(asteroid_in_game):
                screen.blit(asteroid, el)
                el.y += 4

                if el.y >= height+80:
                    asteroid_in_game.pop(i)

                if player_rect.colliderect(el):
                    gameplay = False

        if bullet_in_game:
            for (i, el) in enumerate(bullet_in_game):
                screen.blit(bullet, el)
                el.y -= 8

                if el.y <= -20:
                    bullet_in_game.pop(i)

                if asteroid_in_game:
                    for (index, asteroid_el) in enumerate(asteroid_in_game):
                        if el.colliderect(asteroid_el):
                            asteroid_in_game.pop(index)
                            bullet_in_game.pop(i)
                            score += 1

        keys = pygame.key.get_pressed()

        if (keys[pygame.K_UP] or keys[pygame.K_w]) and player_y > 0:
            player_y -= speed
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player_y < height-80:
            player_y += speed
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_x > 0:
            player_x -= speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_x < height-80:
            player_x += speed

        screen.blit(player[player_anim_count], (player_x, player_y))

        if anim <= 15:
            player_anim_count = 0
            anim += 1
        elif anim <= 30:
            player_anim_count = 1
            anim += 1
        elif anim <= 45:
            player_anim_count = 2
            anim += 1
        else:
            player_anim_count = 0
            anim = 0

        score_label = score_text.render(f'SCORE: {score}', False,
                                        (75, 75, 248))
        score_label_rect = score_label.get_rect(
            center=(width // 2, height // 2 - 60))
        screen.blit(score_label, (24, 24))

    else:
        screen.fill((20, 24, 46))
        screen.blit(lose_label, lose_label_rect)
        screen.blit(restart_button, restart_button_rect)
        screen.blit(score_label, score_label_rect)

        mouse = pygame.mouse.get_pos()
        if (restart_button_rect.collidepoint(mouse)
                and pygame.mouse.get_pressed()[0]):
            gameplay = True
            player_x = (width // 2) - 40
            player_y = (height // 2) - 40
            asteroid_in_game.clear()
            bullet_in_game.clear()
            score = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == asteroid_timer:
            asteroid_in_game.append(asteroid.get_rect(
                topleft=(random.randint(0, width-80), -80)))
        elif event.type == bullet_timer:
            bullet_in_game.append(bullet.get_rect(
                topleft=(player_x + 34, player_y + 10)))

    clock.tick(60)
