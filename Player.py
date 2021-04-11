import pygame
from Walls import*
from Food import*
pygame.init()

# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

# player

pic = pygame.image.load('pac32.png')
pic = pygame.transform.scale(pic, (24, 24))  # 32x32, 8+16+8?


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
        self.image = pic
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

       # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None
        self.food = None

    def changespeed(self, x, y):

        self.change_x += x
        self.change_y += y

    def update(self):

        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of the item we hit or vice versa
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            # same for up down
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

        # if(pygame.sprite.spritecollide(self, self.food, True)):
        #     print("hi")
        pygame.sprite.spritecollide(self, self.food, True)


player = Player(8, 56)
player.walls = wall_list
player.food = food_list
all_sprite_list.add(player)
