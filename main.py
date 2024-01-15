import pygame

clock = pygame.time.Clock()

pygame.init()

width = 720
height = 720
screen = pygame.display.set_mode((width, height))
bg = pygame.image.load('images/bg.png')
bg = pygame.transform.scale(bg, (width, height))

pygame.display.set_caption('StarGame')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

bg_sound = pygame.mixer.Sound('sounds/bg.mp3')
bg_sound.play()

flight = [
    pygame.image.load('images/player/player1.png'),
    pygame.image.load('images/player/player2.png'),
    pygame.image.load('images/player/player3.png'),
]

player_anim_count = 0
i = 0
bg_y = 0
bg_x = 0

player_x = 320
player_y = 320
speed = 7
to_up = False
to_down = False
to_left = False
to_right = False

running = True
while running:

    clock.tick(60)

    background1 = screen.blit(bg, (bg_x, bg_y))
    background2 = screen.blit(bg, (bg_x, bg_y - height))
    screen.blit(flight[player_anim_count], (player_x, player_y))

    bg_y += 1
    if bg_y == 720:
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

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False

    if to_up:
        player_y -= speed
    if to_down:
        player_y += speed
    if to_left:
        player_x -= speed
    if to_right:
        player_x += speed
