import pygame
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

# score
cur_score = 0
