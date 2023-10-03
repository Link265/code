#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 14:00:05 2023

@author: Link
"""

import pygame

# Inicializar Pygame
pygame.init()

# Configurar la ventana
ancho = 640
alto = 480
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("juego")

# Configurar el círculo
x = ancho // 2
y = alto // 2
radio = 50
color = (255, 0, 0)

# Ciclo principal del juego
while True:
    # Manejar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif evento.type == pygame.KEYDOWN:
            print(evento.key)
        elif evento.type == pygame.KEYUP:
            print(evento.key)     
    
    
    # pitando el fondo de la ventana de color gris
    ventana.fill((100, 100, 100))
    
    # Dibujar el círculo en la ventana
    
    pygame.draw.circle(ventana, color, (x, y), radio)
    
    # dibujando cuadrados
    pygame.draw.rect(ventana,color,(2,2,20,20))
    pygame.draw.rect(ventana,(100,100,200),(300,50,100,100))

    # Actualizar la pantalla
    pygame.display.update()