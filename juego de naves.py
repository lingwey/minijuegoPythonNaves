import pygame
import random
import math
import sys
import os

#arraque pygame
pygame.init()

#tamaño de pantalla
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

#rutas de recursos
def recursosPath(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

#cargar imagenes de fondo
fondo = recursosPath('imagenes/background.png')
background = pygame.image.load(fondo)

#icono ventana
iconoVentana = recursosPath('imagenes/ufo.png')
icono = pygame.image.load(iconoVentana)

#reproduce sonido de fondo en bucle
sonido = recursosPath('audio/background_music.mp3')
sonidoFondo = pygame.mixer.music.load(sonido)

#jugador imagen
jugador = recursosPath('imagenes/s')

#reloj para control de velocidad
reloj = pygame.time.Clock()

#posicion de comienzo del jugador
posicionJugadorX = 370
posicionJugadorY = 470
jugadorCambioEjeX = 0
jugadorCambioEjeY = 0

#lista de enemigos
navesEnemigas = []
enemigoX = []
enemigoY = []
enemigoCambioEjeX = []
enemigoCambioEjeY = []
numEnemigos = 10

#inicia las variables para guardar las posiciones de los enemigos
for i in range(numEnemigos):
    #carga las imagenes de las naves enemigas
    enemigo1 = recursosPath('imagenes/enemy1.png')
    navesEnemigas.append(pygame.image.load(enemigo1))
    enemigo2 = recursosPath('imagenes/enemy2.png')
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
    balaEstado = "ready"
    
    #inicia la puntuacion
    puntaje = 0
    
    #funcion para mostrar la puntuacion
    def mostrarPuntaje():
        puntajeValor = font.render("puntaje " + str(puntaje),True,(255,255,255))
        screen.blit(puntajeValor,(10,10))    
