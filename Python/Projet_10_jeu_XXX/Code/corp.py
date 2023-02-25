##########_____importation des modules_____##########

import pygame
from random import *

pygame.init()

# on fait la taille de la fenêtre en fonction de la taille de l'écran
taille_fenetre = pygame.display.Info() #on recupère les info de l'écran


#condition pour verifier la taille de l'écran et donner les tailles en fonction de celle-ci
if taille_fenetre.current_w > 1920 and taille_fenetre.current_h > 1080 :
    taille_fenetre = [1920, 1080]
elif taille_fenetre.current_w <= 1920 and taille_fenetre.current_h <= 1080:
    taille_fenetre = [taille_fenetre.current_w, taille_fenetre.current_h]


ecran = pygame.display.set_mode((taille_fenetre), pygame.RESIZABLE) #initialisation de la fenêtre
pygame.display.set_caption('') #nom de la fenêtre
pygame.display.set_icon('..') #icone de la fenêtre


#boucle principal
continuer = True
while  continuer:

    #evenements
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
    