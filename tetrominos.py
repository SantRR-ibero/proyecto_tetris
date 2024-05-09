from bloque import Bloque
from posicion import Posicion

# Imagina una matriz nxn (segun el bloque), cada xbloque va a llamar la clase padre bloque para que se muestre en pantalla
# Se una un diccionario de 4 para indicar en que estado de rotacion se encuentra el tetrominó
# Se usa la clase Posicion para indicar que bloque de esa matriz esta relleno
 
class IBloque(Bloque):
    def __init__(self):
        super().__init__(pr_id = 1)
        self.celdas = {
            0: [Posicion(1, 0), Posicion(1, 1), Posicion(1, 2), Posicion(1, 3)],                    
            1: [Posicion(0, 2), Posicion(1, 2), Posicion(2, 2), Posicion(3, 2)],                
            2: [Posicion(2, 0), Posicion(2, 1), Posicion(2, 2), Posicion(2, 3)],                
            3: [Posicion(0, 1), Posicion(1, 1), Posicion(2, 1), Posicion(3, 1)]                
        }
        self.mover(-1, 3)
        return


class JBloque(Bloque):
    def __init__(self):
        super().__init__(pr_id = 2)
        self.celdas = {
            0: [Posicion(0, 0), Posicion(1, 0), Posicion(1, 1), Posicion(1, 2)],
            1: [Posicion(0, 1), Posicion(0, 2), Posicion(1, 1), Posicion(2, 1)],
            2: [Posicion(1, 0), Posicion(1, 1), Posicion(1, 2), Posicion(2, 2)],
            3: [Posicion(0, 1), Posicion(1, 1), Posicion(2, 0), Posicion(2, 1)]
        }
        self.mover(0, 3)
        return


class LBloque(Bloque):
    def __init__(self):
        super().__init__(pr_id = 3)
        self.celdas = {
            0: [Posicion(0, 2), Posicion(1, 0), Posicion(1, 1), Posicion(1, 2)],
            1: [Posicion(0, 1), Posicion(1, 1), Posicion(2, 1), Posicion(2, 2)],
            2: [Posicion(1, 0), Posicion(1, 1), Posicion(1, 2), Posicion(2, 0)],
            3: [Posicion(0, 0), Posicion(0, 1), Posicion(1, 1), Posicion(2, 1)]
        }
        self.mover(0, 3)
        return


class OBloque(Bloque):
    def __init__(self):
        super().__init__(pr_id = 4)
        self.celdas = {
            0: [Posicion(0, 0), Posicion(0, 1), Posicion(1, 0), Posicion(1, 1)],
            1: [Posicion(0, 0), Posicion(0, 1), Posicion(1, 0), Posicion(1, 1)],
            2: [Posicion(0, 0), Posicion(0, 1), Posicion(1, 0), Posicion(1, 1)],
            3: [Posicion(0, 0), Posicion(0, 1), Posicion(1, 0), Posicion(1, 1)]
        }
        self.mover(0, 4)
        return


class SBloque(Bloque):
    def __init__(self):
        super().__init__(pr_id = 5)
        self.celdas = {
            0: [Posicion(0, 1), Posicion(0, 2), Posicion(1, 0), Posicion(1, 1)],
            1: [Posicion(0, 1), Posicion(1, 1), Posicion(1, 2), Posicion(2, 2)],
            2: [Posicion(1, 1), Posicion(1, 2), Posicion(2, 0), Posicion(2, 1)],
            3: [Posicion(0, 0), Posicion(1, 0), Posicion(1, 1), Posicion(2, 1)]
        }
        self.mover(0, 3)
        return


class TBloque(Bloque):
    def __init__(self):
        super().__init__(pr_id = 6)
        self.celdas = {
            0: [Posicion(0, 1), Posicion(1, 0), Posicion(1, 1), Posicion(1, 2)],
            1: [Posicion(0, 1), Posicion(1, 1), Posicion(1, 2), Posicion(2, 1)],
            2: [Posicion(1, 0), Posicion(1, 1), Posicion(1, 2), Posicion(2, 1)],
            3: [Posicion(0, 1), Posicion(1, 0), Posicion(1, 1), Posicion(2, 1)]
        }
        self.mover(0, 3)
        return


class ZBloque(Bloque):
    def __init__(self):
        super().__init__(pr_id = 7)
        self.celdas = {
            0: [Posicion(0, 0), Posicion(0, 1), Posicion(1, 1), Posicion(1, 2)],
            1: [Posicion(0, 2), Posicion(1, 1), Posicion(1, 2), Posicion(2, 1)],
            2: [Posicion(1, 0), Posicion(1, 1), Posicion(2, 1), Posicion(2, 2)],
            3: [Posicion(0, 1), Posicion(1, 0), Posicion(1, 1), Posicion(2, 0)]
        }
        self.mover(0, 3)
        return