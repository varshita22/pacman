import pygame
# initialize the pygame
pygame.init()
# screen of w=800,h=600
screen = pygame.display.set_mode((800, 600))  # 2 beackets

# title and icon
pygame.display.set_caption("Pacman")
icon = pygame.image.load('pac32.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('pac32.png')
playerx = 370  # consider size of image also to display midway(half of 800)
playery = 480

playerx_change = 0
playery_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))  # to draw it on screen


# game loop, anything that has to be visible inside
# game window has to go inside while loop
running = True
while running:
    screen.fill((0, 128, 128))  # 3 values of RGB, teal
   # playerx += .05  # everytime while loop executes, moves .05 right
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if key stroke is left or right
        if event.type == pygame.KEYDOWN:  # pressing button
            if event.key == pygame.K_LEFT:
                playerx_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.3
            if event.key == pygame.K_UP:
                playery_change = -0.3
            if event.key == pygame.K_DOWN:
                playery_change = 0.3

        if event.type == pygame.KEYUP:  # release button
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerx_change = 0
                playery_change = 0

    playerx += playerx_change
    playery += playery_change

    if playerx <= 0:
        playerx = 0
    elif playerx >= 768:  # 800-32
        playerx = 768

    if playery <= 0:
        playery = 0
    elif playery >= 568:  # 600-32
        playery = 568

    player(playerx, playery)  # draw img above backgroung
    pygame.display.update()
