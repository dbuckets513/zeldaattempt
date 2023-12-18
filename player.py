import pygame
from settings import settings

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -26)
# how does player move, after we creataed him? the code below
        # math.Vector2 gives us a x and y value controller for our player and his player speed so vector x speed for player speed
        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites
        #keyboard input
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        # need y = 0 so the player can come to a stop after one press on keyboard
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    # this move block works for all players and enemies
    def move(self,speed):#move method for player and other units
        #the if statement brings diagonal speed to match up/down/right/left
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize() # changes the length of a vector to one, because when you diagonal scroll it is faster speed
        # each movement for x and y
        self.hitbox.x +=  self.direction.x * speed
        self.hitbox.y += self.direction.y * speed
        #creates collisions with the walls of the blank screen
        self.collision('horizontal')
        self.collision('vertical')
        self.rect.center = self.hitbox.center

        self.rect.center += self.direction * speed

    def collision(self,direction): # our player object collisions
        #OVERLAPPING sprites is what we need to address, what do we need to do?
        # we have to apply each direction indivdidually, if there is any collision from any direction our game wont crash! instead we adress the problem
        if direction == 'horizontal': # we are gonna check all sprites in all obstacle sprites,
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: #moving right
                        self.hitbox.right = sprite.hitbox.left #our player is moving right and collides with some obstacle
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right #for horiztonal collisions
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                    if sprite.rect.colliderect(self.rect):
                        if self.direction.y > 0:  # MOVING DOWN
                            self.rect.bottom = sprite.rect.top  # our player is moving right and collides with some obstacle
                        if self.direction.y < 0:#moving up
                            self.rect.top = sprite.rect.bottom



    def update(self):
        self.input()
        self.move(self.speed)
