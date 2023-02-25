import pygame

from projectile import Projectile
from projectile2 import Projectile2



#classe du joueur

class Joueur(pygame.sprite.Sprite):

    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        self.vie = 100
        self.max_vie = 100
        self.attaque = 50
        self.vitesse = 10
        self.all_projectiles =pygame.sprite.Group()
        self.all_projectiles2 =pygame.sprite.Group()
        self.image = pygame.image.load(r'image/vaisseau1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 620
        self.rect.y = 550

    def lancer_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def lancer_projectile2(self):
        self.all_projectiles2.add(Projectile2(self))



    def mouvement_droit(self):
        if not self.jeu.colision(self, self.jeu.all_meteorite):
            self.rect.x += self.vitesse

    def mouvement_gauche(self):
        if not self.jeu.colision(self, self.jeu.all_meteorite):
            self.rect.x -= self.vitesse

    def mouvement_haut(self):
        if not self.jeu.colision(self, self.jeu.all_meteorite):
            self.rect.y += self.vitesse

    def mouvement_bas(self):
        if not self.jeu.colision(self, self.jeu.all_meteorite):
            self.rect.y -= self.vitesse


