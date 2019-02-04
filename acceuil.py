import pygame
from pygame.locals import *


pygame.init()


#Ouverture de la fenêtre Pygame

fenetre = pygame.display.set_mode((640, 480))

#Chargement et collage du fond

fond = pygame.image.load("images.jpeg").convert()

fenetre.blit(fond, (0,0))

#Rafraîchissement de l'écran

pygame.display.flip()

continuer = 1

while continuer:
    for event in pygame.event.get():  # Attente des événements
        if event.type == QUIT:
            continuer = 0
