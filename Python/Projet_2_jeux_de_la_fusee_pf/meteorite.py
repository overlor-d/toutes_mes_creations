import pygame
from random import randint



class Meteorite(pygame.sprite.Sprite):


    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        self.vie = 100
        self.max_vie = 100
        self.image = pygame.image.load(r'image/meteorite.png')
        self.image = pygame.transform.scale(self.image, (150, 70))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 1060)
        self.rect.y = 10
        self.vitesse = randint(1, 3)

    def degat(self, montant_degat):
        self.vie -= montant_degat

        if self.vie <=0 :
            self.rect.x = randint(0, 1060)
            self.rect.y = 10
            self.vie = self.max_vie
            self.vitesse = randint(3, 5)



    def barre_vie(self, surface):
        barre_couleur = (112, 218, 72)
        barre_arrierre_couleur = (255, 255, 255)


        barre_position = [self.rect.x + 20, self.rect.y, self.vie, 5]

        barre_arrierre_position = [self.rect.x + 20, self.rect.y, self.max_vie, 5]

        pygame.draw.rect(surface, barre_arrierre_couleur, barre_arrierre_position)
        pygame.draw.rect(surface, barre_couleur, barre_position)



    def avancer(self):

        if self.rect.y >= 720 :
            self.rect.x = randint(0, 1060)
            self.rect.y = 10
            self.vie = self.max_vie
            self.vitesse = randint(3, 5)



        if not self.jeu.colision(self, self.jeu.all_joueur):
            self.rect.y += self.vitesse

        if self.jeu.colision(self, self.jeu.all_joueur):
            temps_image_explosion = 120
            while temps_image_explosion >= 0:
                self.image = pygame.image.load(r'image/explosion.png')
                self.image = pygame.transform.scale(self.image, (150, 150))
                temps_image_explosion-=1
            self.image = pygame.image.load(r'image/meteorite.png')
            self.image = pygame.transform.scale(self.image, (150, 70))
            self.rect.x = randint(0, 1060)
            self.rect.y = 10
            self.vie = self.max_vie
            self.vitesse = randint(3, 5)









