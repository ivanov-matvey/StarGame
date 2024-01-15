import pygame


clock = pygame.time.Clock()

pygame.init()

width = 720
height = 720
screen = pygame.display.set_mode((width, height))
bg = pygame.image.load('images/bg.png').convert()
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

running = True
while running:

    clock.tick(60)

    screen.blit(bg, (0, bg_y))
    screen.blit(bg, (0, bg_y-height))
    screen.blit(flight[player_anim_count], (320, 320))

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
