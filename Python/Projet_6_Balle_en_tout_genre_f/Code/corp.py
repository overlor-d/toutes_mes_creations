"""
Amélioration apportées au programme :
    
    - Ajout d'une fonction qui change la gravité lorsque l'on appuit sur espace

    - Déplacement à gauche ou a droite de la fontaine avec les flèches du clavier

    - Lorsque vous appuyez sur la touche v cela déclenche un loup touche touche entre 20 balles. Lorsque toutes les balles sont touchées
    la fontaine redemarre. Plusieurs méthodes on donc été crées 


Difficultés rencontrées :

    - La collision des balles → impossible de les empiler en mode
    fontaine peut-être trop de calcul et une formule pas assez simplifié de ma part
    j'ai donc désactivé les collisions dans ce mode et modifié la formule afin de ne juste avoir des collisions simple sur la
    scene loup touche touche

    - Parfois malgré que les balles rouge touchent les blanches il ne se passe rien le chagement de couleur de ne se fait
    pas même si la collision a lieu je n'ai pas trouvé la solution au problème

But atteint:
    oui en quelque sorte
        à la base, je ne voulais pas faire un loup touche touche, mais avec le temps donné en plus je trouvais que mes
        modifications étaient trop légères. Ce que j'aurais aimé pouvoir faire, c'est une intelligence artificielle
        qui irai chercher les balles à toucher, j'ai réussi à la créer, mais je n'ai pas réussi à l'incorporer dans mon programme.
        Cela générait des baisses de fps et donc rendait le programme inutilisable sans doute par manque d'optimisation
        de ma part. Je me suis donc rabattu sur quelque chose de plus simple où je pouvais combiner mes deux scenes.
"""


import pyxel
from random import randint
from math import *

# rayon des balles
global rayon ; rayon = 10

# taille de l'écran
global cote ; cote = 700

# gravite négative ou positive ou nulle
gravite = 1

# coordonnées abscisse de la fontaine
x_fontaine = cote//2

# scene loup touche touche ou fontaine
scene = 0

class Balle :
    '''
    objet Balle avec ses coordonnées son différentiel en x et en y
    '''
    # le constructeur
    def __init__(self, couleur):
        global gravite , x_fontaine 

        # deplacement de la fontaine avec la touche fleche gauche
        if pyxel.btnr(pyxel.KEY_LEFT):
            if x_fontaine - 50 > 0:
                x_fontaine -= 50

        
        # deplacement de la fontaine avec la touche fleche gauche
        elif pyxel.btnr(pyxel.KEY_RIGHT):
            if x_fontaine + 50 < cote:
                x_fontaine += 50


        self.x = x_fontaine
        self.y = cote // 2

        # changement de la direction de projection des balles au changement de gravité
        if gravite == 1:
            self.dy = randint(-20,-10)
        else :
            self.dy = randint(10,20)

        self.dx = randint(-10,10)

        self.couleur = couleur # couleurs entre 0 et 15
        temps_secondes = 8 # secondes
        self.temps_vie = 20*temps_secondes # il y a 30 images par seconde
        
        
        


# =====================================================
# == La class qui définit l'animation
# =====================================================    

class Anim:
    # le constructeur
    def __init__(self):
        # taille de la fenetre cote * cote pixels
        pyxel.init(cote, cote, title="Fontaine de balles rebondissantes")
       
        # les balles
        self.couleur = 1
        # notre liste de balles qui n'en contient qu'une pour commencer
        self.balles = [Balle(self.couleur)]
        
        # pour exécuter le jeu
        pyxel.run(self.update, self.draw)
    
    
    
    # Des méthodes
    
    def change_couleur(self):
        """
        cette fonction permet de chager la couleur des balles lorsqu'elles apparaissent
        """
        
        self.couleur += 1
        # self.couleur ne peut pas dépassser 15
        if self.couleur == 16:
            # self.couleur ne doit pas valoir 0 sinon les balles sont noires
            self.couleur = 1
            
    def deplacement(self,gravite):
        """déplacement des balles avec les rebonds sur les côtés ou au sol"""

        for b in self.balles :

            if b.x + b.dx > cote or b.x + b.dx < 0 :
                # on touche le mur droit ou gauche
                # on modifie le sens de dx
                b.dx = b.dx * (-1)
            if b.y + b.dy > cote or b.y + b.dy < 0:
                # on touche le sol
                # on modifie le sens de dy et on le divise par 2
                if gravite == 0:
                    b.dy = b.dy * (-1)
                else:
                    b.dy = int(b.dy / (-2))


            # la balle se déplace
            b.x = b.x + b.dx
            b.y = b.y + b.dy
            # on simule la gravité en accélérant dy
            b.dy = b.dy + gravite

            

    def vieillir(self) :
        """ vieillissement et mort des balles"""
        # on crée la liste des balles qui sont périmées
        liste_dead = []
        for i in range(len(self.balles)) :
            self.balles[i].temps_vie -= 1
            if self.balles[i].temps_vie == 0 :
                liste_dead.append(i)
        # on supprime les balles périmées de la liste en commençant par la fin
        for i in range(len(liste_dead)-1,-1,-1) :
            self.balles.pop(i)

    def gravite(self):
        "changerment de la gravite des balles vers le haut ou vers le bas"
        global gravite
        if pyxel.btnr(pyxel.KEY_SPACE):
            if gravite == 1:
                gravite = -1
            elif gravite == -1:
                gravite = 1
            
    def changement_scene(self):
        '''
        Quand on appuit sur v cela déclenche le loup touche touche
        '''
        global scene
        if pyxel.btnr(pyxel.KEY_V):
            if scene == 0:
                self.balles = [] 
                #On met les balles à la même vitesse
                for k in range(len(self.balles)):
                    self.balles[k].dy = 5
                    self.balles[k].dx = 5
                scene = 1
            else:
                scene = 0
        return scene

    def deplacement_collision(self):
        """déplacement des balles avec les rebonds sur les côtés ou au sol + ajout des collision entre 
        les balles en prenant le point central de deux balles 
        puis on vérifie que la distance entre ces deux points est inférieure à la somme des rayons de ces deux cercles"""

        for b in self.balles :

            if b.x + b.dx > cote or b.x + b.dx < 0 :
                # on touche le mur droit ou gauche
                # on modifie le sens de dx
                b.dx = b.dx * (-1)
            if b.y + b.dy > cote or b.y + b.dy < 0:
                # on touche le sol
                # on modifie le sens de dy et on le divise par 2
                
                b.dy = b.dy * (-1)

            #on verifie pour chacune des balles que peut rencontrer b
            for k in self.balles:
                #on ecarte b pour eviter qu'il soit en collision avec lui même
                if k != b:
                    
                    #variable de calcul pour la distance de collision
                    distance_entre_balles = sqrt((b.x - k.x)**2 + (b.y - k.y)**2)

                    #on change la couleur
                    if distance_entre_balles <= rayon*2:
                        if b.couleur == 8:
                            k.couleur = 8 
                        b.dx = b.dx * (-1)
                        k.dx = k.dx * (-1)
                        b.dy = b.dy * (-1)
                        k.dy = k.dy * (-1)

            # la balle se déplace
            b.x = b.x + b.dx
            b.y = b.y + b.dy
            
            
    def test_couleur(self):
        '''
        On test si toutes les balles sont rouge et si oui alors renvoyer True
        '''

        toute_balles_rouge = True
        for k in self.balles:
            if k.couleur == 7:
                toute_balles_rouge = False

        return toute_balles_rouge

    
    # update

    def update(self):
        """mise à jour des variables (30 fois par seconde)"""
        # on effectue les mises à jour éventuelles
        
        global scene
        
        self.changement_scene()

        #scene 0 fontaine à balle
        if scene == 0:
            
            self.change_couleur()
            self.gravite()
            self.deplacement(gravite)
            self.vieillir()
            # on rajoute une nouvelle balle

            self.balles.append(Balle(self.couleur)) 
                
        # scene 1 loup touche touche 
        elif scene == 1:
            
            self.deplacement_collision()
            
            #on créer seulement 20 balles de couleur blanche et une seule de couleur rouge avec une position aléatoire
            if len(self.balles) < 20:
                self.balles.append(Balle(7)) 
                if len(self.balles) == 20:
                    self.balles[0].couleur = 8
                    self.balles[0].x = randint(0,cote)
                    self.balles[0].y = randint(0,cote)
            
            #on change la scene
            if  self.test_couleur():
                scene = 0
            
            
      

    # draw

    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""
        # vide la fenêtre
        pyxel.cls(0)
        
        # on dessine les balles
        for b in self.balles :
            
            pyxel.circ(b.x, b.y, rayon, b.couleur)         


Anim()