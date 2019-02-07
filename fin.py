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

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
