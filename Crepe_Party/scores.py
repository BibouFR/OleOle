import pygame
from operator import itemgetter

#COULEURS
noir = (0,0,0)
gris = (127,127,127)
grisClair = (200,200,200)
blanc = (255,255,255)
rouge = (255,0,0)

clock = pygame.time.Clock()
winwidht = 1000
winheight = 768
win = pygame.display.set_mode((winwidht,winheight))

pygame.display.set_caption("Crêpe party")

bg = pygame.image.load('FondNormale.png')
bgX = 0
bgX2 = bg.get_width()


fin = True
kk = {}


def prendreScores():
    src = open("scores.txt","r")
    liste = []
    for ligne in src:
        score = ""
        nom = ""
        for car in ligne:
            if car<='9' and car >= '0':
                score = score + car
            elif car<='z' and car >='A':
                nom = nom + car
        tuple = (nom, int(score))
        liste.append(tuple)
    liste2 = sorted(liste, key = itemgetter(1), reverse=True)
    #print(liste2)
    src.close()
    if len(liste2) < 4:
        x = len(liste2)
    else:
        x = 3
    for i in range(0,x):
        font2 = pygame.font.SysFont('comicsans', 60)
        prevtextscore = font2.render(liste2[i][0] + " " + str(liste2[i][1]), True,(255,255,255))
        win.blit(prevtextscore, (winwidht/2 - prevtextscore.get_width()/2,200 + 50*i))


def LancerAccueil():
    import accueil

win.blit(bg, (bgX,0))
#win.blit(bg, (bgX2,0))
xBaseBoutons = 400
yBaseBoutons = 350
crectBaseBoutons = (xBaseBoutons, yBaseBoutons, 200, 50)

boutonAccueil = pygame.draw.rect(win, gris, crectBaseBoutons, 1)
taillePolice = 40
policeNomAccueil = pygame.font.SysFont("freesans", taillePolice)
texteAccueil = policeNomAccueil.render("Accueil", True, gris)
positTexteAccueil = texteAccueil.get_rect()
positTexteAccueil.centerx = crectBaseBoutons[0]+crectBaseBoutons[2]/2
positTexteAccueil.centery = crectBaseBoutons[1]+crectBaseBoutons[3]/2
win.blit(texteAccueil, positTexteAccueil)

while fin:
    clock.tick(30)
    mouseXY = pygame.mouse.get_pos()
    over_Accueil = boutonAccueil.collidepoint(mouseXY)
    for event in pygame.event.get():
        if over_Accueil:
            boutonAccueil = pygame.draw.rect(win, rouge, crectBaseBoutons, 1)
            texteAccueil = policeNomAccueil.render("Accueil", True, rouge)
        else:
            boutonAccueil = pygame.draw.rect(win, gris, crectBaseBoutons, 1)
            texteAccueil = policeNomAccueil.render("Accueil", True, gris)
        pygame.display.flip()
        win.blit(texteAccueil, positTexteAccueil)
        if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN and event.button==1 and over_Accueil:
            fin = False
            import accueil

    prendreScores()
    pygame.display.update()
