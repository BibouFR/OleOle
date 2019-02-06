import pygame
from pygame import *
from random import *

class Crepes:
    def __init__(self, difficulte):        #Crée une crêpe en fonction de la difficulté renvoie une liste d'ingrédients
        ingredientsDisponibles = ["Oeuf","Fromage","Jambon","Cornichon", "Champignons", "Salade", "Tomate", "Nutella", "Sucre", "Miel", "Confiture", "Citron", "Chantilly"]
        ingredientsSales = ingredientsDisponibles[:7]
        ingredientsSucres = ingredientsDisponibles[7:]
        self.ingredients = []
        self.difficulte = difficulte
        a = choice(ingredientsDisponibles)
        if a in ingredientsSales:                           #RESPECTE LES CREPES SALES
            ingredientsDisponibles=ingredientsSales         #ET LES CREPES SUCRES
        else:                                               #PAS DE MELANGE ptdr
            ingredientsDisponibles=ingredientsSucres
        b = a
        self.ingredients.append(a)
        while b in self.ingredients:
            b = choice(ingredientsDisponibles)
        self.ingredients.append(b)
        if difficulte >= 1:                             #Si la difficulte c'est normal ou difficile : 3 ingredients
            c = b
            while c in self.ingredients:
                c = choice(ingredientsDisponibles)
            self.ingredients.append(c)
            if difficulte>=2:                           #Si c'est difficile : 4 ingredients
                d = c
                while d in self.ingredients:
                    d = choice(ingredientsDisponibles)
                self.ingredients.append(d)
    def afficherCrepe(self):
        if self.difficulte==1:
            difstr="normale"
        elif self.difficulte>=2:
            difstr="difficile"
        else:
            difstr="facile"
        print("Recette "+difstr + " :")
        print("Ingrédients : ")
        for i in range(0,len(self.ingredients)):
            print("\t- "+self.ingredients[i])

def rectangle(win, couleur, hitbox):
    pygame.draw.rect(win, couleur, hitbox, 2)

def AfficheRecette(win, x, y, crepe):
    #COULEURS
    blanc = (255,255,255)
    rouge = (255,0,0)
    vert = (0,255,0)
    jaune = (255,215,0)

    #GESTION DES DIFFICULTES
    if crepe.difficulte==1:
        difstr="Normal"
        couldif = jaune
    elif crepe.difficulte>=2:
        difstr="Difficile"
        couldif = rouge
    else:
        difstr="Facile"
        couldif = vert

    #DIMENSIONS + TEXTES
    crect1 = (x,y,150,50)
    crect2 = (x, y+50, 150,50*len(crepe.ingredients))
    rectangle(win, blanc, crect1)
    rectangle(win, blanc, crect2)

    police = pygame.font.SysFont("freesans",20)

    texte = police.render(difstr, True, couldif)
    positDiff = texte.get_rect()
    positDiff.centerx = x+crect1[2]/2
    positDiff.centery = y+crect1[3]/2

    win.blit(texte, positDiff)

    nb = 25
    for ing in crepe.ingredients:
        texte = police.render(ing, True, blanc)
        position = texte.get_rect()
        position.centerx = crect2[0]+crect2[2]/2
        position.centery = crect2[1]+nb
        win.blit(texte, position)
        nb += 50

    pygame.display.flip()
