import pygame
from meteorite import Meteorite
from joueur import Joueur

class Jeu:


    def __init__(self):
        #charger le joueur
        self.all_joueur = pygame.sprite.Group()
        self.joueur1 = Joueur(self)
        self.all_joueur.add(self.joueur1)
        self.all_meteorite = pygame.sprite.Group()
        self.presser = {}
        self.spawn_meteorite()


    def colision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_meteorite(self):
        meteorite = Meteorite(self)
        self.all_meteorite.add(meteorite)
