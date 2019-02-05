import pygame
from pygame.locals import *
from random import *

class Perso:

    def __init__(self, droite, gauche, haut, bas):
        # Sprites du personnage
        self.droite = pygame.image.load("image/perso.png").convert_alpha()
        self.gauche = pygame.image.load(gauche).convert_alpha()
        self.haut = pygame.image.load(haut).convert_alpha()
        self.bas = pygame.image.load(bas).convert_alpha()
        # Position du personnage en cases et en pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        # Direction par défaut
        self.direction = self.droite


    def deplacement(self, direction):
        # Déplacement vers la droite
        if direction == 'droite':
            # Pour ne pas dépasser l'écran
            if self.case_x < (nombre_sprite_cote - 1):
                # On vérifie que la case de destination n'est pas un mur
                if self.niveau.structure[self.case_y][self.case_x + 1] != 'm':
                    # Déplacement d'une case
                    self.case_x += 1
                    # Calcul de la position "réelle" en pixel
                    self.x = self.case_x * taille_sprite
            # Image dans la bonne direction
            self.direction = self.droite

        # Déplacement vers la gauche
        if direction == 'gauche':
            if self.case_x > 0:
                if self.niveau.structure[self.case_y][self.case_x - 1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * taille_sprite
            self.direction = self.gauche

        # Déplacement vers le haut
        if direction == 'haut':
            if self.case_y > 0:
                if self.niveau.structure[self.case_y - 1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.haut

        # Déplacement vers le bas
        if direction == 'bas':
            if self.case_y < (nombre_sprite_cote - 1):
                if self.niveau.structure[self.case_y + 1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.bas

class Crepes:
    def __init__(self, difficulte, ingredients):        #Crée une crêpe en fonction de la difficulté renvoie une liste d'ingrédients
        ingredientsDisponibles = ["oeuf","fromage","jambon","cornichon", "champignons", "salade", "tomate", "nutella", "sucre", "miel", "confiture", "citron", "chantilly"]
        ingredientsSales = ingredientsDisponibles[:7]
        ingredientsSucres = ingredientsDisponibles[6:]
        self.ingredients = []
        self.difficulte = difficulte
        a = choice(ingredientsDisponibles)
        if a in ingredientsSales:                           #RESPECTE LES CREPES SALES
            ingredientsDisponibles=ingredientsSales         #ET LES CREPES SUCRES
        else:                                               #PAS DE MELANGE ptdr
            ingredientsDisponibles=inggredientsSucres
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
            print("Recette, difficulté = "+self.difficulte==0?"facile":self.difficulte==1?"Normal":"Difficile" + " :")
            print("Ingrédients : ")
            for i in range(0,len(self.ingredients)):
                print(self.ingredients[i])
