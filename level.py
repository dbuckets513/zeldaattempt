import pygame
from settings import *
from tile import Tile
from player import Player
from support import *
class Level:
    def __init__(self):

        #get the display surface
        self.display_surface = pygame.display.get_surface()

        #sprite group setup
        self.visible_sprites = YSortCameraGroup()

        self.obstacles_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self): #for each row i need to know the index so i need to get the y mehtod by using the enumerate method
        layout = {
            'boundary': import_csv_layout('../map/map_FloorBlocks.csv')
        }
        for style_layout in layouts.items():
            for row_index, row in enumerate(layout):
            # y value of map cordinates
            #   by using the instance below, you get the x value and y value for every position in the map, it names what each space has in it and where.
                for col_index, col in enumerate(row):
                    if col != '-1': #empty space tile
                    x = col_index * TILESIZE
                    y = row_index * TILESIZE
                    if style == 'boundary':
                        Tile((x,y),[self.visible_sprites,self.obstacles_sprites],'invisible')
                    if col == 'x': #now we got the value of each space, we can actually write out the code for what x and y should be
                        Tile((x,y)), [self.visible_sprites, self.obstacles_sprites]
                    if col == 'p':
                        self.player = Player((2000,1430 ),[self.visible_sprites],self.obstacle_sprites)



    def run(self):
        #update and draw the game, after knowing what each value is, we have to draw it here
            self.visible_sprites.custom_draw(self.player)
            self.visible_sprites.update()
# for sprite in sprites or sprite.update
class YSortCameraGroup(pygame.sprite.Group): #how the camera keeps the player in the middle of the screen at all times
    def __init__(self):
        #general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        #below is how you get the camera to keep character in the middle of the window
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2() #creates the offset of the camera position to the player
            # creating the floor
            self.floor_surface = pygame.image.load('').convert()
            self.floot_react = self.floor_surf.get_rect(topleft - (0,0))
    def custom_draw(self, player):
        #camera and player position/ getting offset
        self.offset.x = player.rect_center - self.half_width
        self.offset.y = player.rect_center - self.half_height


        # drawing the floor

        floor_offset_pos = self.floor_rect.topleft - self.offset

        #for sprite in self.sprites(): #draw elements from here on out
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery)
            offset_pos = sprite.rect.topleft + self.offset
            self.display_surface.blit(sprite.image,offset_pos)
