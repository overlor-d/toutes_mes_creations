from os import listdir
from PIL import Image
import os 
import pygame


def initialisation_donnes_images(chemin_dossier,liste_pos_images):
    '''importation des images avec les bonnes taille en fonctione de la longueur et de la largeur de lecran en question redimenssionage possible l'adapation se fait automatiquement'''
    a = []
    #boucle servant a la creation des chemins de chacune des images
    for z in listdir(chemin_dossier):
        if os.path.splitext(z)[1] == (".png" or ".jpg"):
            b = [chemin_dossier+"/"+str(z)]
            a.append(b)
    a.sort()

    #boucle servant a obtenir la taille des images et les ajouter a chacune des listes
    for y in range(len(a)):
        img = Image.open(a[y][0])
        t_img = img.width,img.height
        a[y].append(t_img)

    #boucle servant a ajouter la position des images elles sont adaptable en fonction de la taille de la fenetre
    for x in range(len(a)):
        a[x].append(liste_pos_images[x])

    #boucle servant a importer les images dans pygame
    for w in range(len(a)):
        a[w].append(pygame.image.load(a[w][0]))
    
    
    return a 



def affichage_image(liste_donnees_images,liste_image_a_afficher,screen,liste_co_image,dimension_ecran_base):
    

    #boucle servant a importer les images dans pygame
    for z in range(len(liste_donnees_images)):
        liste_donnees_images[z][3] = (pygame.image.load(liste_donnees_images[z][0]))

    #boucle servant a la redimenssion des images
    for y in range(len(liste_donnees_images)):
        liste_donnees_images[y][3] = pygame.transform.scale(liste_donnees_images[y][3], (liste_donnees_images[y][1][0]/1920*dimension_ecran_base[0], liste_donnees_images[y][1][1]/1080*dimension_ecran_base[1]))

    #boucle servent a adapter les coordonnes des images
    for w in range(len(liste_donnees_images)):
        liste_donnees_images[w][2] = (liste_co_image[w][0]/1920*dimension_ecran_base[0],liste_co_image[w][1]/1080*dimension_ecran_base[1])

    #boucle servant a laffichage des images
    for x in range(len(liste_image_a_afficher)):
        screen.blit(liste_donnees_images[liste_image_a_afficher[x]][3],liste_donnees_images[liste_image_a_afficher[x]][2])
