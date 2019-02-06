import pygame
from pygame import *
from random import *

class Crepes:
    def __init__(self, difficulte):        #Crée une crêpe en fonction de la difficulté renvoie une liste d'ingrédients
        ingredientsDisponibles = ["Oeuf","Fromage","Jambon","Cornichon", "Champignons", "Salade", "Tomate", "Nutella", "Sucre", "Miel", "Confiture", "Citron", "chantilly"]
        ingredientsSales = ingredientsDisponibles[:7]
        ingredientsSucres = ingredientsDisponibles[6:]
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

def tableau(win, hitbox):
    pygame.draw.rect(win, (255,0,0), hitbox, 2)

pygame.init()
winwidth=500
winheight=400
win = pygame.display.set_mode((winwidth,winheight))

testcr = Crepes(1)
print(testcr.ingredients)
testcr.afficherCrepe()

hitbox = (100,100,100,100)

pygame.draw.rect(win, (255,255,255), hitbox, 2)
pygame.display.flip()

a=True
while a:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False

pygame.quit()
