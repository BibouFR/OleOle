import pygame
from pygame import *

def AfficheCredit(taille):
    #COULEURS
    blanc = (255,255,255)
    gris = (127,127,127)
    noir = (0,0,0)

    credit = pygame.display.set_mode(taille)
    pygame.display.set_caption("Crédits")
    bg = pygame.image.load("../image/MenuOuvert.png")
    credit.blit(bg, (0,0))

    coord = (394, 340, 250, 70)

    pygame.display.flip()
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                import accueil


tailleCredit = (1000,768)
AfficheCredit(tailleCredit)
