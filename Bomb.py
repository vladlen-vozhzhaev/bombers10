import pygame
from configGame import *

class Bomb(pygame.sprite.Sprite):
    def __init__(self, place):
        super().__init__()
        self.image = pygame.Surface((BLOCK_SIZE,BLOCK_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        y = (place[1] + (BLOCK_SIZE - place[1]%BLOCK_SIZE))-BLOCK_SIZE/2
        x = (place[0] + (BLOCK_SIZE - place[0]%BLOCK_SIZE))-BLOCK_SIZE/2
        self.rect.center = (x, y)
        self.start_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time > 3000:
            print("Boom!")