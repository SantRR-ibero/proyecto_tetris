import pygame
from colores import Colores

class Grid:
    def __init__(self):
        self.numero_filas    = 20
        self.numero_columnas = 10
        self.size_celda      = 30
        self.grid            = [[0 for j in range(self.numero_columnas)] for i in range(self.numero_filas)]
        self.colores         = Colores.get_color_celda()
        return

    def esta_dentro(self, fila, columna):
        if fila >= 0 and fila < self.numero_filas and columna >= 0 and columna < self.numero_columnas:
            return True
        return False
    
    def esta_vacio(self, fila, columna):
        if self.grid[fila][columna] == 0:
            return True
        return False
    
    def esta_fila_completa(self, fila):
        for columna in range(self.numero_columnas):
            if self.grid[fila][columna] == 0:
                return False
        return True
    
    def limpia_fila(self, fila):
        for columna in range(self.numero_columnas):
            self.grid[fila][columna] = 0
        return
        
    def mover_fila_abajo(self, fila, numero_filas_desplazar):
        for column in range(self.numero_columnas):
            self.grid[fila + numero_filas_desplazar][column] = self.grid[fila][column]
            self.grid[fila][column] = 0

    def limpia_fila_completa(self):
        filas_completas = 0
        for fila in range(self.numero_filas - 1, 0, -1):
            if self.esta_fila_completa(fila):
                self.limpia_fila(fila)
                filas_completas += 1
            elif filas_completas > 0:
                self.mover_fila_abajo(fila, filas_completas)
        return filas_completas

    def reiniciar(self):
        for fila in range(self.numero_filas):
            for columna in range(self.numero_columnas):
                self.grid[fila][columna] = 0
        return

    def dibuja(self, screen):
        for fila in range(self.numero_filas):
            for columna in range(self.numero_columnas):
                valor_celda = self.grid[fila][columna]
                rectangulo_celda = pygame.Rect(columna * self.size_celda + 11, fila * self.size_celda + 11, self.size_celda - 1, self.size_celda - 1)
                pygame.draw.rect(screen, self.colores[valor_celda], rectangulo_celda)
        return
