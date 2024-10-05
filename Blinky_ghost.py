import pygame
from Walls import*
from Player import*
from settings import*
pygame.init()

# blinky
pic = pygame.image.load('red_ghost.png')
pic = pygame.transform.scale(pic, (24, 24))  # 32x32, 8+16+8?


class Red_ghost(pygame.sprite.Sprite):

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
        self.plyr = None

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
                # self.changespeed(0, 4)
            else:
                self.rect.left = block.rect.right
                # self.changespeed(0, -4)

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            # same for up down
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                # self.changespeed(4, 0)
            else:
                self.rect.top = block.rect.bottom
                # self.changespeed(-4, 0)

        if(pygame.sprite.spritecollide(self, self.plyr, True)):
            global cur_score
            cur_score -= 100


rghost = Red_ghost(16*13, 13.5*16)
rghost.walls = wall_list
rghost.plyr = player_list
all_sprite_list.add(rghost)
