import pygame
from pygame.locals import *
from gestionRecettes import *
import random
import math
from operator import itemgetter


pygame.init()

winwidht = 1000
winheight = 768
win = pygame.display.set_mode((winwidht,winheight))

pygame.display.set_caption("Crêpe party")

walkLeft = [pygame.transform.flip(pygame.image.load('../image/R1.png'),True,False),pygame.transform.flip(pygame.image.load('../image/R2.png'),True,False),pygame.transform.flip(pygame.image.load('../image/R3.png'),True,False),pygame.transform.flip(pygame.image.load('../image/R4.png'),True,False),pygame.transform.flip(pygame.image.load('../image/R5.png'),True,False),pygame.transform.flip(pygame.image.load('../image/R6.png'),True,False),pygame.transform.flip(pygame.image.load('../image/R7.png'),True,False),pygame.transform.flip(pygame.image.load('../image/R8.png'),True,False),pygame.transform.flip(pygame.image.load('../image/R9.png'),True,False)]
walkRight = [pygame.image.load('../image/R1.png'), pygame.image.load('../image/R2.png'), pygame.image.load('../image/R3.png'), pygame.image.load('../image/R4.png'), pygame.image.load('../image/R5.png'), pygame.image.load('../image/R6.png'), pygame.image.load('../image/R7.png'), pygame.image.load('../image/R8.png'), pygame.image.load('../image/R9.png')]
char = pygame.image.load('../image/R1.png')

bg = pygame.image.load('FondNormale.png')
bglune = pygame.image.load('../image/FondEspace.png')
bgX = 0
bgX2 = bg.get_width()

bgXlune = 0
bgX2lune = bglune.get_width()

clock = pygame.time.Clock()

def calculscore():
    global testcr
    score = 0




class joueur(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.istombe = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)

    def draw(self,win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))

        self.hitbox = (self.x + 17, self.y + 10, 31, 57)
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def tomber(self,objects):
        i = 5
        for objectt in objects:
            if not(objectt.collision(self.hitbox)):
                poele.y += i
                i += 3
            else:
                i = 5


class longuePlateforme(object):
    def __init__(self, x, y, width, height, nb, type, ingre, ingrePos):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.nb = nb
        self.type = type
        self.hitbox = (x,y,width*nb,height)
        self.count = 0
        self.ingre = ingre
        self.ingrePos = ingrePos
        self.estTouché = False



    def draw(self,win):
        for i in range(self.nb):
            self.hitbox = (self.x, self.y, self.width, self.height)
            if i == self.ingrePos:
                cube = plateforme(self.x+i*self.width,self.y, self.width,self.height, self.type, self.ingre)
            else:
                cube = plateforme(self.x+i*self.width,self.y, self.width,self.height, self.type, 999)
            cube.draw(win)

    def collision(self,rect):
        if rect[1] + rect[3] >= sol.y:
            poele.istombe = False
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2] * self.nb:
            if rect[1] < self.hitbox[3] + self.hitbox[1] and rect[1] + rect[3] > self.hitbox[1]:
                if ((rect[1] + rect[3]) <= (self.hitbox[1] + self.hitbox[3]/2)) and ((rect[1] + rect[3]) >= (self.hitbox[1])):
                    poele.y = self.hitbox[1] - poele.height
                    poele.jumpCount = 10
                    poele.istombe = False

                elif ((rect[1]) >= (self.hitbox[1] + self.hitbox[3]/2)) and (rect[1]) <= (self.hitbox[1] +self.hitbox[3]):
                    poele.y = self.hitbox[1] + self.hitbox[3]
                    poele.y = self.hitbox[1] + self.hitbox[3]+ 5
                    poele.jumpCount = 10
                    poele.istombe = False

                if rect[0] < self.hitbox[0] and rect[1] +rect[3] > self.hitbox[1]+20:  #collision a droite
                    poele.x -= 5
                elif rect[0] + rect[2] > self.hitbox[0] and rect[1] +rect[3] > self.hitbox[1]+20:
                    poele.x += 5
                return True
        elif poele.isJump:
            poele.istombe = False
        elif rect[1] < self.hitbox[1] and rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2] * self.nb:
            poele.istombe = False
        else:
            poele.istombe = True
            poele.isJump = False
        return False


    def toucheIngr(self,rect):
        global modelunaire
        for i in range(self.nb):
            self.hitbox = (self.x, self.y, self.width, self.height)
            if i == self.ingrePos:
                cube = plateforme(self.x+i*self.width,self.y, self.width,self.height, self.type, self.ingre)
                self.estTouché = cube.toucheIngre(rect)
                if self.estTouché:
                    if self.ingre == 0:
                        poele.y = 0
                        testIngr("Ressort")
                    elif self.ingre == 1:
                        testIngr("Fromage")
                    elif self.ingre == 2:
                        testIngr("Oeuf")
                    elif self.ingre == 3:
                        testIngr("Tomate")
                    elif self.ingre == 4:
                        testIngr("Sucre")
                    elif self.ingre == 5:
                        testIngr("Cornichon")
                    elif self.ingre == 6:
                        testIngr("Nutella")
                    elif self.ingre == 7:
                        testIngr("Champignons")
                    elif self.ingre == 8:
                        testIngr("Miel")
                    elif self.ingre == 9:
                        testIngr("Confiture")
                    elif self.ingre == 10:
                        modelunaire = True
                    elif self.ingre == 11:
                        testIngr("Citron")
                    elif self.ingre == 12:
                        testIngr("Chantilly")
                    self.ingre = 999


def testIngr(nom):
    global score, dernierIngr
    ingrTrouve = False
    if nom == "Ressort":
        if dernierIngr != "":
            testcr.ingredients.append(dernierIngr)
    for i in testcr.ingredients:
        if i == nom:
            dernierIngr = nom
            ingrTrouve = True
            testcr.ingredients.pop(testcr.ingredients.index(i))
            if len(testcr.ingredients) == 0:
                score += 100
                nouvelleRecette(2)
                dernierIngr = ""
    if ingrTrouve:
        score += 20
    else:
        score -= 10

class plateforme(object):
    img = [pygame.image.load('../image/BlockFour.png'),pygame.image.load('../image/CommodeBlock.png'),pygame.image.load('../image/LaveVaiselleBlock.png')]
    ingredients = [pygame.image.load('../image/ressort.png'),pygame.image.load('../image/fromage.png'),pygame.image.load('../image/oeuf.png'),pygame.image.load('../image/tomate.png'),pygame.image.load('../image/sucre.png'),pygame.image.load('../image/cornichon.png'),pygame.image.load('../image/Nutella.png'),pygame.image.load('../image/champi.png'),pygame.image.load('../image/miel.png'),pygame.image.load('../image/Confiture.png'),pygame.image.load('../image/fusee.png'),pygame.image.load('../image/citron.png'),pygame.image.load('../image/chantilly.png')]

    def __init__(self, x, y, width, height, type, numIngre):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = type
        self.hitbox = (x,y,width,height)
        self.count = 0
        self.ing = 0
        self.numIngre = numIngre
        self.hitboxIngre = (x,y-width,width,height)
        if self.numIngre < 13:
            self.ing = pygame.transform.scale(self.ingredients[self.numIngre],(64,64))


    def draw(self,win):
        self.hitbox = (self.x,self.y, self.width,self.height)
        if not(modelunaire):
            win.blit(self.img[self.type], (self.x,self.y))
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        if self.ing != 0:
            win.blit(self.ing,(self.x,self.y-self.height))
            self.hitboxIngre = (self.x,self.y-self.height, self.width,self.height)
            #pygame.draw.rect(win, (255,0,0), self.hitboxIngre, 2)


    def toucheIngre(self,rect):
        if rect[0] + rect[2] > self.hitboxIngre[0] and rect[0] < self.hitboxIngre[0] + self.hitboxIngre[2]:
            if rect[1] < self.hitboxIngre[3] + self.hitboxIngre[1] and rect[1] + rect[3] > self.hitboxIngre[1]:
                if self.numIngre < 13:
                    return True
        else:
            return False


class ingredient(object):
    ingredientsImg = [pygame.image.load('../image/ressort.png'),pygame.image.load('../image/fromage.png'),pygame.image.load('../image/oeuf.png'),pygame.image.load('../image/tomate.png'),pygame.image.load('../image/sucre.png'),pygame.image.load('../image/cornichon.png'),pygame.image.load('../image/Nutella.png'),pygame.image.load('../image/champi.png'),pygame.image.load('../image/miel.png'),pygame.image.load('../image/Confiture.png'),pygame.image.load('../image/fusee.png'),pygame.image.load('../image/citron.png'),pygame.image.load('../image/chantilly.png')]
    def __init__(self,numIngreImg,nomIngre):
        self.nomIngre = nomIngre
        self.nomIngreImg = pygame.image.load('../image/' + nomIngreImg + '.png')
        self.x = 20
        self.y = 720
        self.width = 32
        self.height = 32
        self.petiteImage = pygame.transform.scale(self.nomIngreImg,(32,32))

    def draw(self,win):
        self.x = 20 + self.numIngre * 52
        win.blit(self.petiteImage,(self.x,self.y))

def nouvelleRecette(difficulte):
    global testcr
    testcr = Crepes(difficulte)



def redrawGameWindow():
    global walkCount
    global seconds
    global score
    global modelunaire
    global timelunaire
    global timerss

    time = 180 - math.floor(seconds)
    timer = "Time : " + str(time)
    tscore = "score : " + str(score)
    font = pygame.font.Font(None, 50)
    texttemps = font.render(timer, True,(255,255,255))
    font2 = pygame.font.Font(None, 50)
    textscore = font2.render(tscore, True,(255,255,255))



    if not (modelunaire):
        win.blit(bg, (bgX,0))
        win.blit(bg, (bgX2,0))
        poele.draw(win)
        for x in objects:
            x.draw(win)

        win.blit(texttemps, [((bg.get_width()/3)), 50])
        win.blit(textscore, [((bg.get_width()/4) - 150), 50])
        AfficheRecette(win,0,0,testcr)
        pygame.display.update()
    else:
        win.blit(bglune, (bgXlune,0))
        win.blit(bglune, (bgX2lune,0))
        win.blit(texttemps, [((bg.get_width()/3)), 50])
        win.blit(textscore, [((bg.get_width()/4) - 150), 50])

        timerlunaire = "lunaire : " + str(timerss)
        font3 = pygame.font.Font(None, 50)
        texttimer = font3.render(timerlunaire, True,(255,255,255))
        win.blit(texttimer, [((bg.get_width()/3)), 100])

        poele.draw(win)
        for x in objects:
            x.draw(win)
        if (timerss <= 1):
            modelunaire = False
            debut = 0
            poele.y = 0

        AfficheRecette(win,0,0,testcr)
        pygame.display.update()

def endScreen():
    fin = True
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    nom = text
    kk = {}
    b = True

    while fin:
        clock.tick(30)
        mouseXY = pygame.mouse.get_pos()

        win.blit(bg, (bgX,0))
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        nom = text
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        font = pygame.font.SysFont(text, 50)
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        input_box.x = (winwidht/2 - width/2)
        input_box.y = 550
        win.blit(txt_surface, (winwidht/2 - width/2,550))
        pygame.draw.rect(win, color, input_box, 2)

        if nom != '' and b:
            mettreScores(nom,score)
            b = False

        prendreScores()
        font2 = pygame.font.SysFont('comicsans', 80)
        textscore = font2.render("Score : " + str(score), True,(255,255,255))
        win.blit(textscore, (winwidht/2 - textscore.get_width()/2,270))
        pygame.display.update()

def mettreScores(nom,score):
    src = open("scores.txt","a")
    src.write(nom + " " + str(score) + "\n")
    src.close()

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
        font2 = pygame.font.SysFont('comicsans', 80)
        prevtextscore = font2.render(str(i+1) + " : " + liste2[i][0] + " " + str(liste2[i][1]), True,(255,255,255))
        win.blit(prevtextscore, (winwidht/2 - prevtextscore.get_width()/2,100 + 50*i))

def LancerAccueil():
    import accueil

sol = longuePlateforme(0,564,64,64,20,0,999,999)
poele = joueur(300, 500, 64, 64)
score = 0
plateformeSpeed = 7   #14.4 pour du rapide
plateformeSpawn = 2000  #1000 pour du rapide
pygame.time.set_timer(pygame.USEREVENT+1,plateformeSpawn)
pygame.time.set_timer(pygame.USEREVENT+2,1000)
start_ticks=pygame.time.get_ticks()
testcr = Crepes(2)
dernierIngr = ""
mesIngredients = []
objects = []
modelunaire = False
timelunaire =0
timerss = 20
run = True
while run:
    clock.tick(30)
    seconds=(pygame.time.get_ticks()-start_ticks)/1000
    if seconds>180:
        run = False
        endScreen()

    if not(modelunaire):
        for objectt in objects:
            objectt.collision(poele.hitbox)
            objectt.x -= plateformeSpeed
            if objectt.x < -objectt.width * objectt.nb:
                objects.pop(objects.index(objectt))
            objectt.toucheIngr(poele.hitbox)
    else:
        for objectt in objects:
            objectt.x -= plateformeSpeed*3
            if objectt.x < -objectt.width * objectt.nb:
                objects.pop(objects.index(objectt))
            objectt.toucheIngr(poele.hitbox)

    bgX -= 1.4
    bgX2 -= 1.4
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.USEREVENT+1:
            nbPlatformes = random.randrange(1,5)
            if not (modelunaire):
                objects.append(longuePlateforme(1000,random.randrange(300,500),64,64,nbPlatformes,random.randrange(0,3),random.randrange(0,16),random.randrange(0,nbPlatformes)))
            else:
                objects.append(longuePlateforme(1000,random.randrange(50,700),64,64,nbPlatformes,random.randrange(0,3),random.randrange(0,16),random.randrange(0,nbPlatformes)))

        if event.type == pygame.USEREVENT+2:
            if modelunaire:
                timerss -= 1
            else:
                timerss = 20

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and poele.x > poele.vel:
        poele.x -= poele.vel
        poele.left = True
        poele.right = False
    elif keys[pygame.K_RIGHT] and poele.x < winwidht - poele.width - poele.vel:
        poele.x += poele.vel
        poele.left = False
        poele.right = True
    else:
        poele.left = False
        poele.right = False
        poele.walkCount = 0

    if not(modelunaire):
        if not(poele.isJump):
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                poele.isJump = True
                poele.left = False
                poele.right = False
                poele.walkCount = 0
        else:
            if poele.jumpCount >= -10:
                neg = 1
                if poele.jumpCount < 0:
                    neg = -1
                poele.y -= (poele.jumpCount ** 2) * 0.5 * neg
                poele.jumpCount -= 1
            else:
                poele.isJump = False
                poele.jumpCount = 10
        if poele.istombe:
            if (poele.y+poele.height < sol.y):
                poele.tomber(objects)
            else:
                poele.istombe = False
    else:
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            poele.y = poele.y-7
        if keys[pygame.K_DOWN]:
            poele.y= poele.y+7

    redrawGameWindow()
pygame.quit()
