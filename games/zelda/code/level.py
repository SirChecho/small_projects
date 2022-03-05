import pygame
from settings import *
from tile import Tile
from player import Player
class Level:
    def __init__(self):
        #get the display surface
        self.display_surface = pygame.display.get_surface()

        #sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        #sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    #Tile is part of visible and obstacle sprites
                    #when the player colides with obstacles it should interact
                    Tile((x,y),[self.visible_sprites,self.obstacles_sprites])

                if col == 'p':
                    Player((x,y),[self.visible_sprites])



    def run(self):
        self.visible_sprites.draw(self.display_surface)