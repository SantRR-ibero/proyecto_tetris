class Colores:
    cyan        = (0, 111, 111) # I id = 1
    azul        = (49, 55, 253) # J id = 2
    naranja     = (255, 128, 0) # L id = 3
    amarillo    = (255, 255, 0) # O id = 4
    rojo        = (255, 0, 0)   # S id = 5
    morado      = (87, 35, 100) # T id = 6
    verde       = (0, 155, 0)   # Z id = 7
    blanco      = (246, 246, 246)
    azul_bg     = (13, 27, 42)
    azul2_bg    = (58, 89, 162)
    dorado      = (41, 56, 69)

    @classmethod # Hace que el metodo reciba una clase como primer argumento
    def get_lista_colores(cls):
        return [cls.cyan, cls.azul, cls.naranja, cls.amarillo, cls.rojo, cls.morado, cls.verde, cls.blanco, cls.azul_bg, cls.azul2_bg, cls.dorado]