import pygame
import sys

# Inicializa Pygame
pygame.init()
pygame.mixer.init()

# Carga y redimensiona las imagens de fondo
fondo = pygame.image.load('images/grass.png')
flowers = pygame.image.load('images/arbusto1.png')
cartel = pygame.image.load('images/cartel.png')
tronco1 = pygame.image.load('images/tronco1.png')
tronco2 = pygame.image.load('images/tronco2.png')
fondo = pygame.transform.scale(fondo, (1500, 1000))  # Redimensiona la imagen al tamaño de la pantalla

# Define constantes
ANCHO = 800
ALTO = 600
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS = (50, 50, 50)

# Configura la ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Menú Mejorado')

# Fuentes
fuente = pygame.font.SysFont(None, 55)
fuente_titulo = pygame.font.SysFont(None, 80)  # Fuente más grande para el título

# Tamaño de botones
ANCHO_BOTON = 300
ALTO_BOTON = 60

# Volumen inicial
volumen = 0.5
pygame.mixer.music.set_volume(volumen)  # Ajusta el volumen inicial

# Función para dibujar texto
def dibujar_texto(texto, color, superficie, x, y, fuente_usada=fuente):
    texto_surf = fuente_usada.render(texto, True, color)
    texto_rect = texto_surf.get_rect(center=(x, y))
    superficie.blit(texto_surf, texto_rect)

# Función para crear botones con bordes redondeados
def crear_botones(opciones, seleccion):
    botones = {}
    for i, opcion in enumerate(opciones):
        # Determina colores
        color_fondo = BLANCO if i == seleccion else GRIS
        color_texto = NEGRO if i == seleccion else BLANCO
        y_pos = 200 + i * (ALTO_BOTON + 10)

        # Dibuja un rectángulo redondeado
        boton_rect = pygame.Rect(250, y_pos, ANCHO_BOTON, ALTO_BOTON)
        pygame.draw.rect(pantalla, color_fondo, boton_rect, border_radius=10)

        # Dibuja el texto del botón
        dibujar_texto(opcion, color_texto, pantalla, 250 + ANCHO_BOTON // 2, y_pos + ALTO_BOTON // 2)
        botones[opcion] = boton_rect

    return botones

# Función para el menú principal
def menu():
    reloj = pygame.time.Clock()
    opciones = ['Iniciar', 'Configuración', 'Salir']
    seleccion = 0

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(opciones)
                elif evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(opciones)
                elif evento.key == pygame.K_RETURN:
                    if opciones[seleccion] == 'Iniciar':
                        pass  # Aquí puedes agregar el código para iniciar el juego
                    elif opciones[seleccion] == 'Salir':
                        pygame.quit()
                        sys.exit()
                    elif opciones[seleccion] == 'Configuración':
                        configuracion()

        # Dibuja la imagen de fondo
        pantalla.blit(fondo, (-390, -300))

        # Dibuja tres arbustos en diferentes posiciones
        pantalla.blit(flowers, (0, 10))   # Primer arbusto
        pantalla.blit(flowers, (300, 400))  # Segundo arbusto
        pantalla.blit(flowers, (400, 0))  # Tercer arbusto
        pantalla.blit(flowers, (-200, 350))  # Cuarto arbusto
        
        # Dibuja un cartel
        pantalla.blit(cartel, (-70, 150))

        #dibuja tronco
        pantalla.blit(tronco1,(-200,50 ))
        pantalla.blit(tronco1,(400,400 ))
        pantalla.blit(tronco1,(200,100 ))
        pantalla.blit(tronco2,(-100,400 ))

        # Dibuja el título
        dibujar_texto("The RPG Game", NEGRO, pantalla, ANCHO // 2, 100, fuente_titulo)

        # Dibuja los botones
        crear_botones(opciones, seleccion)

        pygame.display.flip()
        reloj.tick(30)

# Función para la pantalla de configuración
def configuracion():
    seleccion = 0

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % 2
                elif evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % 2
                elif evento.key == pygame.K_RETURN:
                    if seleccion == 0:  # Botón "Volumen"
                        ajuste_volumen()
                    elif seleccion == 1:  # Botón "Volver"
                        return

        pantalla.fill(NEGRO)
        crear_botones_config(seleccion)
        pygame.display.flip()

# Función para crear botones en configuración
def crear_botones_config(seleccion):
    opciones = ['Volumen', 'Volver']
            # Dibuja la imagen de fondo
    pantalla.blit(fondo, (-390, -300))

    # Dibuja tres arbustos en diferentes posiciones
    pantalla.blit(flowers, (0, 10))   # Primer arbusto
    pantalla.blit(flowers, (300, 400))  # Segundo arbusto
    pantalla.blit(flowers, (400, 0))  # Tercer arbusto
    pantalla.blit(flowers, (-200, 350))  # Cuarto arbusto
    
    # Dibuja un cartel
    pantalla.blit(cartel, (-70, 150))

    #dibuja tronco
    pantalla.blit(tronco1,(-200,50 ))
    pantalla.blit(tronco1,(400,400 ))
    pantalla.blit(tronco1,(200,100 ))
    pantalla.blit(tronco2,(-100,400 ))

    return crear_botones(opciones, seleccion)

# Función para ajustar el volumen
def ajuste_volumen():
    global volumen
    seleccion = 0
    ajustes = ['Subir', 'Bajar', 'Volver']

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(ajustes)
                elif evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(ajustes)
                elif evento.key == pygame.K_RETURN:
                    if seleccion == 0:  # Botón "Subir"
                        volumen = min(volumen + 0.1, 1.0)
                    elif seleccion == 1:  # Botón "Bajar"
                        volumen = max(volumen - 0.1, 0.0)
                    pygame.mixer.music.set_volume(volumen)
                    if seleccion == 2:  # Botón "Volver"
                        return

        pantalla.fill(NEGRO)
        crear_botones_ajuste_volumen(seleccion)
        dibujar_texto(f'Volumen: {int(volumen * 100)}%', BLANCO, pantalla, ANCHO // 2, 100)
        pygame.display.flip()

# Función para crear botones de ajuste de volumen
def crear_botones_ajuste_volumen(seleccion):
    opciones = ['Subir', 'Bajar', 'Volver']
    return crear_botones(opciones, seleccion)

# Llama a la función del menú
menu()
