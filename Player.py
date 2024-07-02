import pygame
from configGame import *
class Player(pygame.sprite.Sprite):
    def __init__(self, walls):
        super().__init__()
        self.image = pygame.image.load("img/players/alienBeige_badge1.png")
        self.image = pygame.transform.scale(self.image, (PLAYER_SIZE, PLAYER_SIZE))
        self.rect = self.image.get_rect()
        self.rect.center = (20, 20)
        self.walls = walls
        self.bombs = pygame.sprite.Group()
        self.countBomb = 2
        self.__hp = 3

    def setBomb(self, bomb):
        bomb_collide = pygame.sprite.spritecollide(bomb, self.bombs, False)
        if not bomb_collide:
            self.bombs.add(bomb)
            if self.countBomb >= len(self.bombs):
                all_sprites.add(bomb)
            else:
                self.bombs.remove(bomb)
    def setHp(self, hp):
        self.__hp += hp
        print("Здоровье игрока ", self.__hp)
        if self.__hp <= 0:
            print("Игра оконена")
            all_sprites.remove(self)
    def update(self, dx, dy):
        # Ограничение на диагональное перемещение
        if dx != 0 and dy != 0:
            dx = 0
            dy = 0
        new_x = self.rect.x + dx
        new_y = self.rect.y + dy
        # Проверка на выход за границы экрана
        if new_x < 0 or new_x > SCREEN_WIDTH-PLAYER_SIZE:
            new_x = self.rect.x
        if new_y < 0 or new_y > SCREEN_HEIGHT-PLAYER_SIZE:
            new_y = self.rect.y
        self.rect.x = new_x
        self.rect.y = new_y
        collided_walls = pygame.sprite.spritecollide(self, self.walls, False)
        for wall in collided_walls:
            if dx > 0:
                self.rect.right = wall.rect.left
            if dx < 0:
                self.rect.left = wall.rect.right
            if dy > 0:
                self.rect.bottom = wall.rect.top
            if dy < 0:
                self.rect.top = wall.rect.bottom
