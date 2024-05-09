class Colores:
    cyan     = (12, 183, 242) # I id = 1
    azul     = (50, 85, 239)  # J id = 2
    naranja  = (255, 128, 0) # L id = 3
    amarillo = (255, 255, 0) # O id = 4
    rojo     = (255, 0, 0)   # S id = 5
    morado   = (120, 10, 200) # T id = 6
    verde    = (0, 155, 0)   # Z id = 7
    blanco   = (246, 246, 246)
    bg1      = (34, 34, 59)     
    bg2      = (74, 78, 105) # matriz
    bg3      = (154, 140, 152)
    bg4      = (201, 173, 167)
    
    @classmethod # Hace que el metodo reciba una clase como primer argumento
    def get_color_celda(cls):
        return [cls.bg2, cls.cyan, cls.azul, cls.naranja, cls.amarillo, cls.rojo, cls.morado, cls.verde]