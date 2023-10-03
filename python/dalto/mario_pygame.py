import pygame

# Inicializa Pygame
pygame.init()

# Define los colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (50,200,50)

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
        self.suelo = False

    def update(self):
        if self.rect.y == 400:
            self.suelo = True

        if self.rect.y == 500:
            self.suelo = False

        if self.suelo:
            self.rect.y -= self.velocidad_y
        else:    
            self.rect.y += self.velocidad_y

        self.rect.x += self.velocidad_x




    def saltar(self):
        self.velocidad_y = -10


    def mover_izquierda(self):
        self.velocidad_x = -5

    def mover_derecha(self):
        self.velocidad_x = 5

    def detener(self):
        self.velocidad_x = 0

# Define la clase de la moneda
class Moneda(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Crea todos los sprites
todos_los_sprites = pygame.sprite.Group()
jugador = Jugador()
todos_los_sprites.add(jugador)
monedas = pygame.sprite.Group()
for i in range(10):
    moneda = Moneda(i * 70 + 100, 400)
    monedas.add(moneda)
    todos_los_sprites.add(moneda)

# Define el bucle principal del juego
hecho = False
reloj = pygame.time.Clock()
puntuacion = 0
while not hecho:

    pantalla.fill(VERDE)

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

    # Verifica si el jugador ha recolectado una moneda
    monedas_recolectadas = pygame.sprite.spritecollide(jugador, monedas, True)
    puntuacion += len(monedas_recolectadas)

    # Dibuja todos los sprites
    pantalla.fill(NEGRO)
    todos_los_sprites.draw(pantalla)

    # Dibuja la puntuación
    fuente = pygame.font.Font(None, 36)
    texto_puntuacion = fuente.render("Puntuación: " + str(puntuacion), True, BLANCO)
    pantalla.blit(texto_puntuacion, [10, 10])

    # Actualiza la pantalla
    pygame.display.flip()

    # Limita el juego a 60 fotogramas por segundo
    reloj.tick(60)

# Cierra Pygame
pygame.quit()