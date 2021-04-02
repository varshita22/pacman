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

# backgroung

# background = pygame.image.load('Originalpacmaze.png')
# background = pygame.transform.scale(background, (560, 620))

# Wall Class


class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """

    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
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

wall = Wall(0, 0, 10, 600)
wall_list.add(wall)

wall = Wall(10, 0, 790, 10)
wall_list.add(wall)

wall = Wall(10, 200, 100, 10)
wall_list.add(wall)

wall = Wall(690, 200, 100, 10)
wall_list.add(wall)

wall = Wall(790, 0, 10, 600)
wall_list.add(wall)

wall = Wall(0, 590, 800, 10)
wall_list.add(wall)

# player

playerImg = pygame.image.load('pac32.png')
playerx = 370  # consider size of image also to display midway(half of 800)
playery = 480

playerx_change = 0
playery_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))  # to draw it on screen


# game loop, anything that has to be visible inside
# game window has to go inside while loop
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
                playerx_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.3
            if event.key == pygame.K_UP:
                playery_change = -0.3
            if event.key == pygame.K_DOWN:
                playery_change = 0.3

        if event.type == pygame.KEYUP:  # release button
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerx_change = 0
                playery_change = 0

    playerx += playerx_change
    playery += playery_change

    wall_list.draw(screen)

    if playerx <= 0:
        playerx = 0
    elif playerx >= 528:  # 560-32
        playerx = 528

    if playery <= 0:
        playery = 0
    elif playery >= 588:  # 620-32
        playery = 588

    player(playerx, playery)  # draw img above backgroung
    pygame.display.update()
