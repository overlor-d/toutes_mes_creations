'''
Ce programme est un gestionnaire qui permet de gerer vos mots de passe et votre calendrier personnel ainsi qu une troisieme action qui sera rajoute dans une prochaine maj
'''
#import des modules
import pygame
from random import randint
from os import listdir
#importation des fonctions
import sys
sys.path.insert(0,"../../fonctions classes")
import initialisation_images
import creation_boutons
import deplacement_images
import classe_img_mdp


################################################################################


#initialisation


################################################################################

#initialisation du module pygame
pygame.init()
pygame.mixer.init()
pygame.key.set_repeat()

#configuration de la fenetre

pygame.display.set_caption("Gestionnaire personnel")

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
dimension_ecran_base = screen.get_size()

if dimension_ecran_base[0] < 1920 or dimension_ecran_base[1] < 1080:
    screen = pygame.display.set_mode((dimension_ecran_base[0]//1.2,dimension_ecran_base[1]//1.2))
else :
    screen = pygame.display.set_mode((1920,1080))

''',pygame.RESIZABLE'''
#importation de l'icone de la fenetre

pygame.display.set_icon(pygame.image.load('../../Images/ZZZ-mini_logo_overwatch.ico'))

#initialisation des variables
marche = True
barre_rangee = False
coef_add = 30/1080*dimension_ecran_base[1]
clock = pygame.time.Clock()
scene = [True,False,False]

'''
scene 0 = Menu principal
scene 1 = touchpad
scene 2 = mdp
'''

key_pressees = []
timer = 5

code_mdp_saisi = []
image_etoiles_code = []


verif_scene_2 = False


#variable
liste_co_image = [
    #Arriere-plan   0
    [0,0],
    #banniere bas   1
    [0,810],
    #bar logo   2
    [0,0],
    #bouton baisser baniere 3
    [1871,760],
    #bouton lever la banniere   4
    [1870,995],
    #boutons 1 mdp  5
    [652.5,845.5],
    #boutons 2 calendrier   6
    [1016.5,845.5],
    #boutons 3 xxx  7
    [1176.5,845.5],
    #ligne rangee   8
    [0,1050],
    #logo-overwatch 9
    [633,215],
    #boutons 1 mdp appuye   10
    [652.5,845.5],
    #boutons 2 calendrier appuye    11
    [1016.5,845.5],
    #boutons 3 xxx appuye   12
    [1176.5,845.5],
    #etoile 1   13
    [788,310],
    #etoile 2   14
    [880,310],
    #etoile 3   15
    [982,310],
    #etoile 4   16
    [1077,310],
    #panel code     17
    [761,271],
    #touche 0   18
    [909,854],
    #touche 1   19
    [780,464],
    #touche 2   20
    [910,464],
    #touche 3   21
    [1040,464],
    #touche 4   22
    [779,594],
    #touche 5   23
    [909,594],
    #touche 6   24
    [1039,594],
    #touche 7   25
    [779,724],
    #touche 8   26
    [909,724],
    #touche 9   27
    [1039,724],
    #bar mdp    28
    [0,0] 
]


liste_co_image_originel = liste_co_image.copy()



#creation des listes
liste_donnees_images = initialisation_images.initialisation_donnes_images("../../Images",liste_co_image)


liste_touche_pygame = [pygame.K_KP0,pygame.K_KP1,pygame.K_KP2,pygame.K_KP3,pygame.K_KP4,pygame.K_KP5,pygame.K_KP6,pygame.K_KP7,pygame.K_KP8,pygame.K_KP9]


code_scene_1 = [0,0,0,0]


################################################################################


#fonctions


################################################################################


def pave_num_code():
    global code_mdp_saisi
    global image_etoiles_code
    global boutonstouchpad
    global scene
    global timer
    global code_scene_1

    if len(code_mdp_saisi)== 4:
        code_mdp_saisi = []
        image_etoiles_code = []
        code_mdp_saisi.append(boutonstouchpad)

        if len(image_etoiles_code) == 0:
            image_etoiles_code.append(13)
        elif len(image_etoiles_code) == 1:
            image_etoiles_code.append(14)
        elif len(image_etoiles_code) == 2:
            image_etoiles_code.append(15)
        elif len(image_etoiles_code) == 3:
            image_etoiles_code.append(16)
            pygame.display.update()

    else :
        code_mdp_saisi.append(boutonstouchpad)
        if len(image_etoiles_code) == 0:
            image_etoiles_code.append(13)
        elif len(image_etoiles_code) == 1:
            image_etoiles_code.append(14)
        elif len(image_etoiles_code) == 2:
            image_etoiles_code.append(15)
        elif len(image_etoiles_code) == 3:
            image_etoiles_code.append(16)

    
    if code_mdp_saisi == code_scene_1:
        for num_scene in range(len(scene)):
            if num_scene == 2:
                scene[num_scene] = True
            else :
                scene[num_scene] = False

    if len(code_mdp_saisi)== 4:

        while timer != 0:
            initialisation_images.affichage_image(liste_donnees_images, image_etoiles_code, screen, liste_co_image, dimension_ecran_base)
            pygame.display.update()
            timer -= 1
        timer = 5
        image_etoiles_code = []
        code_mdp_saisi = []


#creation des ligne de mdp
def creation_liste_mdp():
    fichier_mdp = open(r"../../Fichiers/mdp.txt", "r")
    nbr_ligne_fichier = fichier_mdp.readlines()
    
    fichier_mdp.close()
    return nbr_ligne_fichier



################################################################################


#corp du programme


################################################################################



while marche:
    dimension_ecran_base = screen.get_size()
    if scene[0]:
        time = clock.tick(60)

        #initialisation de toutes les variables qui ont besoin detre reutilisee

        image_scene_1 = [0,9,2,1,5,6]


        initialisation_images.affichage_image(liste_donnees_images,image_scene_1,screen,liste_co_image,dimension_ecran_base)


    elif scene[1]:
        time = clock.tick(60)

        #initialisation de toutes les variables qui ont besoin detre reutilisee
        image_scene_2 = [0,9,2,17,18,19,20,21,22,23,24,25,26,27]
        initialisation_images.affichage_image(liste_donnees_images, image_scene_2, screen, liste_co_image, dimension_ecran_base)
        initialisation_images.affichage_image(liste_donnees_images, image_etoiles_code, screen, liste_co_image, dimension_ecran_base)

    elif scene[2]:
        time = clock.tick(60)
        
        if verif_scene_2 == False:
            liste_lignes_mdp_jean = creation_liste_mdp()
            liste_mdp = []
            

            #creation des classes des mdp
            for k in range(len(liste_lignes_mdp_jean)//3):
                liste_mdp.append(classe_img_mdp.Image_pygame(k,"BC- bar mdp.png",y = 200*k + 150))
            mdp = 0
            for k in range(0,len(liste_lignes_mdp_jean),3):
                liste_mdp[mdp].ajouter_txt(liste_lignes_mdp_jean[k])
                liste_mdp[mdp].ajouter_txt(liste_lignes_mdp_jean[k+1])
                liste_mdp[mdp].ajouter_txt(liste_lignes_mdp_jean[k+2])
                if k % 3 == 0:
                    mdp += 1    

            

            verif_scene_2 = True

        image_scene_3 = [0]
        initialisation_images.affichage_image(liste_donnees_images, image_scene_3, screen, liste_co_image, dimension_ecran_base)

        #initialisation de toutes les variables qui ont besoin detre reutilisee
        for k in range(len(liste_mdp)):
            liste_mdp[k].affichage(screen,dimension_ecran_base)

        image_scene_3 = [2]
        initialisation_images.affichage_image(liste_donnees_images, image_scene_3, screen, liste_co_image, dimension_ecran_base)
        
    pygame.display.update()
    dimension_ecran_base = screen.get_size()


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
                marche = False
                pygame.quit()

        if event.type == pygame.MOUSEWHEEL:
                
                if scene[2]:
                    if event.y > 0 and liste_mdp[-1].y < 200*(len(liste_mdp)-1)+150:
                        for k in range(len(liste_mdp)):
                            liste_mdp[k].y += 150

                    if event.y < 0 and liste_mdp[0].y > -200*(len(liste_mdp)-4.5)+150:
                        for k in range(len(liste_mdp)):
                            liste_mdp[k].y -= 150

                    

               


        #condition si click gauche est utilise
        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) :

            #changement de couleurs des boutons scene principale
            if scene[0] :

                for num_boutons_chagement in range(2):
                    if creation_boutons.fonction_creation_bouton(pygame.mouse.get_pos(), liste_donnees_images[5+num_boutons_chagement][2], liste_donnees_images[5+num_boutons_chagement][1], liste_donnees_images[5+num_boutons_chagement][0],dimension_ecran_base) and event.button == 1:

                        while timer != 0:

                            #changement de la couleur du bouton 1
                            initialisation_images.affichage_image(liste_donnees_images, [10+num_boutons_chagement], screen, liste_co_image, dimension_ecran_base)
                            pygame.display.update()
                            timer -= 1

                        timer = 5

                        if 5 + num_boutons_chagement == 5:
                            for num_scene in range(len(scene)):
                                if num_scene == 1:
                                    scene[num_scene] = True
                                else :
                                    scene[num_scene] = False

                            deplacement_images.deplacement_images(liste_co_image,[9],0,100/1080*dimension_ecran_base[1])


            #appui sur les touche du panel code
            if scene[1]:

                for boutonstouchpad in range(10):

                    if  creation_boutons.fonction_creation_bouton(pygame.mouse.get_pos(), liste_donnees_images[18+boutonstouchpad][2], liste_donnees_images[18+boutonstouchpad][1], liste_donnees_images[18+boutonstouchpad][0],dimension_ecran_base) and event.button == 1:
                        pave_num_code()

        #touche retour base
        if event.type == pygame.KEYDOWN:

            if scene[1]:
                if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                    if len(code_mdp_saisi) != 0:
                        code_mdp_saisi.pop(-1)
                        image_etoiles_code.pop(-1)


                for boutonstouchpad in range(10):

                    if  event.key == liste_touche_pygame[boutonstouchpad]:
                        pave_num_code()

            if event.key == pygame.K_ESCAPE :
                
                if scene[0] == False :
                    for num_scene in range(len(scene)):
                        if num_scene == 0:
                            scene[num_scene] = True
                        else :
                            scene[num_scene] = False

                        for liste_originel in range(len(liste_co_image_originel)):
                            liste_co_image[liste_originel]= liste_co_image_originel[liste_originel]
                elif scene[0] == True:
                    pygame.quit()
                    
                    