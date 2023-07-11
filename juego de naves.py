import pygame
import random
import math
import sys
import os

#arraque pygame
pygame.init()

#tamaño de pantalla
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

#rutas de recursos
def recursosPath(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

#cargar imagenes de fondo
fondo = recursosPath('recursos/imagenes/background.png')
background = pygame.image.load(fondo)

#icono ventana
iconoVentana = recursosPath('recursos/imagenes/ufo.png')
icono = pygame.image.load(iconoVentana)

#cargar sonido de fondo
sonido = recursosPath('recursos/audio/background_music.mp3')
sonidoFondo = pygame.mixer.music.load(sonido)

#jugador imagen
jugadorImagen = recursosPath("recursos/imagenes/space-invaders.png")
jugador = pygame.image.load(jugadorImagen)


#cargar bala
balaImagen = recursosPath('recursos/imagenes/bullet.png')
bala = pygame.image.load(balaImagen)

#cargar fuente para texto de fin del juego
gameOverPantalla = recursosPath('recursos/fondos/RAVIE.TTF')
gameOver = pygame.font.Font(gameOverPantalla, 60)

#cargar fuente para exto de puntaje
fuenteTexto = recursosPath('recursos/fondos/comicbd.ttf')
texto = pygame.font.Font(fuenteTexto, 32)

#establece el titulo de la ventana
pygame.display.set_caption('invasores espaciales')

#establece ventana
pygame.display.set_icon(icono)

#musica de fondo en bucle
pygame.mixer.music.play(-1)

#reloj para control de velocidad
reloj = pygame.time.Clock()

#posicion de comienzo del jugador
posicionJugadorX = 370
posicionJugadorY = 470
jugadorCambioEjeX = 0
jugadorCambioEjeY = 0

#lista de posiciones de los enemigos
navesEnemigas = []
enemigoX = []
enemigoY = []
enemigoCambioEjeX = []
enemigoCambioEjeY = []
numEnemigos = 10

#inicia las variables para guardar las posiciones de los enemigos
for i in range(numEnemigos):
    #carga las imagenes de las naves enemigas
    enemigo1 = recursosPath('recursos/imagenes/enemy1.png')
    navesEnemigas.append(pygame.image.load(enemigo1))
    enemigo2 = recursosPath('recursos/imagenes/enemy2.png')
    navesEnemigas.append(pygame.image.load(enemigo2))
    
    #se asigna lugar aleatorio de las naves enemigas ejes X y Y
    enemigoX.append(random.randint(0, 736))
    enemigoY.append(random.randint(0, 150))
    
    #establece la velocidad de movimiento de los enemigos X y Y
    enemigoCambioEjeX.append(5)
    enemigoCambioEjeY.append(20)
    
    #inicia las variables para guardar la posicion de la bala
    balaX = 0
    balaY = 480
    balaCambioEjeX = 0
    balaCambioEjeY = 10
    balaEstado = "lista"
    
    #inicia la puntuacion
    puntaje = 0
    
    #funcion para mostrar la puntuacion
    def mostrarPuntaje():
        puntajeValor = texto.render("puntaje " + str(puntaje),True,(255,255,255))
        screen.blit(puntajeValor,(10,10))
        
    #funcion para dibujar al jugador en la pantalla
    def player (x, y):
        screen.blit(jugadorImagen, (x,y))
        
    
    #funcion para dibujar naves enemigas en la pantalla
    def enemigos (x, y ,i):
        screen.blit(navesEnemigas[i],(x,y))      

    #funcion de disparo de bala
    def dispararBala(x, y):
        global balaEstado
        balaEstado = "lista"
        screen.blit(balaImagen,(x + 16 , y + 10))
    
    #funcion para comprobar colision de bala contra enemigos
    def ifColision (enemigoX, enemigoY, balaX, balaY):
        distancia = math.sqrt(math.pow(enemigoX - balaX,2) +
                              (math.pow(enemigoY - balaY, 2)))
        if distancia < 27:
            return True
        else:
            return False
    
    #funcion para mostrar texto de game over
    def gameOverTexto ():
        overTexto = texto.render("Game Over", True, (255,255,255))
        textoRect = texto.get_rect(
            center = (int(screen_width / 2), int(screen_height / 2)))
        screen.blit(overTexto, textoRect)
        
    #funcion principal del juego
    def gameloop():
        #declara variables globales
        global puntaje
        global posicionJugadorX
        global jugadorCambioEjeX
        global balaX
        global balaY
        global colision
        global balaEstado
           
        inGame = True
        while inGame:
            #maneja los eventos, actualiza,limpia la pantalla y renderiza el juego
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    inGame = False
                    pygame.quit()
                    sys.exit()
            
                #maneja los movimientos del jugador
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        jugadorCambioEjeX = -5
                    
                    if event.key == pygame.K_RIGHT:
                        jugadorCambioEjeX = 5
                    
                    if event.key == pygame.K_SPACE:
                        if balaEstado == "lista" :
                            balaX = posicionJugadorX
                            dispararBala(balaX,balaY)
                    
                    if event.type == pygame.KEYUP:
                        jugadorCambioEjeX = 0
                        
            #se actualiza la posicion del jugador
            posicionJugadorX += jugadorCambioEjeX
                    
            if posicionJugadorX <= 0:
                posicionJugadorX = 0
            elif   posicionJugadorX >= 736:
                posicionJugadorX = 736
                
            #ejecuta la actividad de las naves enemigas
            for i in range(numEnemigos):
                if enemigoY[i] >440:
                    for j in range(numEnemigos):
                        enemigoY[j] = 2000
                    gameOverTexto()
                
                enemigoX[i] += enemigoCambioEjeX[i]
                if enemigoX[i] <= 0:
                    enemigoCambioEjeX[i] = 5
                    enemigoY[i] += enemigoCambioEjeY[i]
                elif enemigoX[i] >= 736:
                    enemigoCambioEjeX[i] = -5    
                    enemigoY[i] += enemigoCambioEjeY[i]
            
                 #comprueba las coliciones de los enemigos y la bala
                colicion = ifColision(enemigoX[i], enemigoY[i], balaX, balaY)
                if colicion:
                    balaY = 454
                    balaEstado = "lista"
                    puntaje += 1
                    enemigoX[i] = random.randint(0,736)
                    enemigoY[i] = random.randint(0, 150)
                enemigos(enemigoX[i],enemigoY[i],i)
                
            if balaY < 0:
                balaY = 454
                balaEstado = "lista"
            if balaEstado == "fuego":
                dispararBala (balaX, balaY)
                balaY -= balaCambioEjeY
                
            #player(posicionJugadorX,posicionJugadorY)
            mostrarPuntaje()
            pygame.display.update()
            
            reloj.tick(120)
gameloop()                