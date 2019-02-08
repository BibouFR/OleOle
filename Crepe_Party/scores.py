import pygame

pygame.init()
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

def prendreScores(fn = "scores.txt"):
    hs = {}
    try:
        with open(fn,"r") as f:
            for line in f:
                name,_,points = line.partition(":")
                if name and points:
                    hs[name]=int(points)
    except FileNotFoundError:
        return {}
    return hs

def prendrePoint(fn = "scores.txt"):
    hs = []
    try:
        with open(fn,"r") as f:
            for line in f:
                name,_,points = line.partition(":")
                if name and points:
                    hs.append(points)
    except FileNotFoundError:
        return []
    return hs



"""
def updateFile():
    f = open('scores.txt','r')
    file = f.readlines()
    last = int(file[0])

    if last < int(score):
        f.close
        file = open('scores.txt','w')
        file.write(str(score))
        file.close

        return score

    return last
"""

def LancerAccueil():
    import accueil

while fin:
    clock.tick(30)
    mouseXY = pygame.mouse.get_pos()

    win.blit(bg, (bgX,0))
    #win.blit(bg, (bgX2,0))
    xBaseBoutons = 390
    yBaseBoutons = 340
    crectBaseBoutons = (xBaseBoutons, yBaseBoutons, 250, 70)

    boutonAccueil = pygame.draw.rect(win, (127,127,127), crectBaseBoutons, 1)
    taillePolice = 40
    policeNomAccueil = pygame.font.SysFont("freesans", taillePolice)
    texteAccueil = policeNomAccueil.render("Accueil", True, (0,0,0))
    positTexteAccueil = texteAccueil.get_rect()
    positTexteAccueil.centerx = crectBaseBoutons[0]+crectBaseBoutons[2]/2
    positTexteAccueil.centery = crectBaseBoutons[1]+crectBaseBoutons[3]/2
    win.blit(texteAccueil, positTexteAccueil)

    over_Accueil = boutonAccueil.collidepoint(mouseXY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1 and over_Accueil:
            print("ACCUEIL...")
            LancerAccueil()


    kk = prendreScores()
    pts = []
    scr1 = 0
    scr2 = 0
    scr3 = 0
    j = 0
    pts = prendrePoint()
    for pt in pts:
        if j == 0:
            scr1 = pt
        elif j == 1:
            scr2 = pt
        elif j == 2:
            scr3 = pt
        j += 1
    font2 = pygame.font.SysFont('comicsans', 80)
    if kk != {}:
        pts = prendrePoint()
        i = 0
        for k in kk:
            nom = k
            if i == 0:
                prevtextscore = font2.render(str(nom) + " : " + str(scr1), True,(255,255,255))
                win.blit(prevtextscore, (winwidht/2 - prevtextscore.get_width()/2,100 + 50*i))
            elif i == 1:
                prevtextscore = font2.render(str(nom) + " : " + str(scr2), True,(255,255,255))
                win.blit(prevtextscore, (winwidht/2 - prevtextscore.get_width()/2,100 + 50*i))
            elif i == 2:
                prevtextscore = font2.render(str(nom) + " : " + str(scr3), True,(255,255,255))
                win.blit(prevtextscore, (winwidht/2 - prevtextscore.get_width()/2,100 + 50*i))
            i += 1
    pygame.display.update()
