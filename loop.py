import pygame
import sys
from juego import Juego
from colores import Colores

pygame.init()

fuente_titulo      = pygame.font.Font(None, 40)
superficie_puntaje = fuente_titulo.render("Puntaje", True, Colores.blanco)
rectangulo_puntaje = pygame.Rect(320, 55, 170, 60)

superficie_siguiente = fuente_titulo.render("Siguiente", True, Colores.blanco)
rectangulo_siguiente = pygame.Rect(320, 215, 170, 180)

superficie_game_over = fuente_titulo.render("GAME OVER", True, Colores.blanco)

screen             = pygame.display.set_mode((500, 620))
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
                mi_juego.actualiza_puntaje(0, 1)
            if event.key == pygame.K_UP and mi_juego.game_over == False:
                mi_juego.rotar()
        if event.type == actualiza_juego and mi_juego.game_over == False:
            mi_juego.mover_abajo()

    # Dibuja
    valor_superficie_puntaje = fuente_titulo.render(str(mi_juego.puntaje), True, Colores.blanco)
    screen.fill(Colores.bg1)
    screen.blit(superficie_puntaje, (355, 20, 50, 50))
    screen.blit(superficie_siguiente, (340, 180, 50 , 50))
    

    if mi_juego.game_over == True:
        screen.blit(superficie_game_over, (320, 450, 50, 50))

    pygame.draw.rect(screen, Colores.bg3, rectangulo_puntaje, 0, 10)
    screen.blit(valor_superficie_puntaje, valor_superficie_puntaje.get_rect(centerx = rectangulo_puntaje.centerx, centery = rectangulo_puntaje.centery))
    pygame.draw.rect(screen, Colores.bg3, rectangulo_siguiente, 0, 10)
    mi_juego.dibuja(screen)

    pygame.display.flip()
    reloj.tick(60)
