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


wall_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()  # all sprite lists

wall = Wall(0, 48, 8, 160)  # left most wall
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(440, 48, 8, 160)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 48, 448, 8)  # top most
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(13.5*16, 48, 16, 72)  # middle vertical
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(40, 88, 48, 32)  # first top-left rect
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(16*7.5, 88, 16*4, 32)  # rect
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(16.5 * 16, 88, 4*16, 32)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(22.5*16, 88, 48, 32)  # end of top 4 rects
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(40, 9.5*16, 48, 16)  # 2 horizontal lines
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(22.5*16, 9.5*16, 3*16, 16)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(7.5*16, 9.5*16, 16, 16*7)  # left T
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(8.5*16, 12.5*16, 3*16, 16)  # left T
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10.5*16, 9.5*16, 16*7, 16)  # middle T
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(13.5*16, 10.5*16, 16, 3*16)  # middle T
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(19.5*16, 9.5*16, 16, 16*7)  # right T
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(16.5*16, 12.5*16, 16*3, 16)  # right T
wall_list.add(wall)
all_sprite_list.add(wall)
