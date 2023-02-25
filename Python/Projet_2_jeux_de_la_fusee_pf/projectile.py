import pygame

#définbition de la classe du projectile


class Projectile(pygame.sprite.Sprite):


    def __init__(self, joueur1):
        super().__init__()
        self.joueur1 = joueur1
        self.vitesse = 30
        self.image = pygame.image.load(r'image/projectile.png')
        self.rect = self.image.get_rect()
        self.rect.x = joueur1.rect.x + 32
        self.rect.y = joueur1.rect.y - 40


    def remove(self):
        self.joueur1.all_projectiles.remove(self)

    def move(self):
        self.rect.y -= self.vitesse

        if self.rect.y <= -50 :
            self.remove()

        for meteorite in self.joueur1.jeu.colision(self, self.joueur1.jeu.all_meteorite):
            self.remove()
            meteorite.degat(self.joueur1.attaque)
