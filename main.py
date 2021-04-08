import pygame
# initialize the pygame
pygame.init()
# screen of w=800,h=600
screen = pygame.display.set_mode((800, 600))  # 2 brackets

# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

# title and icon
pygame.display.set_caption("Pacman")
icon = pygame.image.load('pac32.png')
pygame.display.set_icon(icon)

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

wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 200, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(690, 200, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(790, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 590, 800, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

# player


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
        self.image = pygame.image.load('pac32.png')
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

       # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None

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


player = Player(50, 50)
player.walls = wall_list

all_sprite_list.add(player)

#playerImg = pygame.image.load('pac32.png')
# playerx = 370  # consider size of image also to display midway(half of 800)
#playery = 480
#playerx_change = 0
#playery_change = 0


# def player(x, y):
#   screen.blit(playerImg, (x, y))  # to draw it on screen


# game loop, anything that has to be visible inside
# game window has to go inside while loop

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)  # 3 values of RGB, teal
    # playerx += .05  # everytime while loop executes, moves .05 right
    # screen.blit(background, (0, 0)) # img as backgroung
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if key stroke is left , right, up or down
        if event.type == pygame.KEYDOWN:  # pressing button
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            if event.key == pygame.K_UP:
                player.changespeed(0, -3)
            if event.key == pygame.K_DOWN:
                player.changespeed(0, 3)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

    all_sprite_list.draw(screen)

    # if playerx <= 0:
    #     playerx = 0
    # elif playerx >= 528:  # 560-32
    #     playerx = 528

    # if playery <= 0:
    #     playery = 0
    # elif playery >= 588:  # 620-32
    #     playery = 588

    all_sprite_list.update()
    # player(playerx, playery)  # draw img above backgroung
    pygame.display.update()
    clock.tick(80)
