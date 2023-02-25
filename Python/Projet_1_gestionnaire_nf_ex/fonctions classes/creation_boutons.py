import pygame
import analyse_pixel

def fonction_creation_bouton(coordonnee_souris, coordonnee_bouton,taille_bouton,image,dim_ecran):


    if coordonnee_souris[0] > coordonnee_bouton[0] and coordonnee_souris[1] > coordonnee_bouton[1] and coordonnee_souris[0] < (coordonnee_bouton[0] + taille_bouton[0]/1920*dim_ecran[0]) and coordonnee_souris[1] < (coordonnee_bouton[1] + taille_bouton[1]/1080*dim_ecran[1]) and analyse_pixel.image_transparence(image,coordonnee_souris,coordonnee_bouton,dim_ecran):
        return True
