import pygame
import sys

pygame.init()

BLUE = (0,0,150)
BLACK = (0,0,0)
YELLOW = (150,100,10)

width = 700
height = 700

window = pygame.display.set_mode((700,700))

def draw_cartesian_plane(grosor):
    # eje y
    pygame.draw.rect(window,BLUE,(width/2 - grosor,0,grosor,height))

    # eje x
    pygame.draw.rect(window,BLUE,(0,height/2 - grosor,width,grosor))

    


while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    window.fill((0,100,10))
    draw_cartesian_plane(10)

    pygame.display.update()