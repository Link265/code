import pygame

# Inicializa Pygame
pygame.init()

# Define los colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Define las dimensiones de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# Crea la pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

# Define la clase del jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 500
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.gravedad = 0.5

    def update(self):
        # Actualiza la posición del jugador en función de la velocidad
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Aplica la gravedad al jugador
        self.velocidad_y += self.gravedad

        # Verifica si el jugador ha llegado al suelo
        if self.rect.y >= 500:
            self.rect.y = 500
            self.velocidad_y = 0

        # Verifica si el jugador ha alcanzado el límite superior de la pantalla
        if self.rect.y <= 0:
            self.rect.y = 0
            self.velocidad_y = 0

    def saltar(self):
        # Verifica si el jugador está en el suelo
        if self.rect.y == 500:
            self.velocidad_y = -10

    def mover_izquierda(self):
        self.velocidad_x = -5

    def mover_derecha(self):
        self.velocidad_x = 5

    def detener(self):
        self.velocidad_x = 0

# Crea todos los sprites
todos_los_sprites = pygame.sprite.Group()
jugador = Jugador()
todos_los_sprites.add(jugador)

# Define el bucle principal del juego
hecho = False
reloj = pygame.time.Clock()
while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador.mover_izquierda()
            elif evento.key == pygame.K_RIGHT:
                jugador.mover_derecha()
            elif evento.key == pygame.K_SPACE:
                jugador.saltar()
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT and jugador.velocidad_x < 0:
                jugador.detener()
            elif evento.key == pygame.K_RIGHT and jugador.velocidad_x > 0:
                jugador.detener()

    # Actualiza todos los sprites
    todos_los_sprites.update()

    # Dibuja todos los sprites
    pantalla.fill(NEGRO)
    todos_los_sprites.draw(pantalla)

    # Actualiza la pantalla
    pygame.display.flip()

    # Limita el juego a 60 fotogramas por segundo
    reloj.tick(60)

# Cierra Pygame
pygame.quit()