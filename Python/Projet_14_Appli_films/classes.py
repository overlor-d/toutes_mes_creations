import pygame
from PIL import Image

class Rectangle:

    def __init__(self, w, h, color, groupe,co = [0,0], bordure = "", arrondi = 0, margin = 0):
        self.groupe = groupe

        self.wid = w
        self.hei = h

        self.x = co[0]
        self.y = co[1]
        self.co = co

        self.couleur = color
        self.pos = bordure
        self.arrondi = arrondi
        self.margin = margin

        self.timer = [0,False,5]


    def affichage(self,ecran,coef_divi):
        self.rect = pygame.Rect(( (self.x + self.margin) // coef_divi, self.y // coef_divi ), ( (self.wid - (self.margin*2)) // coef_divi, self.hei // coef_divi ))
        pygame.draw.rect(ecran, self.couleur, self.rect, 0, self.arrondi // coef_divi)

    def bordure_rect(self,ecran,coef_divi):
        if self.pos == "haut":
            pygame.draw.rect(ecran, (self.couleur[0] + 15, self.couleur[1] + 15, self.couleur[2] + 15 ), pygame.Rect(( (self.x + self.margin) // coef_divi, self.y // coef_divi ), ( (self.wid - (self.margin*2)) // coef_divi, 20 // coef_divi )), 0, self.arrondi // coef_divi)
        elif self.pos == "bas":
            pygame.draw.rect(ecran, (self.couleur[0] + 15, self.couleur[1] + 15, self.couleur[2] + 15 ), pygame.Rect(( (self.x + self.margin) // coef_divi, (self.y + self.hei -20) // coef_divi ), ( (self.wid - (self.margin*2)) // coef_divi, 20 // coef_divi )), 0, self.arrondi // coef_divi)
        elif self.pos == "gauche":
            pygame.draw.rect(ecran, (self.couleur[0] + 15, self.couleur[1] + 15, self.couleur[2] + 15 ), pygame.Rect(( (self.x + self.margin) // coef_divi, self.y // coef_divi ), ( ((self.wid - (self.margin*2)) - (self.wid -20)) // coef_divi, self.hei // coef_divi )), 0, self.arrondi // coef_divi)
        elif self.pos == "droite":
            pygame.draw.rect(ecran, (self.couleur[0] + 15, self.couleur[1] + 15, self.couleur[2] + 15 ), pygame.Rect(( ((self.x + self.margin) + self.wid -20) // coef_divi, self.y // coef_divi ), ( ((self.wid - (self.margin*2)) - (self.wid -20)) // coef_divi, self.hei // coef_divi )), 0, self.arrondi // coef_divi)
        elif self.pos == "tot":
            pygame.draw.rect(ecran, (self.couleur[0] + 15, self.couleur[1] + 15, self.couleur[2] + 15 ), pygame.Rect(( (self.x + self.margin) // coef_divi, self.y // coef_divi ), ( (self.wid - (self.margin*2)) // coef_divi, self.hei // coef_divi )), 20 // coef_divi, self.arrondi // coef_divi)
        else :
            pass

    def led(self,ecran,coef_divi):
        if self.pos == "haut":
            pygame.draw.rect(ecran, (150,45,45), pygame.Rect(( (self.x + self.margin) // coef_divi, self.y - 4 // coef_divi ), ( (self.wid - (self.margin*2)) // coef_divi, 4 // coef_divi )), 0, self.arrondi // coef_divi)
        elif self.pos == "bas":
            pygame.draw.rect(ecran, (150,45,45), pygame.Rect(( (self.x + self.margin)// coef_divi, (self.y + self.hei) // coef_divi ), ( (self.wid - (self.margin*2)) // coef_divi, 4 // coef_divi )), 0, self.arrondi // coef_divi)
        elif self.pos == "tot":
            pygame.draw.rect(ecran, (150,45,45), pygame.Rect(( ((self.x + self.margin) - 4) // coef_divi, (self.y - 4) // coef_divi ), ( ((self.wid - (self.margin*2)) + 4) // coef_divi, (self.hei + 4) // coef_divi )), 4, self.arrondi // coef_divi)
        else :
            pass

    def clignotement(self, scene, id, place):

        self.timer[0] += 1
        if self.timer[0] == self.timer[2]:
            self.timer[0] = 0
            if self.timer[1] == False:
                self.timer[1] = True
                scene.insert(place,id)
                self.timer[2] = 20
            else :
                self.timer[1] = False
                if scene[place] == id:
                    scene.pop(place)
                    self.timer[2] = 5
        return scene

    def reini_co(self):
        self.x = self.co[0]
        self.y = self.co[1]

class Im:

    def __init__(self, groupe, nom_image, co = [0,0]):
        self.x = co[0]
        self.y = co[1]
        self.co = co

        self.groupe = groupe
        self.chemin = "Images/" + nom_image

        self.image = Image.open(self.chemin)
        self.timer = [0]

        self.sizes = [self.image.size[0],self.image.size[1]]

    def affichage(self,ecran,coef_divi):
        ecran.blit(pygame.transform.scale(pygame.image.load(self.chemin),(self.sizes[0] // coef_divi,self.sizes[1] // coef_divi)),(self.x // coef_divi, self.y // coef_divi))

    def bouton(self,co_souris,coef_divi,coef_2 = 1):
        cosour = int((co_souris[0] - self.x // coef_divi)),int((co_souris[1] - self.y // coef_divi))

        dim_img = int(self.image.size[0] // coef_divi // coef_2),int(self.image.size[1] // coef_divi // coef_2)
        image = self.image.resize((dim_img))

        if (co_souris[0] > self.x // coef_divi and co_souris[1] > self.y // coef_divi and co_souris[0] < (self.x // coef_divi + dim_img[0]) and co_souris[1] < (self.y // coef_divi + dim_img[1])):

            couleurs=image.getpixel((cosour))

            if couleurs != 0:

                if len(couleurs) > 3:
                    if couleurs[3] == 0:
                        return False
                    else:
                        return True
                else :
                    return True
            else :
                return True
        else :
            return False

    def resi(self):
        self.sizes[0] = self.sizes[0] // 2
        self.sizes[1] = self.sizes[1] // 2

    def reini_resi(self):
        self.sizes[0] = self.image.size[0]
        self.sizes[1] = self.image.size[1]

    def reini_co(self):
        self.x = self.co[0]
        self.y = self.co[1]

class Txt:

    def __init__(self,x,y,txt,couleur,coef_divi, t_font):

        self.x = x
        self.y = y
        self.couleur = couleur

        self.txt = txt
        self.font = pygame.font.Font(None, t_font // coef_divi)
        self.surface = self.font.render(self.txt, True, self.couleur)

    def ajouter(self, t):
        self.txt += t
        self.surface = self.font.render(self.txt, True, self.couleur)

    def suprimer(self):
        self.txt = self.txt[:-1]
        self.surface = self.font.render(self.txt, True, self.couleur)

    def res(self):
        self.txt = ""
        self.surface = self.font.render(self.txt, True, self.couleur)

    def affichage(self,ecran,coef_divi):
        self.surface = self.font.render(self.txt, True, self.couleur)
        ecran.blit(self.surface, (self.x // coef_divi, self.y // coef_divi))

    def saut_ligne(self):
        self.surface.get_width()

    def __str__(self):
        return self.txt