import pygame
from Walls import*
from Player import*
pygame.init()

# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

# Food Class


class Food(pygame.sprite.Sprite):

    def __init__(self, x, y):

        # Call the parent's constructor
        super().__init__()

        # Make a white food, of the size specified in the parameters
        self.image = pygame.Surface([16, 16])
        self.image.fill(WHITE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


food_list = pygame.sprite.Group()


def d_food(xs, ys, xe, ye):  # draws a line of food
    if(xs == xe):
        for i in range(ys, ye, 32):  # 16
            food = Food(xs, i)
            food_list.add(food)
            all_sprite_list.add(food)
    if(ys == ye):
        for i in range(xs, xe, 32):  # 16
            food = Food(i, ys)
            food_list.add(food)
            all_sprite_list.add(food)


d_food(16, 16*4, 16, 16*11)
