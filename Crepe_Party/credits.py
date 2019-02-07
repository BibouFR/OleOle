import pygame
from pygame import *

def AfficheCredit(taille):

    credit = pygame.display.set_mode(taille)
    pygame.display.set_caption("Crédits")
    bg = pygame.image.load("../image/MenuOuvert.png")
    credit.blit(bg, (0,0))

    pygame.display.flip()
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                import accueil


tailleCredit = (1024,768)
AfficheCredit(tailleCredit)
