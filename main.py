import pygame
from Walls import*
from Player import*
# initialize the pygame
pygame.init()


# screen of w=800,h=600
w = 16*28
h = 16*36   # 16 x 16 px square
screen = pygame.display.set_mode((w, h))  # 2 brackets

# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

# title and icon
pygame.display.set_caption("Pacman")
icon = pygame.image.load('pac32.png')
pygame.display.set_icon(icon)

# game loop, anything that has to be visible inside
# game window has to go inside while loop

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)  # 3 values of RGB, teal

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if key stroke is left , right, up or down
        if event.type == pygame.KEYDOWN:  # pressing button
            if event.key == pygame.K_LEFT:
                player.changespeed(-4, 0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(4, 0)
            if event.key == pygame.K_UP:
                player.changespeed(0, -4)
            if event.key == pygame.K_DOWN:
                player.changespeed(0, 4)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(4, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-4, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 4)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -4)

    all_sprite_list.draw(screen)
    all_sprite_list.update()
    pygame.display.update()
    clock.tick(60)
