from os import listdir
from PIL import Image
import os 
import pygame

class Image_pygame:
    def __init__(self, id, img, x = 110, y = 150):
        chemin = "../../Images/" + str(img)
        image_taille = Image.open(chemin)

        self.num_id = id
        self.image = pygame.image.load(chemin)
        self.x = x
        self.y = y
        self.taille_x = image_taille.width
        self.taille_y = image_taille.height
        self.texte = ""

    def ajouter_txt(self,txt):
        if txt == '/':
            self.texte += "Aucune entrée\n"
        else :
            self.texte += txt + "\n"

    def affichage(self,scr, dim_ecran):
        
        self.image = pygame.transform.scale(self.image, (self.taille_x / 1920*dim_ecran[0],self.taille_y / 1080*dim_ecran[1]))
        x = self.x / 1920 * dim_ecran[0]
        y = self.y / 1080 * dim_ecran[1]
        scr.blit(self.image,(x,y))
