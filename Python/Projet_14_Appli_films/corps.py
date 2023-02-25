##########_____importation des modules_____##########

import pygame
from random import *
from classes import *
from fonctions import *

pygame.init()
clock = pygame.time.Clock()

# on fait la taille de la fenêtre en fonction de la taille de l'écran
taille_fenetre = pygame.display.Info() #on recupère les info de l'écran

#condition pour verifier la taille de l'écran et donner les tailles en fonction de celle-ci
if taille_fenetre.current_w > 1920 and taille_fenetre.current_h > 1080 :
    division_e = 1
    size = [1920 // division_e,1080 // division_e]
    size_w = size[0]
    size_h = size[1]

elif taille_fenetre.current_w <= 1920 and taille_fenetre.current_h <= 1080:
    division_e = 2
    size = [1920 // division_e,1080 // division_e]
    size_w = size[0]
    size_h = size[1]

ecran = pygame.display.set_mode((size)) #initialisation de la fenêtre
pygame.display.set_caption('') #nom de la fenêtre

txt_recher = Txt(1165,40,"",(0,0,0),division_e, 100)

#inscription text
txt_nom = Txt(650,260,"Nom",(200,200,200),division_e, 50)
txt_prenom = Txt(650,410,"Prenom",(200,200,200),division_e, 50)
txt_mdp = Txt(650,560,"Mot de passe",(200,200,200),division_e, 50)
txt_pseudo = Txt(650,710,"Pseudo",(200,200,200),division_e, 50)
txt_identifiant_deja_u = Txt(txt_pseudo.x + 200,txt_pseudo.y,"Identifiant déjà utilisé",(200,0,0),division_e, 50)

#connexion text
txt_mdp_connexion = Txt(650,510,"Mot de passe",(200,200,200),division_e, 50)
txt_pseudo_connexion = Txt(650,360,"Pseudo",(200,200,200),division_e, 50)
txt_mdp_incorect = Txt(txt_mdp_connexion.x + 250,txt_mdp_connexion.y,"Mot de passe incorect",(200,0,0),division_e, 50)
txt_pseudo_incorect = Txt(txt_pseudo_connexion.x + 200,txt_pseudo_connexion.y,"Pseudo non-enregistré",(200,0,0),division_e, 50)

#saisie des informations personnelles pour s'enregistrer
nom_senregistrer = Txt(txt_nom.x +10,txt_nom.y + 60,"",(0,0,0),division_e, 75)
prenom_senregistrer = Txt(txt_prenom.x + 10,txt_prenom.y + 60 , "" , (0,0,0),division_e, 75)
mdp_senregistrer = Txt(txt_mdp.x + 10,txt_mdp.y + 60,"",(0,0,0),division_e, 75)
pseudo_senregistrer = Txt(txt_pseudo.x + 10,txt_pseudo.y + 60,"",(0,0,0),division_e, 75)

#saisie des informations personnelles pour se connecter
mdp_connexion = Txt(txt_mdp_connexion.x + 10,txt_mdp_connexion.y + 60,"",(0,0,0),division_e, 75)
pseudo_connexion = Txt(txt_pseudo_connexion.x + 10,txt_pseudo_connexion.y + 60,"",(0,0,0),division_e, 75)

# création des image qui permettent la conception graphique en évitant des calculs compliqués
fond_princ = Im([0],"fond_princ.png")
logo_compte = Im([1],"logo_account.png", [1800,25])
logo_recher = Im([2],"logo_search.png", [1680,25])
logo_overlo = Im([3],"logo_blanc.png", [890,25])
im_menu = Im([4],"menu.png", [45,25])
barre_recher = Im([5],"barre_re.png", [1150,25])
bouton_pg = Im([2],"bouton change page gauche.png",[840,1140])
bouton_pd = Im([2],"bouton change page droite.png",[980,1140])
cont_senregistrer = Im([2],"senregistrer.png",[1600,210])
cont_connexion = Im([2],"connexion.png",[1600,110])
bouton_senregistrer = Im([2],"senregistrer.png",[800,900])
bouton_connexion = Im([2],"connexion.png",[800,700])
menu_connnexion = Im([2],"connexion.png",[40,110])
cont_deconnexion = Im([2],"deconnexion.png",[1600,110])
menu_bouton_film_vu = Im([2],"films_vu.png",[40,110])
menu_bouton_film_voir = Im([2],"films_a_voir.png",[40,210])


#inscription
rec_nom = Im([5],"barre_re.png", [650,300])
rec_prenom = Im([5],"barre_re.png", [650,450])
rec_mdp = Im([5],"barre_re.png", [650,600])
rec_pseudo = Im([5],"barre_re.png", [650,750])

#connexion
rec_mdp_connexion = Im([5],"barre_re.png", [650,400])
rec_pseudo_connexion = Im([5],"barre_re.png", [650,550])

# création des rectangles qui permettent la conception graphique
rect_bar_affiche = Rectangle(1920,160,(33,33,33),[0],(0,0),"bas")
rect_propo_film = Rectangle(1920,1000,(33,33,33),[0],(0,350),"tot",50,150)
rec_recherche_film = Rectangle(1920, 1080, (33,33,33),[0],[0,200],"tot",50,10)
rec_senregistrer = Rectangle(1920,850,(33,33,33),[1],[0,200],"tot",50,600)
rec_connexion = Rectangle(1920,650,(33,33,33),[1],[0,300],"tot",50,600)

liste_objet = [

    fond_princ, #0
    logo_compte, #1
    rect_bar_affiche, #2
    logo_recher, #3
    logo_overlo, #4
    im_menu, #5
    rect_propo_film, #6
    barre_recher, #7
    txt_recher, #8
    rec_recherche_film, #9
    bouton_pg, #10
    bouton_pd, #11
    cont_senregistrer, #12
    cont_connexion, #13
    rec_senregistrer, #14
    rec_nom, #15
    rec_prenom, #16
    rec_mdp, #17
    rec_pseudo, #18
    txt_nom, #19
    txt_prenom, #20
    txt_mdp, #21
    txt_pseudo, #22
    nom_senregistrer, #23
    prenom_senregistrer, #24
    mdp_senregistrer, #25
    pseudo_senregistrer, #26
    bouton_senregistrer, #27
    rec_connexion, #28
    txt_mdp_connexion, #29
    txt_pseudo_connexion, #30
    mdp_connexion, #31
    pseudo_connexion, #32
    rec_pseudo_connexion, #33
    rec_mdp_connexion, #34
    bouton_connexion, #35
    txt_identifiant_deja_u, #36
    menu_connnexion, #37
    cont_deconnexion, #38
    menu_bouton_film_vu, #39
    menu_bouton_film_voir, #40
    txt_mdp_incorect, #41
    txt_pseudo_incorect, #42
]

liste_objet_bordure = [
    [rect_bar_affiche,rect_propo_film], #1
    [rect_bar_affiche], #1.1
    [rec_recherche_film], #2
    [rect_bar_affiche], #3
    [rect_bar_affiche], #4
    [rect_bar_affiche,rec_senregistrer], #5
    [rect_bar_affiche,rec_connexion], #6
    [rect_bar_affiche,rec_recherche_film], #7
    [rect_bar_affiche], #7.1
]

liste_objet_led = [
    [rect_bar_affiche,rect_propo_film], #1
    [rect_bar_affiche], #1.1
    [rec_recherche_film], #2
    [rect_bar_affiche], #3
    [rect_bar_affiche], #4
    [rect_bar_affiche,rec_senregistrer], #5
    [rect_bar_affiche,rec_connexion], #6
    [rect_bar_affiche,rec_recherche_film], #7
    [rect_bar_affiche], #7.1
]

page = [0,8]

scene_0 = [ 0, 2, 1, 3, 4, 5, 6] #scene principale #0
scene_1 = [2, 1, 7, 3, 4, 5, 8] #scene de recherche #1
scene_1_bis = [0, 9] #1.1
scene_page_film = [0, 2, 1, 3, 4, 5] #scene affichage des films #2
scene_depliant_compte = [12 ,13 , 1] #scene du dépliant du compte en haut à droite #3
scene_senregistrer = [0, 2, 1, 4, 5, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27] #page d'enregistrement utilisateur #4
scene_connexion = [0, 2, 1, 4, 5, 28, 29, 30, 33, 34, 31, 32, 35] #page de connaxion utilisateur #5
scene_depliant_menu = [37,5] #scene du dépliant du menu en haut à gauche #6
scene_film_vu = [2, 1, 4, 5, 8] # scene d'affichage des films vu en fonction du compte #7
scene_film_vu_bis = [0,9] # 7.1


connexion = False
scene = [
    True, #0
    False, #1
    False, #2
    False, #3
    False, #4
    False, #5
    False, #6
    False, #7
]

txt_reini = [23, 24, 25, 26, 31, 32]

case_register = [True,False,False,False]
case_connexion = [False,True]

liste_affichage = affichage_images_rech(txt_recher, division_e, page, scene_1_bis)

liste_page_princiaple_tot = page_principale(division_e, [0,1])
liste_page_princiaple = liste_page_princiaple_tot[0]

liste_pages = []
pseudo = pseudo_connexion.txt
liste_film_vu = affichage_films_vu(pseudo,division_e,page,scene_film_vu_bis)

#boucle principal
continuer = True
while  continuer:
    co_souris = pygame.mouse.get_pos()
    if scene[0]:

        for k in range(len(scene_0)):
            liste_objet[scene_0[k]].affichage(ecran,division_e)

        for k in range(len(liste_objet_bordure[0])):
            liste_objet_bordure[0][k].bordure_rect(ecran,division_e)

        for k in range(len(liste_objet_led[0])):
            liste_objet_led[0][k].led(ecran,division_e)

        if logo_recher.bouton(co_souris, division_e):
            if not 7 in scene_0:
                scene_0.insert(3,7)
        else :
            if  scene_0[3] == 7 and scene[0]:
                scene_0.pop(3)

        for k in liste_page_princiaple:
            k.affichage(ecran, division_e)

    if scene[1]:
        for k in range(len(scene_1_bis)):
            liste_objet[scene_1_bis[k]].affichage(ecran,division_e)

        for k in range(len(liste_objet_bordure[2])):
            liste_objet_bordure[2][k].bordure_rect(ecran,division_e)

        for k in range(len(liste_objet_led[2])):
            liste_objet_led[2][k].led(ecran,division_e)

        for i in range(len(liste_affichage[0])):
            liste_affichage[0][i].affichage(ecran, division_e)

        for k in range(len(scene_1)):
            liste_objet[scene_1[k]].affichage(ecran,division_e)

        for k in range(len(liste_objet_bordure[1])):
            liste_objet_bordure[1][k].bordure_rect(ecran,division_e)

        for k in range(len(liste_objet_led[1])):
            liste_objet_led[1][k].led(ecran,division_e)

    if scene[2]:
        for k in range(len(scene_page_film)):
            liste_objet[scene_page_film[k]].affichage(ecran,division_e)

        for k in range(len(liste_pages)):
            liste_pages[k].affichage(ecran, division_e)

        for k in range(len(liste_objet_bordure[3])):
            liste_objet_bordure[3][k].bordure_rect(ecran,division_e)

        for k in range(len(liste_objet_led[3])):
            liste_objet_led[3][k].led(ecran,division_e)

        for k in range(len(rectangle_page_film)):
            rectangle_page_film[k].led(ecran, division_e)
            rectangle_page_film[k].bordure_rect(ecran, division_e)

        if logo_recher.bouton(co_souris, division_e):
            if not 7 in scene_page_film:
                scene_page_film.insert(3,7)
        else :
            if  scene_page_film[3] == 7 and scene[2]:
                scene_page_film.pop(3)

    if scene[3]:
        if connexion == False:
            scene_depliant_compte = [12 ,13 , 1]
        else :
            scene_depliant_compte = [38 , 1]

        for k in range(len(liste_objet_bordure[4])):
            liste_objet_bordure[4][k].bordure_rect(ecran,division_e)

        for k in range(len(liste_objet_led[4])):
            liste_objet_led[4][k].led(ecran,division_e)

        for k in range(len(scene_depliant_compte)):
            liste_objet[scene_depliant_compte[k]].affichage(ecran,division_e)

    if scene[4]:
        for k in range(len(scene_senregistrer)):
            liste_objet[scene_senregistrer[k]].affichage(ecran,division_e)

        for k in range(len(liste_objet_bordure[5])):
            liste_objet_bordure[5][k].bordure_rect(ecran,division_e)

        for k in range(len(liste_objet_led[5])):
            liste_objet_led[5][k].led(ecran,division_e)

    if scene[5]:
        for k in range(len(scene_connexion)):
            liste_objet[scene_connexion[k]].affichage(ecran,division_e)

        for k in range(len(liste_objet_bordure[6])):
            liste_objet_bordure[6][k].bordure_rect(ecran,division_e)

        for k in range(len(liste_objet_led[6])):
            liste_objet_led[6][k].led(ecran,division_e)

    if scene[6]:
        if connexion == False:
            scene_depliant_menu = [37,5]
        else :
            scene_depliant_menu = [39,40,5]

        for k in range(len(scene_depliant_menu)):
            liste_objet[scene_depliant_menu[k]].affichage(ecran,division_e)


    if scene[7]:
        

        for k in range(len(scene_film_vu_bis)):
            liste_objet[scene_film_vu_bis[k]].affichage(ecran,division_e)

        for k in range(len(liste_objet_bordure[7])):
            liste_objet_bordure[7][k].bordure_rect(ecran,division_e)

        for k in range(len(liste_objet_led[7])):
            liste_objet_led[7][k].led(ecran,division_e)
        
        for i in range(len(liste_film_vu[0])):
            liste_film_vu[0][i].affichage(ecran, division_e)

        for k in range(len(scene_film_vu)):
            liste_objet[scene_film_vu[k]].affichage(ecran,division_e)

        for k in range(len(liste_objet_bordure[1])):
            liste_objet_bordure[1][k].bordure_rect(ecran,division_e)

        for k in range(len(liste_objet_led[1])):
            liste_objet_led[1][k].led(ecran,division_e)


    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if scene[1]:
                if event.key == pygame.K_RETURN:
                    txt_recher.res()
                    liste_affichage = []
                    liste_affichage = affichage_images_rech(txt_recher, division_e, page, scene_1_bis)
                elif event.key == pygame.K_BACKSPACE:
                    txt_recher.suprimer()
                    rec_recherche_film.reini_co()
                    bouton_pd.reini_co()
                    bouton_pg.reini_co()
                    page = [0, 8]
                    liste_affichage = affichage_images_rech(txt_recher, division_e, page, scene_1_bis)

                elif txt_recher.surface.get_width() < 500 // division_e:
                    txt_recher.ajouter(event.unicode)
                    liste_affichage = affichage_images_rech(txt_recher, division_e, page, scene_1_bis)

            if event.key == pygame.K_ESCAPE :
                if scene[2]:
                    for k in range(len(scene)):
                        if scene[k] and scene[scene_suspend] != True:

                            scene[k],scene[scene_suspend] = False,True
                            rec_recherche_film.reini_co()
                            bouton_pd.reini_co()
                            bouton_pg.reini_co()

                            liste_affichage = affichage_images_rech(txt_recher, division_e, page, scene_1_bis)
                            liste_page_princiaple_tot = page_principale(division_e, [0,1])
                            liste_page_princiaple = liste_page_princiaple_tot[0]
                            for z in range(len(txt_reini)):
                                liste_objet[txt_reini[z]].res()
                            if 36 in scene_senregistrer:
                                scene_senregistrer.pop(-1)

                elif scene[1]:
                    for k in range(len(scene)):
                        if scene[k] and scene[0] != True:
                            scene[k],scene[0] = False,True

                            txt_recher.res()
                            liste_affichage = []
                            liste_affichage = affichage_images_rech(txt_recher, division_e, page, scene_1_bis)
                            rec_recherche_film.reini_co()
                            bouton_pd.reini_co()
                            bouton_pg.reini_co()
                            liste_page_princiaple_tot = page_principale(division_e, [0,1])
                            liste_page_princiaple = liste_page_princiaple_tot[0]
                            for z in range(len(txt_reini)):
                                liste_objet[txt_reini[z]].res()
                            if 36 in scene_senregistrer:
                                scene_senregistrer.pop(-1)

                else :
                    for k in range(len(scene)):
                        if scene[k] and scene[0] != True:
                            scene[k],scene[0] = False,True

                            txt_recher.res()
                            liste_affichage = []
                            liste_affichage = affichage_images_rech(txt_recher, division_e, page, scene_1_bis)
                            rec_recherche_film.reini_co()
                            bouton_pd.reini_co()
                            bouton_pg.reini_co()
                            liste_page_princiaple_tot = page_principale(division_e, [0,1])
                            liste_page_princiaple = liste_page_princiaple_tot[0]
                            for z in range(len(txt_reini)):
                                liste_objet[txt_reini[z]].res()
                            if 36 in scene_senregistrer:
                                scene_senregistrer.pop(-1)

            if scene[4]:
                for k in range(len(case_register)):
                    if case_register[k]:
                        if event.key == pygame.K_BACKSPACE:
                            liste_objet[k + 23].suprimer()

                        elif event.key == pygame.K_TAB:
                            if len(case_register) -1 == k :
                                case_register[0],case_register[k] = True,False
                                break
                            else :

                                case_register[k],case_register[k+1] = False,True
                                break

                        elif liste_objet[k + 23].surface.get_width() < 500 // division_e:
                            liste_objet[k + 23].ajouter(event.unicode)

            if scene[5]:
                for k in range(len(case_connexion)):
                    if case_connexion[k]:
                        if event.key == pygame.K_BACKSPACE:
                            liste_objet[k + 31].suprimer()

                        elif event.key == pygame.K_TAB:
                            if len(case_connexion) -1 == k :
                                case_connexion[0],case_connexion[k] = True,False
                                break
                            else :

                                case_connexion[k],case_connexion[k+1] = False,True
                                break

                        elif liste_objet[k + 31].surface.get_width() < 500 // division_e:

                            liste_objet[k + 31].ajouter(event.unicode)

        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):

            if logo_compte.bouton(co_souris, division_e) and scene[6] != True:
                for z in range(len(txt_reini)):
                    liste_objet[txt_reini[z]].res()
                if 36 in scene_senregistrer:
                    scene_senregistrer.pop(-1)
                for k in range(len(scene)):

                    if scene[k] and scene[3] != True:
                        scene[k],scene[3] = False,True
                        scene_suspend = k

            elif im_menu.bouton(co_souris, division_e) and scene[3] != True:
                for k in range(len(scene)):
                    if scene[k] and scene[6] != True:
                        scene[k],scene[6] = False,True
                        scene_suspend = k

            elif scene[6] and ((not menu_connnexion.bouton(co_souris,division_e) and not connexion) or (not menu_bouton_film_vu.bouton(co_souris,division_e) and not menu_bouton_film_voir.bouton(co_souris, division_e) and connexion)):
                scene[scene_suspend],scene[6] = True, False

            elif scene[3] and ((not cont_senregistrer.bouton(co_souris, division_e) and not cont_connexion.bouton(co_souris , division_e) and not connexion) or (not cont_deconnexion.bouton(co_souris,division_e) and connexion)):
                scene[scene_suspend],scene[3] = True,False

            elif scene[3] and cont_deconnexion.bouton(co_souris, division_e) and connexion:
                connexion = False
                for k in range(len(scene)):
                    if scene[k] and k != 0:
                        scene[k], scene[0] = False,True

            elif scene[3] and cont_senregistrer.bouton(co_souris,division_e) and not connexion:
                scene[3],scene[4] = False, True


            elif (scene[3] or scene[6]) and (cont_connexion.bouton(co_souris, division_e) or menu_connnexion.bouton(co_souris, division_e)) and not connexion:
                scene[3],scene[6],scene[5] = False, False , True

            elif scene[0]:
                


                for k in range(len(liste_page_princiaple_tot[2])):
                    if liste_page_princiaple_tot[2][k].bouton(co_souris, division_e, 2):
                        fonction_pages = page_films(liste_page_princiaple_tot, k, division_e)
                        liste_pages = fonction_pages[0]
                        rectangle_page_film = fonction_pages[1]
                        scene[0], scene[2] = False, True
                        scene_suspend = 0

            elif scene[1] and bouton_pg.bouton(co_souris,division_e):
                page[0] -= 8
                page[1] -= 8
                liste_affichage = affichage_images_rech(txt_recher, division_e, page, scene_1_bis)
                rec_recherche_film.reini_co()
                bouton_pd.reini_co()
                bouton_pg.reini_co()

            elif scene[1] and bouton_pd.bouton(co_souris,division_e):
                page[0] += 8
                page[1] += 8
                liste_affichage = affichage_images_rech(txt_recher, division_e, page, scene_1_bis)
                rec_recherche_film.reini_co()
                bouton_pd.reini_co()
                bouton_pg.reini_co()

            elif scene[1]:
                for k in range(len(liste_affichage[2])):
                    if liste_affichage[2][k].bouton(co_souris, division_e, 2):
                        fonction_pages = page_films(liste_affichage, k, division_e)
                        liste_pages = fonction_pages[0]
                        rectangle_page_film = fonction_pages[1]
                        scene[1], scene[2] = False, True
                        scene_suspend = 1

            if scene[0] or scene[2] :
                if logo_recher.bouton(co_souris, division_e):

                    for k in range(len(scene)):

                        if scene[k] and scene[1] != True:
                            scene[k],scene[1] = False,True

                            txt_recher.res()
                            liste_affichage = []
                            liste_affichage = affichage_images_rech(txt_recher, division_e, page, scene_1_bis)
                            rec_recherche_film.reini_co()
                            bouton_pd.reini_co()
                            bouton_pg.reini_co()
                            page = [0, 8]

            elif scene[4]:
                for k in range(4):
                    if liste_objet[k + 15].bouton(co_souris,division_e):
                        for i in range(len(case_register)):
                            if case_register[i] and case_register[k] != True:
                                case_register[i],case_register[k] = False,True

                if bouton_senregistrer.bouton(co_souris, division_e) and (nom_senregistrer.txt != "" and prenom_senregistrer.txt != "" and mdp_senregistrer.txt != "" and pseudo_senregistrer.txt != "") :
                    for i in range(4):
                        if liste_objet[k + 23].txt == "":
                            break

                    if Register(nom_senregistrer.txt,prenom_senregistrer.txt,mdp_senregistrer.txt,pseudo_senregistrer.txt):
                        scene[4],scene[5] = False,True
                        for z in range(len(txt_reini)):
                            liste_objet[txt_reini[z]].res()
                        if 36 in scene_senregistrer:
                            scene_senregistrer.pop(-1)
                    else :
                        scene_senregistrer.insert(len(scene_senregistrer),36)

            elif scene[5]:
                for k in range(2):

                    if liste_objet[k + 33].bouton(co_souris,division_e):


                        for i in range(len(case_connexion)):
                            if case_connexion[i] and case_connexion[k] != True:
                                case_connexion[i],case_connexion[k] = False,True

                if bouton_connexion.bouton(co_souris,division_e) and (pseudo_connexion.txt != "" and mdp_connexion.txt != ""):
                    if Login(pseudo_connexion.txt, mdp_connexion.txt) == "1":
                        connexion = True
                        pseudo = pseudo_connexion.txt
                        StatutFilm(pseudo,24)
                        liste_film_vu = affichage_films_vu(pseudo,division_e,page,scene_film_vu_bis)
                        scene[5],scene[0] = False,True
                        
                        for z in range(len(txt_reini)):
                            liste_objet[txt_reini[z]].res()
                        if 41 and 42 in scene_connexion:
                            scene_connexion.pop(-1)
                            scene_connexion.pop(-2)
                        elif 41 in scene_connexion and 42 not in scene_connexion:
                            scene_connexion.pop(-1)
                        elif 42 in scene_connexion and 41 not in scene_connexion:
                            scene_connexion.pop(-1)
                        


                    elif Login(pseudo_connexion.txt, mdp_connexion.txt) == "0":
                        scene_connexion.insert(len(scene_connexion),42)

                    elif Login(pseudo_connexion.txt, mdp_connexion.txt) == "2":
                        scene_connexion.insert(len(scene_connexion),41)
            
            elif scene[6]:
                
                if menu_bouton_film_vu.bouton(co_souris, division_e):

                    for k in range(len(scene)):
                        if scene[k] and k != 7:
                            scene[k], scene[7] = False, True

        if event.type == pygame.MOUSEWHEEL:
                if scene[1] :
                    if event.y > 0 and liste_objet[9].y < 200:
                        for k in range(len(liste_affichage[0])):
                            liste_affichage[0][k].y += 100
                        for k in range(1,len(scene_1_bis)):
                            liste_objet[scene_1_bis[k]].y += 100


                    if event.y < 0 and liste_objet[9].y > -100:
                        for k in range(len(liste_affichage[0])):
                            liste_affichage[0][k].y -= 100

                        for k in range(1, len(scene_1_bis)):
                            liste_objet[scene_1_bis[k]].y -= 100
