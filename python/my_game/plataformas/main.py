import pygame
import sys

from character import Character
from controles import controles_fun

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width,height))

player = Character(screen)

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            controles_fun(player,event.key)
        elif event.type == pygame.KEYUP:
            player.stop()

    screen.fill((0,100,0))

    player.update()
    player.draw()
    pygame.display.flip()        