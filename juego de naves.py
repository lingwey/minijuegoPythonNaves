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