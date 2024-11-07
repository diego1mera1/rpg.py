import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla y el juego
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Territorios Inexplorados - RPG")

# Configuración del mapa
MAP_WIDTH, MAP_HEIGHT = 1600, 1200  # Tamaño del mundo, más grande que la pantalla
background = pygame.Surface((MAP_WIDTH, MAP_HEIGHT))
background.fill((34, 139, 34))  # Fondo verde para simular hierba

# Cargar la imagen del tronco
tronco = pygame.image.load("images/tronco1.png").convert_alpha()
tronco_rect = tronco.get_rect(topleft=(300, 300))  # Posición del tronco en el mapa

# Configuración del personaje
player = pygame.Surface((40, 40))  # Un simple cuadrado como personaje
player.fill((0, 0, 255))
player_rect = player.get_rect()

# Posición inicial del jugador en el mapa
player_x, player_y = MAP_WIDTH // 2, MAP_HEIGHT // 2
speed = 5

# Variables para el desplazamiento de la cámara
camera_x, camera_y = 0, 0

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Copia de la posición del jugador
    new_player_x, new_player_y = player_x, player_y

    # Obtener teclas presionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        new_player_x -= speed
    if keys[pygame.K_RIGHT]:
        new_player_x += speed
    if keys[pygame.K_UP]:
        new_player_y -= speed
    if keys[pygame.K_DOWN]:
        new_player_y += speed

    # Crear un nuevo rectángulo del jugador con la nueva posición
    new_player_rect = pygame.Rect(new_player_x, new_player_y, player_rect.width, player_rect.height)

    # Verificar colisión con el tronco
    if not new_player_rect.colliderect(tronco_rect):
        # Si no hay colisión, actualizar la posición del jugador
        player_x, player_y = new_player_x, new_player_y

    # Limitar el movimiento del jugador al tamaño del mapa
    player_x = max(0, min(player_x, MAP_WIDTH - player_rect.width))
    player_y = max(0, min(player_y, MAP_HEIGHT - player_rect.height))

    # Actualizar la posición de la cámara para que siga al jugador
    camera_x = max(0, min(player_x - SCREEN_WIDTH // 2, MAP_WIDTH - SCREEN_WIDTH))
    camera_y = max(0, min(player_y - SCREEN_HEIGHT // 2, MAP_HEIGHT - SCREEN_HEIGHT))

    # Dibujar el fondo, tronco y el jugador en la posición de la cámara
    screen.blit(background, (-camera_x, -camera_y))
    screen.blit(tronco, (tronco_rect.x - camera_x, tronco_rect.y - camera_y))
    screen.blit(player, (player_x - camera_x, player_y - camera_y))

    # Actualizar la pantalla
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
