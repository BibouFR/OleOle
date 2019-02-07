import pygame
from pygame import *

tailleAccueil = (1024,768)

def LancerJeu():
    import main

def AfficheAccueil(tailleAccueil):
    accueil = pygame.display.set_mode(tailleAccueil)
    pygame.display.set_caption("Menu d'accueil")
    bg = pygame.image.load("../image/Menu.png")
    accueil.blit(bg, (0,0))

    #COULEURS
    noir = (0,0,0)
    blanc = (255,255,255)


    #NOM DU JEU + NOM D'EQUIPE
    crectNomJeu = (390,100,250,50)
    crectNomEquipe = (450,200,150,50)
    rectNomJeu = pygame.draw.rect(accueil, noir, crectNomJeu , 2)
    rectNomEquipe = pygame.draw.rect(accueil, noir, crectNomEquipe , 2)
    """policeNomJeu = pygame.font.SysFont("freesans", 30, True, True)
    texte = policeNomJeu.render("Crêpe Party !", True, noir)
    positTexte = texte.get_rect()
    positTexte.centerx = crectNomJeu[0]+crectNomJeu[2]/2
    positTexte.cernety = crectNomJeu[1]+crectNomJeu[3]/2
    accueil.blit(texte, positTexte)"""

    pygame.display.flip()

    #if appuie sur play:
    #    LancerJeu()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Merci d'avoir joué, à bientot !")
                run = False
    pygame.display.flip()


LancerJeu()
#AfficheAccueil(tailleAccueil)
