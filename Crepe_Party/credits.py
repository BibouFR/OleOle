import pygame
from pygame import *

def AfficheCredit(taille):
    #COULEURS
    blanc = (255,255,255)
    gris = (127,127,127)
    noir = (0,0,0)
    rouge = (255,0,0)
    bleu = (0,0,255)

    winCredit = pygame.display.set_mode(taille)
    pygame.display.set_caption("Crédits")
    bg = pygame.image.load("../image/MenuOuvert.png")
    winCredit.blit(bg, (0,0))

    #CREDITS + QUITTER
    crectCredits = (390,100,250,100)
    crectNomRetour = (520,210,160,50)
    taillePolice = 40
    policeCredits = pygame.font.SysFont("freesans", taillePolice)
    texteCredits = policeCredits.render("Crédits", True, noir)
    positTexteCredits = texteCredits.get_rect()
    positTexteCredits.centerx = crectCredits[0]+crectCredits[2]/2
    positTexteCredits.centery = crectCredits[1]+crectCredits[3]/2
    winCredit.blit(texteCredits, positTexteCredits)

    taillePolice = 20
    boutonRetour = pygame.draw.rect(winCredit, gris, crectNomRetour, 1)
    policeNomRetour = pygame.font.SysFont("freesans", taillePolice)
    texteRetour = policeNomRetour.render("Retour", True, noir)
    positTexteRetour = texteRetour.get_rect()
    positTexteRetour.centerx = crectNomRetour[0]+crectNomRetour[2]/2
    positTexteRetour.centery = crectNomRetour[1]+crectNomRetour[3]/2
    winCredit.blit(texteRetour, positTexteRetour)

    #POLICE GENS
    taillePolice = 15
    policeGens = pygame.font.SysFont("freesans", taillePolice)
    #POLICE TYPES
    policeTypes = pygame.font.SysFont("freesans", taillePolice, True, False)

    #DEVELOPPEURS + LISTE DEVELOPPEURS
    coordDeveloppeurs = (394, 330, 125, 26)
    texteDeveloppeurs = policeTypes.render("Développement", True, bleu)
    positTextDev = texteDeveloppeurs.get_rect()
    positTextDev.centerx = coordDeveloppeurs[0]+coordDeveloppeurs[2]/2
    positTextDev.centery = coordDeveloppeurs[1]+13
    winCredit.blit(texteDeveloppeurs, positTextDev)

    COULEURDELAUTRECASSECOUILLE = (255,0,251)

    coordListeDev = (394, 355, 125, 70)
    texteDev1 = policeGens.render("G. ARNOULT", True, noir)
    texteDev2 = policeGens.render("B. SABY", True, noir)
    texteDev3 = policeGens.render("B. PERRIER", True, noir)
    positTexteDev1 = texteDev1.get_rect()
    positTexteDev1.centerx = coordListeDev[0]+coordListeDev[2]/2
    positTexteDev1.centery = coordListeDev[1]+15
    positTexteDev2 = texteDev1.get_rect()
    positTexteDev2.centerx = coordListeDev[0]+coordListeDev[2]/2
    positTexteDev2.centery = coordListeDev[1]+35
    positTexteDev3 = texteDev1.get_rect()
    positTexteDev3.centerx = coordListeDev[0]+coordListeDev[2]/2
    positTexteDev3.centery = coordListeDev[1]+55
    winCredit.blit(texteDev1, positTexteDev1)
    winCredit.blit(texteDev2, positTexteDev2)
    winCredit.blit(texteDev3, positTexteDev3)

    #GRAPHISMES/SONS + LISTE GENS GRAPHISMES/SONS
    coordStyles = (518, 330, 125, 26)
    texteStyles = policeTypes.render("Graph./Sons", True, bleu)
    positTextDev = texteStyles.get_rect()
    positTextDev.centerx = coordStyles[0]+coordStyles[2]/2
    positTextDev.centery = coordStyles[1]+13
    winCredit.blit(texteStyles, positTextDev)

    coordListeDev = (518, 355, 125, 70)
    texteStyles1 = policeGens.render("P. LAVIER", True, noir)
    texteStyles2 = policeGens.render("Y. COMMEROT", True, noir)
    positTexteStyles1 = texteStyles1.get_rect()
    positTexteStyles1.centerx = coordListeDev[0]+coordListeDev[2]/2
    positTexteStyles1.centery = coordListeDev[1]+20
    positTexteStyles2 = texteStyles2.get_rect()
    positTexteStyles2.centerx = coordListeDev[0]+coordListeDev[2]/2
    positTexteStyles2.centery = coordListeDev[1]+45
    winCredit.blit(texteStyles1, positTexteStyles1)
    winCredit.blit(texteStyles2, positTexteStyles2)

    pygame.draw.line(winCredit, noir, (518, 330), (518, 425))
    pygame.draw.line(winCredit, noir, (394, 356), (643, 356))

    pygame.display.flip()
    run=True
    while run:
        mouseXY = pygame.mouse.get_pos()
        over_Retour = boutonRetour.collidepoint(mouseXY)
        for event in pygame.event.get():
            if over_Retour:
                boutonRetour = pygame.draw.rect(winCredit, rouge, crectNomRetour, 1)
            else:
                boutonRetour = pygame.draw.rect(winCredit, gris, crectNomRetour, 1)
            pygame.display.flip()
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and over_Retour:
                run = False
                import accueil



tailleCredit = (1000,768)
AfficheCredit(tailleCredit)
