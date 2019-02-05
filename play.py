import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640, 480))

fond = pygame.image.load("image/background.jpg").convert()
fenetre.blit(fond, (0, 0))

perso = pygame.image.load("image/perso.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

pygame.display.flip()

continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_DOWN or event.key == K_s:
                position_perso = position_perso.move(0, 10)
            elif event.key == K_UP or event.key == K_z or event.key == K_SPACE:
                position_perso = position_perso.move(0, -30)
            elif event.key == K_LEFT or event.key == K_q:
                position_perso = position_perso.move(-10, 0)
            elif event.key == K_RIGHT or event.key == K_d:
                position_perso = position_perso.move(10, 0)

    fenetre.blit(fond, (0, 0))
    fenetre.blit(perso, position_perso)
    pygame.display.flip()
