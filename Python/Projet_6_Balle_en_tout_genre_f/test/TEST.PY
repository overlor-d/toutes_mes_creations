#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 11:45:44 2022
@author: loran
"""


import pyxel
from random import randint

# rayon des balles
global rayon ; rayon = 10

# taille de l'écran
global cote ; cote = 800



class Balle :
    '''
    objet Balle avec ses coordonnées, son différentiel en x et en y
    '''
    # le constructeur
    def __init__(self, couleur):
        self.x = cote//2
        self.y = cote//3
        self.dx = randint(-10,10)
        self.dy = randint(-20,-10)
        self.couleur = couleur #couleurs entre 0 et 15
        temps_secondes = 8 # secondes
        self.temps_vie = 30*temps_secondes # il y a 30 images par seconde
    
    
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
    
    
    # =====================================================
    # == Des méthodes
    # =====================================================
    def change_couleur(self):
        """change les couleurs de toutes les nouvelles balles
        si on appuye sur la touche espace"""
        if pyxel.btnr(pyxel.KEY_SPACE):
            self.couleur += 1
            # self.couleur ne peut pas dépassser 15
            if self.couleur == 16:
                # self.couleur ne doit pas valoir 0 sinon les balles sont noires
                self.couleur = 1
            
    def deplacement(self):
        """déplacement des balles avec les rebonds sur les côtés ou au sol"""
        for b in self.balles :
            if b.x + b.dx > cote or b.x + b.dx < 0:
                # on touche le mur droit ou gauche
                # on modifie le sens de dx
                b.dx = b.dx * (-1)
            if b.y + b.dy > cote :
                # on touche le sol
                # on modifie le sens de dy et on le divise par 2
                b.dy = int(b.dy / (-2))
            # la balle se déplace
            b.x = b.x + b.dx
            b.y = b.y + b.dy
            # on simule la gravité en accélérant dy
            b.dy = b.dy + 1
    
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
            

    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """mise à jour des variables (30 fois par seconde)"""
        # on effectue les mises à jour éventuelles
        self.change_couleur()
        self.deplacement()
        self.vieillir()
        # on rajoute une nouvelle balle
        self.balles.append(Balle(self.couleur))   
    
      
    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""
        # vide la fenêtre
        pyxel.cls(0)

        # on dessine les balles
        for b in self.balles :
            pyxel.circ(b.x, b.y, rayon, b.couleur)
    
        
Anim()