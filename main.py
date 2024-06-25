import pygame

from Bomb import Bomb
from Player import Player
from configGame import *
from Wall import Wall
pygame.init()
backgroundImage = pygame.image.load("img/ground/ground_05.png")
backgroundWidth, backgroundHeight = backgroundImage.get_size()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

walls = pygame.sprite.Group() # Группа стен
wall1 = Wall(100,100) # Создаём стену
wall2 = Wall(400,400) # Создаём стену
walls.add(wall1, wall2)
player = Player(walls)
all_sprites.add(player, walls)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_LEFT]:
        dx = -PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        dx = PLAYER_SPEED
    if keys[pygame.K_UP]:
        dy = -PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        dy = PLAYER_SPEED
    if keys[pygame.K_SPACE]: # Если пользователь нажал "Пробел"
        bomb = Bomb(player.rect.center) # Создали бомбу
        player.setBomb(bomb) # Пробуем установить бомбу на игровом поле
    player.update(dx, dy)
    for x in range(0, SCREEN_WIDTH, backgroundWidth):
        for y in range(0, SCREEN_HEIGHT, backgroundHeight):
            screen.blit(backgroundImage, (x,y))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)