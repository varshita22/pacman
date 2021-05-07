import pygame
from Walls import*
from Player import*
pygame.init()

# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

food_pic = pygame.image.load('white16.png')
food_pic = pygame.transform.scale(food_pic, (6, 6))


# Food Class


class Food(pygame.sprite.Sprite):

    def __init__(self, x, y):

        # Call the parent's constructor
        super().__init__()

        self.image = food_pic

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y+5
        self.rect.x = x+5


food_list = pygame.sprite.Group()


def d_food(xs, ys, xe, ye):  # draws a line of food
    if(xs == xe):
        for i in range(ys, ye+1, 16):  # 16
            food = Food(xs, i)
            food_list.add(food)
            all_sprite_list.add(food)
    if(ys == ye):
        for i in range(xs, xe+1, 16):  # 16
            food = Food(i, ys)
            food_list.add(food)
            all_sprite_list.add(food)


d_food(16, 16*4, 16, 16*11)  # leftmost vert line
d_food(16*26, 16*4, 16*26, 16*11)  # rightmost vert line
d_food(16, 16*11, 16*6, 16*11)
d_food(16*22, 16*11, 16*25, 16*11)  # smol sleeping line bottom-top
d_food(16, 16*8, 16*25, 16*8)  # top long horizontal line
d_food(16, 16*32, 16*26, 16*32)  # bottom long horizontal line
d_food(16*6, 16*4, 16*6, 16*29)  # left long vertical line
d_food(16*21, 16*4, 16*21, 16*29)  # right long vertical line
d_food(16, 16*4, 16*12, 16*4)  # topmost line1
d_food(16*15, 16*4, 16*25, 16*4)  # topmostline2
d_food(16*12, 16*5, 16*12, 16*7)  # topmost line1,vertical smol
d_food(16*15, 16*5, 16*15, 16*7)  # topmost line2,vertical smol
d_food(16*9, 16*9, 16*9, 16*11)  # line1,vertical smol,L
d_food(16*18, 16*9, 16*18, 16*11)  # line1,vertical smol,L
d_food(16*10, 16*11, 16*12, 16*11)  # topmost line1,hori smol,L
d_food(16*15, 16*11, 16*17, 16*11)  # topmost line1,hori smol,L

## end of top food##
