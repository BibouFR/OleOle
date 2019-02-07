import pygame
from pygame import *

pygame.init()

def LancerJeu():
    import main

def incr(crect):
    crect = (crect[0], crect[1]+75, crect[2], crect[3])
    return crect

def AfficheAccueil(tailleAccueil):
    global font

    accueil = pygame.display.set_mode(tailleAccueil)
    pygame.display.set_caption("Menu d'accueil")
    bg = pygame.image.load("../image/Menu.png")
    accueil.blit(bg, (0,0))

    #COULEURS
    noir = (0,0,0)
    gris = (127,127,127)
    blanc = (255,255,255)


    #NOM DU JEU + NOM D'EQUIPE
    crectNomJeu = (390,100,250,100)
    crectNomEquipe = (540,225,160,50)
    taillePolice = 60
    policeNomJeu = pygame.font.SysFont("freesans", taillePolice)
    texteJeu = policeNomJeu.render("Crêpe Party !", True, noir)
    positTexteJeu = texteJeu.get_rect()
    positTexteJeu.centerx = crectNomJeu[0]+crectNomJeu[2]/2
    positTexteJeu.centery = crectNomJeu[1]+crectNomJeu[3]/2
    accueil.blit(texteJeu, positTexteJeu)

    taillePolice = 20
    policeNomEquipe = pygame.font.SysFont("freesans", taillePolice)
    texteEquipe = policeNomEquipe.render("by team OleOle", True, noir)
    positTexteEquipe = texteEquipe.get_rect()
    positTexteEquipe.centerx = crectNomEquipe[0]+crectNomEquipe[2]/2
    positTexteEquipe.centery = crectNomEquipe[1]+crectNomEquipe[3]/2
    accueil.blit(texteEquipe, positTexteEquipe)


    #BOUTONS CHOIX POUR MENU
    xBaseBoutons = 390
    yBaseBoutons = 340
    crectBaseBoutons = (xBaseBoutons, yBaseBoutons, 250, 70)
    boutonJouer = pygame.draw.rect(accueil, gris, crectBaseBoutons, 1)
    taillePolice = 40
    policeNomJouer = pygame.font.SysFont("freesans", taillePolice)
    texteJouer = policeNomJouer.render("Jouer !", True, noir)
    positTexteJouer = texteJouer.get_rect()
    positTexteJouer.centerx = crectBaseBoutons[0]+crectBaseBoutons[2]/2
    positTexteJouer.centery = crectBaseBoutons[1]+crectBaseBoutons[3]/2
    accueil.blit(texteJouer, positTexteJouer)

    crectBaseBoutons = incr(crectBaseBoutons)
    boutonHighscores = pygame.draw.rect(accueil, gris, crectBaseBoutons, 1)
    taillePolice = 60
    policeNomJeu = pygame.font.SysFont("freesans", taillePolice)
    texteJeu = policeNomJeu.render("Crêpe Party !", True, noir)
    positTexteJeu = texteJeu.get_rect()
    positTexteJeu.centerx = crectNomJeu[0]+crectNomJeu[2]/2
    positTexteJeu.centery = crectNomJeu[1]+crectNomJeu[3]/2
    accueil.blit(texteJeu, positTexteJeu)

    crectBaseBoutons = incr(crectBaseBoutons)
    boutonRegles = pygame.draw.rect(accueil, gris, crectBaseBoutons, 1)
    taillePolice = 60
    policeNomJeu = pygame.font.SysFont("freesans", taillePolice)
    texteJeu = policeNomJeu.render("Crêpe Party !", True, noir)
    positTexteJeu = texteJeu.get_rect()
    positTexteJeu.centerx = crectNomJeu[0]+crectNomJeu[2]/2
    positTexteJeu.centery = crectNomJeu[1]+crectNomJeu[3]/2
    accueil.blit(texteJeu, positTexteJeu)

    crectBaseBoutons = incr(crectBaseBoutons)
    boutonCredits = pygame.draw.rect(accueil, gris, crectBaseBoutons, 1)
    taillePolice = 60
    policeNomJeu = pygame.font.SysFont("freesans", taillePolice)
    texteJeu = policeNomJeu.render("Crêpe Party !", True, noir)
    positTexteJeu = texteJeu.get_rect()
    positTexteJeu.centerx = crectNomJeu[0]+crectNomJeu[2]/2
    positTexteJeu.centery = crectNomJeu[1]+crectNomJeu[3]/2
    accueil.blit(texteJeu, positTexteJeu)

    crectBaseBoutons = incr(crectBaseBoutons)
    boutonQuitter = pygame.draw.rect(accueil, gris, crectBaseBoutons, 1)
    taillePolice = 60
    policeNomJeu = pygame.font.SysFont("freesans", taillePolice)
    texteJeu = policeNomJeu.render("Crêpe Party !", True, noir)
    positTexteJeu = texteJeu.get_rect()
    positTexteJeu.centerx = crectNomJeu[0]+crectNomJeu[2]/2
    positTexteJeu.centery = crectNomJeu[1]+crectNomJeu[3]/2
    accueil.blit(texteJeu, positTexteJeu)


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


#LancerJeu()
tailleAccueil = (1024,768)

AfficheAccueil(tailleAccueil)

pygame.quit()
