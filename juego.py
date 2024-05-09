import random
import pygame
from tetrominos import *
from grid import Grid

class Juego:
    def __init__(self):
        self.grid             = Grid()
        self.bloques          = [IBloque(), JBloque(), LBloque(), OBloque(), SBloque(), TBloque(), ZBloque()]
        self.bloque_actual    = self.get_bloque_random()
        self.bloque_siguiente = self.get_bloque_random()
        self.game_over        = False
        self.puntaje          = 0
        pygame.mixer.music.load("song.mp3")
        pygame.mixer.music.play(-1) # El argumento -1 en la función play indica que se debe de poner en ciclo indefinidamente
        self.sonido_rotar = pygame.mixer.Sound("rotate.mp3")
        self.sonido_clear = pygame.mixer.Sound("clear.mp3")
        return
    
    def actualiza_puntaje(self, lineas_despejadas, puntos_mover_abajo):
        if lineas_despejadas == 1:
            self.puntaje += 100
        elif lineas_despejadas == 2:
            self.puntaje += 300
        elif lineas_despejadas == 3:
            self.puntaje += 500
        elif lineas_despejadas == 4:
            self.puntaje += 700
        self.puntaje += puntos_mover_abajo
        return
        
    def get_bloque_random(self):
        if len(self.bloques) == 0:
            self.bloques = [IBloque(), JBloque(), LBloque(), OBloque(), SBloque(), TBloque(), ZBloque()]
        bloque = random.choice(self.bloques)
        self.bloques.remove(bloque)
        return bloque

    def mover_izquierda(self):
        self.bloque_actual.mover(0, -1)
        if self.bloque_adentro() == False or self.bloque_entra() == False:
            self.bloque_actual.mover(0, 1)
        return

    def mover_derecha(self):
        self.bloque_actual.mover(0, 1)
        if self.bloque_adentro() == False or self.bloque_entra() == False:
            self.bloque_actual.mover(0, -1)
        return
    
    def mover_abajo(self):
        self.bloque_actual.mover(1, 0)
        if self.bloque_adentro() == False or self.bloque_entra() == False:
            self.bloque_actual.mover(-1, 0)
            self.bloquear_bloque()
        return
    
    def rotar(self):
        self.bloque_actual.rotar()
        if self.bloque_adentro() == False or self.bloque_entra() == False:
            self.bloque_actual.deshacer_rotar()
        else:
            self.sonido_rotar.play()
        return

    def bloquear_bloque(self):
        losas = self.bloque_actual.get_posicion_celda()
        for posicion in losas:
            self.grid.grid[posicion.fila][posicion.columna] = self.bloque_actual.id
        self.bloque_actual = self.bloque_siguiente
        self.bloque_siguiente = self.get_bloque_random()
        lineas_despejadas = self.grid.limpia_fila_completa()
        if lineas_despejadas > 0:
            self.sonido_clear.play()
        self.actualiza_puntaje(lineas_despejadas, 0)
        if self.bloque_entra() == False:
            self.game_over = True
        return

    def bloque_entra(self):
        losas = self.bloque_actual.get_posicion_celda()
        for losa in losas:
            if self.grid.esta_vacio(losa.fila, losa.columna) == False:
                return False
        return True

    def bloque_adentro(self):
        losas = self.bloque_actual.get_posicion_celda()
        for losa in losas:
            if self.grid.esta_dentro(losa.fila, losa.columna) == False:
                return False
        return True

    def reiniciar(self):
        self.grid.reiniciar()
        self.bloques          = [IBloque(), JBloque(), LBloque(), OBloque(), SBloque(), TBloque(), ZBloque()]
        self.bloque_actual    = self.get_bloque_random()
        self.bloque_siguiente = self.get_bloque_random()
        self.puntaje          = 0
        return

    def dibuja(self, screen):
        self.grid.dibuja(screen)
        self.bloque_actual.dibuja(screen , 11, 11)
        if self.bloque_siguiente.id == 1:
            self.bloque_siguiente.dibuja(screen, 255, 290)
        elif self.bloque_siguiente.id == 4:
            self.bloque_siguiente.dibuja(screen, 255, 275)
        else:
            self.bloque_siguiente.dibuja(screen, 270, 270)
        return