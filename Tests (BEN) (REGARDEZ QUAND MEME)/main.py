import pygame
from pygame.locals import *
from gestionRecettes import *
import random
import math

pygame.init()

winwidht = 1000
winheight = 768
win = pygame.display.set_mode((winwidht,winheight))

pygame.display.set_caption("Crêpe party")

walkLeft = [pygame.transform.flip(pygame.image.load('../image/R1.png'),True,False),pygame.transform.flip(pygame.image.load('../image/R2.png'),True,False),pygame.transform.flip(pygame.image.load('../image/R3.png'),True,False),pygame.transform.flip(pygame.image.load('../image/R4.png'),True,False),pygame.transform.flip(pygame.image.load('../image/R5.png'),True,False),pygame.transform.flip(pygame.image.load('../image/R6.png'),True,False),pygame.transform.flip(pygame.image.load('../image/R7.png'),True,False),pygame.transform.flip(pygame.image.load('../image/R8.png'),True,False),pygame.transform.flip(pygame.image.load('../image/R9.png'),True,False)]
walkRight = [pygame.image.load('../image/R1.png'), pygame.image.load('../image/R2.png'), pygame.image.load('../image/R3.png'), pygame.image.load('../image/R4.png'), pygame.image.load('../image/R5.png'), pygame.image.load('../image/R6.png'), pygame.image.load('../image/R7.png'), pygame.image.load('../image/R8.png'), pygame.image.load('../image/R9.png')]
#walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
#walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
char = pygame.image.load('../image/R1.png')

bg = pygame.image.load('FondNormale.png')
bglune = pygame.image.load('bg.jpg')
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
        pygame.draw.rect(win,(255,0,0),self.hitbox,2)

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
        #print("1 : ",poele.y+ poele.height,"\n2 : ", sol.y)
        if rect[1] + rect[3] >= sol.y:
            poele.istombe = False
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2] * self.nb:
            if rect[1] < self.hitbox[3] + self.hitbox[1] and rect[1] + rect[3] > self.hitbox[1]:
                if ((rect[1] + rect[3]) <= (self.hitbox[1] + self.hitbox[3]/2)) and ((rect[1] + rect[3]) >= (self.hitbox[1])):
                    poele.y = self.hitbox[1] - poele.height
                    #poele.isJump = False
                    poele.jumpCount = 10
                    poele.istombe = False

                elif ((rect[1]) >= (self.hitbox[1] + self.hitbox[3]/2)) and (rect[1]) <= (self.hitbox[1] +self.hitbox[3]):
                    poele.y = self.hitbox[1] + self.hitbox[3]
                    poele.y = self.hitbox[1] + self.hitbox[3]+ 5
                    #poele.isJump = False
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
        for i in range(self.nb):
            self.hitbox = (self.x, self.y, self.width, self.height)
            if i == self.ingrePos:
                cube = plateforme(self.x+i*self.width,self.y, self.width,self.height, self.type, self.ingre)
                self.estTouché = cube.toucheIngre(rect)
                if self.estTouché:
                    if self.ingre == 0:
                        print("fromage")
                    elif self.ingre == 1:
                        print("oeuf")
                    elif self.ingre == 2:
                        print("tomate")
                    elif self.ingre == 3:
                        print("sucre")
                    elif self.ingre == 4:
                        print("ressort")
                        poele.y = 0

                    self.ingre = 999

class plateforme(object):
    img = [pygame.image.load('../image/BlockFour.png'),pygame.image.load('../image/CommodeBlock.png'),pygame.image.load('../image/LaveVaiselleBlock.png')]
    ingredients = [pygame.image.load('../image/Fromage.png'),pygame.image.load('../image/oeuf.png'),pygame.image.load('../image/Tomate.png'),pygame.image.load('../image/Sucre.png'),pygame.image.load('../image/ressort.png')]
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
        if self.numIngre < 5:
            self.ing = pygame.transform.scale(self.ingredients[self.numIngre],(64,64))


    def draw(self,win):
        self.hitbox = (self.x,self.y, self.width,self.height)
        win.blit(self.img[self.type], (self.x,self.y))
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        if self.ing != 0:
            win.blit(self.ing,(self.x,self.y-self.height))
            self.hitboxIngre = (self.x,self.y-self.height, self.width,self.height)
            #pygame.draw.rect(win, (255,0,0), self.hitboxIngre, 2)


    def toucheIngre(self,rect):
        if rect[0] + rect[2] > self.hitboxIngre[0] and rect[0] < self.hitboxIngre[0] + self.hitboxIngre[2]:
            if rect[1] < self.hitboxIngre[3] + self.hitboxIngre[1] and rect[1] + rect[3] > self.hitboxIngre[1]:
                if self.numIngre < 5:
                    #print('touché')
                    return True
        else:
            return False


class ingredient(object):
    ingredientsImg = [pygame.image.load('../image/Fromage.png'),pygame.image.load('../image/oeuf.png'),pygame.image.load('../image/Tomate.png'),pygame.image.load('../image/Sucre.png'),pygame.image.load('../image/ressort.png')]

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

def redrawGameWindow():
    global walkCount
    global seconds
    global score

    time = 180 - math.floor(seconds)
    time = "Game Over : " + str(time)
    score = calculscore()
    score = "score : " + str(score)
    # Blit to the screen
    font = pygame.font.Font(None, 50)
    texttemps = font.render(time, True,(255,0,0))
    font2 = pygame.font.Font(None, 50)
    textscore = font2.render(score, True,(255,0,0))


    if not (modelunaire):

        win.blit(bg, (bgX,0))
        win.blit(bg, (bgX2,0))
        #caseingredients = (0, 700, 52*nbIngredients, 68)
        #pygame.draw.rect(win, (255, 255, 255), (caseingredients))
        #for y in mesIngredients:
         #   y.draw(win)
        poele.draw(win)
        #sol.draw(win)
        for x in objects:
            x.draw(win)

        win.blit(texttemps, [((bg.get_width()/4) - 150), 50])
        win.blit(textscore, [((bg.get_width()/2) - 150), 50])
        pygame.display.update()
        AfficheRecette(win,0,0,testcr, (True, testcr.ingredients[1]))
    else:
        win.blit(bglune, (bgXlune,0))
        win.blit(bglune, (bgX2lune,0))
        poele.draw(win)
        #poele.draw(win)
        #sol.draw(win)
        pygame.display.update()


sol = longuePlateforme(0,564,64,64,20,0,999,999)
poele = joueur(300, 500, 64, 64)

ingredientsDisponibles = ["Oeuf","Fromage","Jambon","Cornichon", "Champignons", "Salade", "Tomate", "Nutella", "Sucre", "Miel", "Confiture", "Citron", "Chantilly"]

score = 0
#nbIngredients = 0
plateformeSpeed = 4.4   #14.4 pour du rapide
plateformeSpawn = 2750  #1000 pour du rapide
pygame.time.set_timer(pygame.USEREVENT+1,plateformeSpawn)
pygame.time.set_timer(pygame.USEREVENT+2,5000)

start_ticks=pygame.time.get_ticks()


testcr = Crepes(2)

mesIngredients = []
objects = []

modelunaire = False
run = True
while run:
    clock.tick(30)
    seconds=(pygame.time.get_ticks()-start_ticks)/1000
    if seconds>180:
        run =False
    #print(seconds)


    for objectt in objects:
        objectt.collision(poele.hitbox)
        objectt.x -= plateformeSpeed
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
            objects.append(longuePlateforme(1000,random.randrange(300,500),64,64,nbPlatformes,random.randrange(0,3),random.randrange(0,10),random.randrange(0,nbPlatformes)))

        #if event.type == pygame.USEREVENT+2:
         #   mesIngredients.append(ingredient(nbIngredients))
          #  nbIngredients += 1
           # print('test')

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

    #print("tombe : ",poele.istombe,"\njump : ",poele.istombe)
    #if not (poele.istombe):  #istombe = False
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
    #else: #istombe = True
    if poele.istombe:
        if (poele.y+poele.height < sol.y):
            poele.tomber(objects)
        else:
            poele.istombe = False



    redrawGameWindow()
    #if i%2==0:
    #    AfficheRecette(win,0,0,testcr)
    #else:



pygame.quit()
