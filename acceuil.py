import pygame
from pygame.locals import *

class Boutton(object):
    police = pygame.font
    boutton = pygame.image.load("image/)
    rect = boutton.get_rect()

    def __init__(self, lettre, position):
        self.image = Boutton.boutton.copy()
        self.rect = Boutton.rect.copy()
        lettre = Boutton.police.render(lettre, True, (255, 255, 255))
        rect_lettre = lettre.get_rect(center=Boutton.rect.center)
        self.image.blit(lettre, rect_lettre)
        self.rect.topleft = position




pygame.init()


#Ouverture de la fenêtre Pygame

fenetre = pygame.display.set_mode((200,300))

#Chargement et collage du fond

fond = pygame.image.load("image/images.jpeg").convert()

fenetre.blit(fond, (0,0))

#Rafraîchissement de l'écran

pygame.display.flip()

continuer = 1



A = Boutton('A', (100, 550))
fond.blit(A.image, A.rect)

display.flip()

while continuer:
    for event in pygame.event.get():  # Attente des événements
        if event.type == QUIT:
            continuer = 0
