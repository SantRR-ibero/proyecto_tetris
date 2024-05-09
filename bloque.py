from colores import Colores
from posicion import Posicion
import pygame

class Bloque:
    def __init__(self, pr_id):
        self.id              = pr_id
        self.celdas          = {}
        self.cell_size       = 30
        self.fila_desfase    = 0
        self.columna_desfase = 0
        self.estado_rotacion = 0
        self.colores         = Colores.get_lista_colores()
        return

    def mover(self, filas, columnas):
        self.fila_desfase    += filas
        self.columna_desfase += columnas
        return

    def get_posicion_celda(self):
        losas = self.celdas[self.estado_rotacion]
        losas_desplazadas = []
        for posicion in losas:
            posicion = Posicion(posicion.fila + self.fila_desfase, posicion.columna + self.columna_desfase)
            losas_desplazadas.append(posicion)
        return losas_desplazadas
    
    def rotar(self):
        self.estado_rotacion += 1
        if self.estado_rotacion == 4:
            self.estado_rotacion = 0
        return
    
    def deshacer_rotar(self):
        self.estado_rotacion -= 1
        if self.estado_rotacion == -1:
            self.estado_rotacion = len(self.celdas) - 1
        return

    def dibuja(self, screen):
        losas = self.get_posicion_celda()
        for losa in losas:
            rectangulo_losa = pygame.Rect(losa.columna * self.cell_size + 11, losa.fila * self.cell_size + 11, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colores[self.id], rectangulo_losa)
        return
