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
    policeNomHighscores = pygame.font.SysFont("freesans", taillePolice)
    texteHighscores = policeNomHighscores.render("Scores", True, noir)
    positTexteHighscores = texteHighscores.get_rect()
    positTexteHighscores.centerx = crectBaseBoutons[0]+crectBaseBoutons[2]/2
    positTexteHighscores.centery = crectBaseBoutons[1]+crectBaseBoutons[3]/2
    accueil.blit(texteHighscores, positTexteHighscores)

    crectBaseBoutons = incr(crectBaseBoutons)
    boutonRegles = pygame.draw.rect(accueil, gris, crectBaseBoutons, 1)
    policeNomRegles = pygame.font.SysFont("freesans", taillePolice)
    texteRegles = policeNomRegles.render("Règles", True, noir)
    positTexteRegles = texteRegles.get_rect()
    positTexteRegles.centerx = crectBaseBoutons[0]+crectBaseBoutons[2]/2
    positTexteRegles.centery = crectBaseBoutons[1]+crectBaseBoutons[3]/2
    accueil.blit(texteRegles, positTexteRegles)

    crectBaseBoutons = incr(crectBaseBoutons)
    boutonCredits = pygame.draw.rect(accueil, gris, crectBaseBoutons, 1)
    policeNomCredits = pygame.font.SysFont("freesans", taillePolice)
    texteCredits = policeNomCredits.render("Crédits", True, noir)
    positTexteCredits = texteCredits.get_rect()
    positTexteCredits.centerx = crectBaseBoutons[0]+crectBaseBoutons[2]/2
    positTexteCredits.centery = crectBaseBoutons[1]+crectBaseBoutons[3]/2
    accueil.blit(texteCredits, positTexteCredits)

    crectBaseBoutons = incr(crectBaseBoutons)
    boutonQuitter = pygame.draw.rect(accueil, gris, crectBaseBoutons, 1)
    policeNomJeu = pygame.font.SysFont("freesans", taillePolice)
    texteJeu = policeNomJeu.render("Quitter", True, noir)
    positTexteJeu = texteJeu.get_rect()
    positTexteJeu.centerx = crectBaseBoutons[0]+crectBaseBoutons[2]/2
    positTexteJeu.centery = crectBaseBoutons[1]+crectBaseBoutons[3]/2
    accueil.blit(texteJeu, positTexteJeu)






    pygame.display.flip()

    #if appuie sur play:
    #    LancerJeu()
    run = True
    while run:
        mouseXY = pygame.mouse.get_pos()
        over_Jouer = boutonJouer.collidepoint(mouseXY)
        over_Highscores = boutonHighscores.collidepoint(mouseXY)
        over_Regles = boutonRegles.collidepoint(mouseXY)
        over_Credits = boutonCredits.collidepoint(mouseXY)
        over_Quitter = boutonQuitter.collidepoint(mouseXY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN and event.button==1 and over_Quitter:
                print("Merci d'avoir joué, à bientot !")
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1 and over_Jouer:
                print("LOADING...")
                LancerJeu()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1 and over_Regles:
                print("REGLES")
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1 and over_Credits:
                import credits
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1 and over_Highscores:
                import highscores

    pygame.display.flip()


#LancerJeu()
tailleAccueil = (1024,768)

AfficheAccueil(tailleAccueil)

pygame.quit()
