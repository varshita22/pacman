import pygame
pygame.init()

# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

# Wall Class


class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):

        # Call the parent's constructor
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

# wall list


wall_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()  # all sprite lists

wall = Wall(0, 24, 6, 80)  # left most wall
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(790, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 590, 800, 10)
wall_list.add(wall)
all_sprite_list.add(wall)  # end of 4 boundary walls

wall = Wall(42, 42, 10, 126)  # middle vertical
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(42, 242, 10, 348)  # middle vertical
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 200, 42, 10)  # small horizontal
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(758, 200, 42, 10)  # small horizontal
wall_list.add(wall)
all_sprite_list.add(wall)
