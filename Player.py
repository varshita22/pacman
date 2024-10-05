import pygame
from Walls import*
from Food import*
from settings import*
pygame.init()

# player

pic = pygame.image.load('pac32.png')
pic = pygame.transform.scale(pic, (24, 24))  # 32x32, 8+16+8?


def draw_score(words, scr, screen, pos, size, colour, font_name):
    font = pygame.font.SysFont(font_name, size)
    text = font.render(words+str(scr), False, colour)
    text_size = text.get_size()
    screen.blit(text, pos)


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

        if(pygame.sprite.spritecollide(self, self.food, True)):
            global cur_score
            cur_score += 10

        return cur_score


player_list = pygame.sprite.Group()
player = Player(8, 56)
player.walls = wall_list
player.food = food_list
player_list.add(player)
all_sprite_list.add(player)
