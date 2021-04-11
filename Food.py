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

food = Food(16, 16*4)  # top-left most food
food_list.add(food)
all_sprite_list.add(food)

food = Food(16, 16*6)
food_list.add(food)
all_sprite_list.add(food)

food = Food(16, 16*8)
food_list.add(food)
all_sprite_list.add(food)

food = Food(16, 16*10)
food_list.add(food)
all_sprite_list.add(food)
