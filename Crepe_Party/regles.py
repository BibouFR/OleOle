import pygame
from pygame import *

def AfficheRegles(taille):
    #COULEUR
    blanc = (255,255,255)
    gris = (127,127,127)
    noir = (0,0,0)
    rouge = (255,0,0)
    bleu = (0,0,255)

    winRegles = pygame.display.set_mode(taille)
    pygame.display.set_caption("Règles")
    bg = pygame.image.load("../image/Menu.png")
    winRegles.blit(bg, (0,0))

    #REGLES + QUITTER
    crectRegles = (390,100,250,100)
    crectNomRetour = (520,210,160,50)
    taillePolice = 40
    policeRegles = pygame.font.SysFont("freesans", taillePolice)
    texteRegles = policeRegles.render("Règles", True, noir)
    positTexteRegles = texteRegles.get_rect()
    positTexteRegles.centerx = crectRegles[0]+crectRegles[2]/2
    positTexteRegles.centery = crectRegles[1]+crectRegles[3]/2
    winRegles.blit(texteRegles, positTexteRegles)

    taillePolice = 20
    boutonRetour = pygame.draw.rect(winRegles, gris, crectNomRetour, 1)
    policeNomRetour = pygame.font.SysFont("freesans", taillePolice)
    texteRetour = policeNomRetour.render("Retour", True, noir)
    positTexteRetour = texteRetour.get_rect()
    positTexteRetour.centerx = crectNomRetour[0]+crectNomRetour[2]/2
    positTexteRetour.centery = crectNomRetour[1]+crectNomRetour[3]/2
    winRegles.blit(texteRetour, positTexteRetour)

    regl = pygame.image.load("../image/regles.png")
    winRegles.blit(regl, (335,320))

    pygame.display.flip()

    run = True
    while run:
        mouseXY = pygame.mouse.get_pos()
        over_Retour = boutonRetour.collidepoint(mouseXY)
        for event in pygame.event.get():
            if over_Retour:
                boutonRetour = pygame.draw.rect(winRegles, rouge, crectNomRetour, 1)
            else:
                boutonRetour = pygame.draw.rect(winRegles, gris, crectNomRetour, 1)
            pygame.display.flip()
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and over_Retour:
                run = False
                import accueil

tailleRegles = (1000,768)
AfficheRegles(tailleRegles)
