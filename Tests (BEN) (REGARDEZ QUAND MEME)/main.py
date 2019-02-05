import pygame
from pygame.locals import *
import random

pygame.init()

winwidht = 1000
winheight = 768
win = pygame.display.set_mode((winwidht,winheight))

pygame.display.set_caption("Crêpe party")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
char = pygame.image.load('standing.png')

bg = pygame.image.load('FondNormale.png')
bgX = 0
bgX2 = bg.get_width()

clock = pygame.time.Clock()

class joueur(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
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
        for objectt in objects:
            if not(objectt.collision(self.hitbox)) and poele.y < 540 - poele.height:
                poele.y += 4
                poele.istombe = True


class longuePlateforme(object):
    def __init__(self, x, y, width, height, nb, type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.nb = nb
        self.type = type
        self.hitbox = (x,y,width*nb,height)
        self.count = 0

    def draw(self,win):
        for i in range(self.nb):
            self.hitbox = (self.x, self.y, self.width, self.height)
            cube = plateforme(self.x+i*self.width,self.y, self.width,self.height, self.type)
            cube.draw(win)

    def collision(self,rect):
        if self.hitbox[1] > sol.y:
            return True
        else:
            if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2] * self.nb:
                if rect[1] < self.hitbox[3] + self.hitbox[1] and rect[1] + rect[3] > self.hitbox[1]:
                    if ((rect[1] + rect[3]) <= (self.hitbox[1] + self.hitbox[3]/2)) and ((rect[1] + rect[3]) >= (self.hitbox[1] -50)):
                        poele.y = self.hitbox[1] - 5 - poele.height
                        poele.isJump = False
                        poele.jumpCount = 10

                    if ((rect[1]) >= (self.hitbox[1] + self.hitbox[3]/2)) and (rect[1]) <= (self.hitbox[1] +self.hitbox[3]+20):
                        poele.y = self.hitbox[1] + self.hitbox[3]+ 5
                        print("stop")
                        poele.isJump = False
                        poele.jumpCount = 10

                    if rect[0] < self.hitbox[0] and rect[1] +rect[3] > self.hitbox[1]+20:  #collision a droite
                        poele.x -= 5
                    elif rect[0] + rect[2] > self.hitbox[0] and rect[1] +rect[3] > self.hitbox[1]+20:
                        poele.x += 5
                    return True
            return False


class plateforme(object):
    img = [pygame.image.load('../image/BlockFour.png'),pygame.image.load('../image/CommodeBlock.png'),pygame.image.load('../image/LaveVaiselleBlock.png')]
    def __init__(self, x, y, width, height, type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = type
        self.hitbox = (x,y,width,height)
        self.count = 0

    def draw(self,win):
        self.hitbox = (self.x,self.y, self.width,self.height)
        win.blit(self.img[self.type], (self.x,self.y))
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)



def redrawGameWindow():
    global walkCount
    win.blit(bg, (bgX,0))
    win.blit(bg, (bgX2,0))
    poele.draw(win)
    #sol.draw(win)
    for x in objects:
        x.draw(win)
    pygame.display.update()


sol = longuePlateforme(0,600,64,64,20,0)
poele = joueur(300, 500, 64, 64)
pygame.time.set_timer(pygame.USEREVENT+1,2750)

objects = []

run = True
while run:
    clock.tick(30)

    for objectt in objects:
        if objectt.collision(poele.hitbox):
            a = 6
        objectt.x -= 3.4
        if objectt.x < -objectt.width * objectt.nb:
            objects.pop(objects.index(objectt))
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
            objects.append(longuePlateforme(1000,random.randrange(350,500),64,64,random.randrange(1,5),random.randrange(0,3)))

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

    if not(poele.isJump):
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            poele.isJump = True
            poele.left = False
            poele.right = False
            poele.walkCount = 0
        else:
            poele.tomber(objects)
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


    redrawGameWindow()

pygame.quit()
