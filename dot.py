import pygame
import pygame.gfxdraw
from pygame.locals import ( K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT)
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Player, self).__init__()
        self.surf = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.gfxdraw.aacircle(self.surf, 15, 15, 14, (255, 255, 255))
        pygame.gfxdraw.filled_circle(self.surf, 15, 15, 14, (255, 255, 255))
        self.rect = self.surf.get_rect()

        #Make top-left corner the passed-in location
        self.rect.y = y
        self.rect.x = x

        #set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def changespeed(self,x,y):
        self.change_x += x
        self.change_y += y

    def move(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)



    #To find the new position of player
    def update(self, walls):
        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self,walls, False)
        for block in block_hit_list:
            #If we are moving right, set our right side to the left side of the item we hit
            if self.change_x >0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self,walls, False)
        for block in block_hit_list:
            #if we are moving upwards then our top is set to the bottom of the block
            if self.change_y > 0:
                self.rect.top = block.rect.bottom
            else:
                self.rect.bottom = block.rect.top

#creating a wall class which is a simple sprite
class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)

        #make a blue wall with specified size
        self.surf = pygame.Surface((width,height))
        self.surf.fill((50,50,255))

        #make our top-left corner the passed-in location
        self.rect = self.surf.get_rect()
        self.rect.y = y
        self.rect.x = x



#circleRect = pygame.draw.circle(screen, (255, 255, 255), (400,300), 5)

#list to hold all sprites
all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

#1st wall
wall = Wall(0,0,10,600)
wall_list.add(wall)
all_sprite_list.add(wall)

#2nd wall
wall = Wall(10,0,790,10)
wall_list.add(wall)
all_sprite_list.add(wall)

#3rd wall
wall = Wall(0,590,800,10)
wall_list.add(wall)
all_sprite_list.add(wall)

#4th wall
wall = Wall(790,0,10,600)
wall_list.add(wall)
all_sprite_list.add(wall)



player = Player(50,50)
all_sprite_list.add(player)

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.type == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player.move(pressed_keys)

    #To make sure that player doesnt run into walls
    player.update(wall_list)
    #for w in wall_list:
    #    player.update(w)


    screen.fill((0,0,0))
    for entity in all_sprite_list:
        screen.blit(entity.surf,entity.rect)

    pygame.display.flip()

    clock = pygame.time.Clock()
    clock.tick(40)
