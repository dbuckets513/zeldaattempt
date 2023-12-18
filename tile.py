import pygame
from settings import *

class Tile(pygame.sprite.Sprite): # need sprite.Spirte for inheritance
    def __init__(self,pos, groups,sprite_type,surface = pygame.Surface(TILESIZE,TILESIZE)): # the group sprites should be apart of via as a arguement
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        self.rect = self.image.get_rect(topleft = pos)
        #inflate takes a rectangle and changes the size, so original rectangle, and hit box would have the same width and height but it is just shorter and so player can be tanding behind it
        self.hitbox = self.rect.inflate(0,-10) #(x = 0, y= -10) #- 10 takes away 5 megapixel from top and bottom


        #self.image creates the image, self.rect actually creates a thing
        #hitbox,
