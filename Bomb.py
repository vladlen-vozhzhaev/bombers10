import pygame

import Box
import Wall
from configGame import *

class Bomb(pygame.sprite.Sprite):
    def __init__(self, place):
        super().__init__()
        self.image = pygame.Surface((BLOCK_SIZE,BLOCK_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.y = (place[1] + (BLOCK_SIZE - place[1]%BLOCK_SIZE))-BLOCK_SIZE/2
        self.x = (place[0] + (BLOCK_SIZE - place[0]%BLOCK_SIZE))-BLOCK_SIZE/2
        self.rect.center = (self.x, self.y)
        self.start_time = pygame.time.get_ticks()
        self.explodeX = pygame.sprite.Sprite()
        self.explodeY = pygame.sprite.Sprite()
        self.exploded = False
        self.explodeRender = True
        self.radius = 4

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time > 3000 and not self.exploded:
            self.explodeX.image = pygame.Surface((BLOCK_SIZE+BLOCK_SIZE*self.radius, BLOCK_SIZE))
            self.explodeY.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE+BLOCK_SIZE*self.radius))
            self.explodeX.image.fill(RED)
            self.explodeY.image.fill(RED)
            self.explodeX.rect = self.explodeX.image.get_rect()
            self.explodeY.rect = self.explodeY.image.get_rect()
            self.explodeX.rect.center = self.rect.center
            self.explodeY.rect.center = self.rect.center
            x_collide = pygame.sprite.spritecollide(self.explodeX, all_sprites, False)
            y_collide = pygame.sprite.spritecollide(self.explodeY, all_sprites, False)
            all_sprites.remove(self)
            for sprite in x_collide:
                if sprite.__class__ == Wall.Wall:
                    print(sprite.rect.left == self.explodeX.rect.right - BLOCK_SIZE*self.radius/2)
                    if sprite.rect.left == self.explodeX.rect.right - BLOCK_SIZE*self.radius/2:
                        self.explodeX.image = pygame.transform.scale(self.explodeX.image, (BLOCK_SIZE + BLOCK_SIZE * self.radius / 2, BLOCK_SIZE))



            all_sprites.add(self.explodeX)
            x_collide = pygame.sprite.spritecollide(self.explodeX, all_sprites, False)
            y_collide = pygame.sprite.spritecollide(self.explodeY, all_sprites, False)
            for sprite in x_collide:
                if sprite.__class__ == Box.Box:
                    all_sprites.remove(sprite)
                    walls.remove(sprite)
            for sprite in y_collide:
                if sprite.__class__ == Box.Box:
                    all_sprites.remove(sprite)
                    walls.remove(sprite)
            self.exploded = True
        elif current_time - self.start_time > 3500 and self.explodeRender:
            all_sprites.remove(self.explodeX, self.explodeY)
            self.explodeRender = False
