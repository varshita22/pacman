import pygame
from Walls import*
from Player import*
from Food import*
from settings import*
from Blinky_ghost import*
import random
# initialize the pygame
pygame.init()

# title and icon
pygame.display.set_caption("Pacman")
icon = pygame.image.load('pac32.png')
pygame.display.set_icon(icon)

# game loop, anything that has to be visible inside
# game window has to go inside while loop


def draw_grid():
    for x in range(28):
        pygame.draw.line(screen, GREY, (x*16, 0), (x*16, h)
                         )  # draw line from(x,y) to (x,y)
    for x in range(36):
        pygame.draw.line(screen, GREY, (0, x*16), (w, x*16))


clock = pygame.time.Clock()
# running
running = True

while running:
    screen.fill(BLACK)  # 3 values of RGB

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

        if event.type == pygame.KEYDOWN:
            n = random.randint(-2, 1)
            if n == -2:
                #print("hi -2")
                rghost.changespeed(4, 0)
            elif n == -1:
                #print("hi -1")
                rghost.changespeed(-4, 0)
            elif n == 0:
                #print("hi 0")
                rghost.changespeed(0, 4)
            else:
                #print("hi 1")
                rghost.changespeed(0, -4)

    all_sprite_list.draw(screen)
    draw_grid()
    # rghost.update()
    all_sprite_list.update()
    draw_score("SCORE : ", player.update(), screen, [
        16*9, 0], TEXT_SIZE, WHITE, TEXT_FONT)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
