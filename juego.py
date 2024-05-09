import random
from tetrominos import *
from grid import Grid

class Juego:
    def __init__(self):
        self.grid             = Grid()
        self.bloques          = [IBloque(), JBloque(), LBloque(), OBloque(), SBloque(), TBloque(), ZBloque()]
        self.bloque_actual    = self.get_bloque_random()
        self.bloque_siguiente = self.get_bloque_random()
        self.game_over        = False
        
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
        return

    def bloquear_bloque(self):
        losas = self.bloque_actual.get_posicion_celda()
        for posicion in losas:
            self.grid.grid[posicion.fila][posicion.columna] = self.bloque_actual.id
        self.bloque_actual = self.bloque_siguiente
        self.bloque_siguiente = self.get_bloque_random()
        self.grid.limpia_fila_completa()
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
        return

    def dibuja(self, screen):
        self.grid.dibuja(screen)
        self.bloque_actual.dibuja(screen)