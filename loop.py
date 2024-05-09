import pygame
import sys
from juego import Juego

pygame.init()
dorado_grid = (41, 56, 69)
screen      = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tetris")

reloj   = pygame.time.Clock()
mi_juego = Juego()

# Crear un evento cada 400ms, se usa para bajar el bloque automáticamente
actualiza_juego = pygame.USEREVENT
pygame.time.set_timer(actualiza_juego, 400)

salir = False
while salir == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if mi_juego.game_over == True:
                mi_juego.game_over = False
                mi_juego.reiniciar()
            if event.key == pygame.K_LEFT and mi_juego.game_over == False:
                mi_juego.mover_izquierda()
            if event.key == pygame.K_RIGHT and mi_juego.game_over == False:
                mi_juego.mover_derecha()
            if event.key == pygame.K_DOWN and mi_juego.game_over == False:
                mi_juego.mover_abajo()
            if event.key == pygame.K_UP and mi_juego.game_over == False:
                mi_juego.rotar()
        if event.type == actualiza_juego and mi_juego.game_over == False:
            mi_juego.mover_abajo()


    # Dibuja
    screen.fill(dorado_grid)
    mi_juego.dibuja(screen)
    pygame.display.flip()
    reloj.tick(60)