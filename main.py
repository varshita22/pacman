import pygame
from Walls import*
from Player import*
from Food import*
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
GREY = (107, 107, 107)
TEXT_SIZE = 16
TEXT_FONT = 'arial black'

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


def draw_score(words, screen, pos, size, colour, font_name):
    font = pygame.font.SysFont(font_name, size)
    text = font.render(words, False, colour)
    text_size = text.get_size()
    screen.blit(text, pos)


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
    draw_grid()
    draw_score("SCORE : ", screen, [16*9, 0], TEXT_SIZE, WHITE, TEXT_FONT)
    # for entity in food_list:
    # screen.blit(entity.image, entity.rect)
    all_sprite_list.update()
    pygame.display.update()
    # pygame.display.flip()
    clock.tick(60)
