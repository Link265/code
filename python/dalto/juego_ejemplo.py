import pygame
import sys

pygame.init()

ventana = pygame.display.set_mode((800, 600))

x = 0
y = 0

while True:
    # Procesar eventos del usuario
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtener estado de las teclas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= 1
    if teclas[pygame.K_RIGHT]:
        x += 1
    if teclas[pygame.K_UP]:
        y -= 1
    if teclas[pygame.K_DOWN]:
        y += 1

    ventana.fill((0,0,0))

    # Dibujar objeto en la pantalla
    objeto = pygame.Rect(x, y, 50, 50)
    pygame.draw.rect(ventana, (255, 0, 0), objeto)

    # Actualizar pantalla
    pygame.display.update()