import pygame
from time import sleep
from random import randint
from math import *

#initialisation
pygame.init()
pygame.mixer.init()

#fps
clock = pygame.time.Clock()
clock.tick(2)

#configuration de la fenetre
pygame.display.set_caption("Compteur de points UNO")
dimension_fenetre = (1263, 720)
screen = pygame.display.set_mode(dimension_fenetre)

#importation de l'icone de la fenetre
icone_uno = pygame.image.load('Images//icone_uno.png')
pygame.display.set_icon(icone_uno) 

#on rend le curseur invisible
pygame.mouse.set_visible(False)

################################################################################


#corp du programme


################################################################################
#mise en place de l'ecran de chargement
verification = False

for repetion_chargement in range(1):

    #deplacement de la souris aux coordonnees donnees
    pygame.mouse.set_pos(0,0)
    chargement = "chargement"
    if verification == False:


        #ici on affecte toutes les variables et les images pour pouvoir
        #faire un chargement

        #mise en place de la police d'ecriture
        police36=pygame.font.Font('police//police_n_1.ttf',36)
        police50=pygame.font.Font('police//police_n_1.ttf',50)


        #importation des images
        table_daffichage_cartes = pygame.image.load('Images//table_daffichage_cartes.png')
        fond_de_chargement = pygame.image.load('Images//fond_chargement.jpg')
        fond_principal = pygame.image.load('Images//fond_principal.png')
        baniere_commencer_uno = pygame.image.load('Images//baniere_commencer_Uno.png')
        table_daffichage_tour_joueur = pygame.image.load('Images//table_daffichage_cartes.png')
        baniere_passez_joueur_suivant = pygame.image.load('Images//passage_joueur_suivant.png')
        table_score = pygame.image.load('Images//table_daffichage_cartes.png')
        table_daffichage_score_final = pygame.image.load('Images//table_daffichage_cartes_finale.png')

        #images des joueurs
        joueur_2 = pygame.image.load('Images//joueurs//2_joueurs.jpg')
        joueur_3 = pygame.image.load('Images//joueurs//3_joueurs.jpg')
        joueur_4 = pygame.image.load('Images//joueurs//4_joueurs.jpg')
        joueur_5 = pygame.image.load('Images//joueurs//5_joueurs.jpg')
        joueur_6 = pygame.image.load('Images//joueurs//6_joueurs.jpg')
        joueur_7 = pygame.image.load('Images//joueurs//7_joueurs.jpg')
        joueur_8 = pygame.image.load('Images//joueurs//8_joueurs.jpg')
        joueur_9 = pygame.image.load('Images//joueurs//9_joueurs.jpg')
        joueur_10 = pygame.image.load('Images//joueurs//10_joueurs.jpg')




        #Variables cartes
        #cartes a chiffres de 0 a 9
        carte_0=pygame.image.load("Images//cartes//carte_0.jpg")
        carte_1=pygame.image.load("Images//cartes//carte_1.jpg")
        carte_2=pygame.image.load("Images//cartes//carte_2.jpg")
        carte_3=pygame.image.load("Images//cartes//carte_3.jpg")
        carte_4=pygame.image.load("Images//cartes//carte_4.jpg")
        carte_5=pygame.image.load("Images//cartes//carte_5.jpg")
        carte_6=pygame.image.load("Images//cartes//carte_6.jpg")
        carte_7=pygame.image.load("Images//cartes//carte_7.jpg")
        carte_8=pygame.image.load("Images//cartes//carte_8.jpg")
        carte_9=pygame.image.load("Images//cartes//carte_9.jpg")
        #cartes speciales
        carte_plus2=pygame.image.load("Images//cartes//carte_+2.jpg")
        carte_plus4=pygame.image.load("Images//cartes//carte_+4.jpg")
        carte_c_c=pygame.image.load("Images//cartes//carte_c_c.jpg")
        carte_c_s=pygame.image.load("Images//cartes//carte_c_s.jpg")
        carte_s_i=pygame.image.load("Images//cartes//carte_s_i.jpg")


        #Images scores
        score_0 = pygame.image.load('Images//ajout_score//+0.png')
        score_1 = pygame.image.load('Images//ajout_score//+1.png')
        score_2 = pygame.image.load('Images//ajout_score//+2.png')
        score_3 = pygame.image.load('Images//ajout_score//+3.png')
        score_4 = pygame.image.load('Images//ajout_score//+4.png')
        score_5 = pygame.image.load('Images//ajout_score//+5.png')
        score_6 = pygame.image.load('Images//ajout_score//+6.png')
        score_7 = pygame.image.load('Images//ajout_score//+7.png')
        score_8 = pygame.image.load('Images//ajout_score//+8.png')
        score_9 = pygame.image.load('Images//ajout_score//+9.png')
        score_20 = pygame.image.load('Images//ajout_score//+20.png')
        score_50 = pygame.image.load('Images//ajout_score//+50.png')

        #redimension des images scores
        dimension_score = (200,200)

        score_0 = pygame.transform.scale(score_0,dimension_score)
        score_1 = pygame.transform.scale(score_1,dimension_score)
        score_2 = pygame.transform.scale(score_2,dimension_score)
        score_3 = pygame.transform.scale(score_3,dimension_score)
        score_4 = pygame.transform.scale(score_4,dimension_score)
        score_5 = pygame.transform.scale(score_5,dimension_score)
        score_6 = pygame.transform.scale(score_6,dimension_score)
        score_7 = pygame.transform.scale(score_7,dimension_score)
        score_8 = pygame.transform.scale(score_8,dimension_score)
        score_9 = pygame.transform.scale(score_9,dimension_score)
        score_20 = pygame.transform.scale(score_20,dimension_score)
        score_50 = pygame.transform.scale(score_50,dimension_score)

        score_en_activite = score_0

        #redimension des images principales
        fond_de_chargement = pygame.transform.scale(fond_de_chargement, (1263, 720))
        fond_principal = pygame.transform.scale(fond_principal, (1263,720))
        baniere_commencer_uno = pygame.transform.scale(baniere_commencer_uno, dimension_fenetre)
        table_daffichage_cartes = pygame.transform.scale(table_daffichage_cartes, (750,650))
        table_daffichage_tour_joueur = pygame.transform.scale(table_daffichage_tour_joueur,(500, 800))
        baniere_passez_joueur_suivant = pygame.transform.scale(baniere_passez_joueur_suivant,(333,83))
        table_score = pygame.transform.scale(table_score,(750,200))
        table_daffichage_score_final = pygame.transform.scale(table_daffichage_score_final,(dimension_fenetre[0],dimension_fenetre[1]+100))



        #creation des variables principales
        running = 1
        cliquer_commencer = "cliquer pour commencer"
        texte_nbr_joueurs = "De combien de joueurs voulez-vous compter les points au Uno?"
        voix = True
        volume = 1
        question_nbr_joueurs = pygame.mixer.Sound('sons//question_joueurs.mp3')
            #le tour du joueur est 1 car on commence par compter les points du joueur 1
        tour_joueur = 1
        son_tour_joueur = True

            #pour le clique gauche
        LEFT = 1
        temp_affichage_score = 0
        temp_cliquer_commencer = 0






        #coordonnees
        coordonnee_table_daffichage_tour_joueur = (750,-60)
        coordonnee_baniere_passage = (850,500)


        #variables joueurs
        str_joueur_1 = "Joueur 1"
        str_joueur_2 = "Joueur 2"
        str_joueur_3 = "Joueur 3"
        str_joueur_4 = "Joueur 4"
        str_joueur_5 = "Joueur 5"
        str_joueur_6 = "Joueur 6"
        str_joueur_7 = "Joueur 7"
        str_joueur_8 = "Joueur 8"
        str_joueur_9 = "Joueur 9"
        str_joueur_10 = "Joueur 10"

        str_joueur_1_score = "score du joueur 1 :"
        str_joueur_2_score = "score du joueur 2 :"
        str_joueur_3_score = "score du joueur 3 :"
        str_joueur_4_score = "score du joueur 4 :"
        str_joueur_5_score = "score du joueur 5 :"
        str_joueur_6_score = "score du joueur 6 :"
        str_joueur_7_score = "score du joueur 7 :"
        str_joueur_8_score = "score du joueur 8 :"
        str_joueur_9_score = "score du joueur 9 :"
        str_joueur_10_score = "score du joueur 10 :"





        #creation des coordonnees des cartes
        position_carte_0=(100,75)
        position_carte_1=(200,75)
        position_carte_2=(300,75)
        position_carte_3=(400,75)
        position_carte_4=(500,75)
        position_carte_5=(100,225)
        position_carte_6=(200,225)
        position_carte_7=(300,225)
        position_carte_8=(400,225)
        position_carte_9=(500,225)
        position_carte_plus2=(100,375)
        position_carte_plus4=(200,375)
        position_carte_c_c=(300,375)
        position_carte_c_s=(400,375)
        position_carte_s_i=(500,375)

        #creation des coordonnees des images joueurs
        position_joueur2 = (dimension_fenetre[0]//10,dimension_fenetre[1]//8)
        position_joueur3 = (dimension_fenetre[0]//10+297,dimension_fenetre[1]//8)
        position_joueur4 = (dimension_fenetre[0]//10+(297*2),dimension_fenetre[1]//8)
        position_joueur5 = (dimension_fenetre[0]//10+(297*3),dimension_fenetre[1]//8)
        position_joueur6 = (dimension_fenetre[0]//10-75,dimension_fenetre[1]//8+274)
        position_joueur7 = (dimension_fenetre[0]//10+237-15,dimension_fenetre[1]//8+274)
        position_joueur8 = (dimension_fenetre[0]//10+(237*2)-15,dimension_fenetre[1]//8+274)
        position_joueur9 = (dimension_fenetre[0]//10+(237*3)-15,dimension_fenetre[1]//8+274)
        position_joueur10 = (dimension_fenetre[0]//10+(237*4),dimension_fenetre[1]//8+274)


        #creation des textes
        texte_chargement = police36.render(chargement, False,(0,0,0))
        texte_commencement = police50.render(cliquer_commencer,False,(255,255,255))
        texte_joueurs = police36.render(texte_nbr_joueurs,False,(255,255,255))



        #textes dans le cadre des scores et police d'affichage
        couleur_blanche = (255,255,255)
        texte_tour_joueur = police36.render(str_joueur_1, False,couleur_blanche)
        texte_score_joueur = police36.render(str_joueur_1_score, False,couleur_blanche)
        texte_joueur_2 = police36.render(str_joueur_2, False,couleur_blanche)
        texte_joueur_3 = police36.render(str_joueur_3, False,couleur_blanche)
        texte_joueur_4 = police36.render(str_joueur_4, False,couleur_blanche)
        texte_joueur_5 = police36.render(str_joueur_5, False,couleur_blanche)
        texte_joueur_6 = police36.render(str_joueur_6, False,couleur_blanche)
        texte_joueur_7 = police36.render(str_joueur_7, False,couleur_blanche)
        texte_joueur_8 = police36.render(str_joueur_8, False,couleur_blanche)
        texte_joueur_9 = police36.render(str_joueur_9, False,couleur_blanche)
        texte_joueur_10 = police36.render(str_joueur_10, False,couleur_blanche)




        #creation des sons
        #creation du boutton son actif//inactif
        bouton_son_actif_inactif = pygame.image.load('Images//bouton_son_actif.png').convert_alpha()
        bouton_son_actif_inactif = pygame.transform.scale(bouton_son_actif_inactif,(50,50))
        coordonnee_boutton_son = (1203, 660)
        son = True


        #son du choix du nombre de joueurs
        joueur_2_son = pygame.mixer.Sound(r'sons//joueurs//2_joueurs.wav')
        joueur_3_son = pygame.mixer.Sound(r'sons//joueurs//3_joueurs.wav')
        joueur_4_son = pygame.mixer.Sound(r'sons//joueurs//4_joueurs.wav')
        joueur_5_son = pygame.mixer.Sound(r'sons//joueurs//5_joueurs.wav')
        joueur_6_son = pygame.mixer.Sound(r'sons//joueurs//6_joueurs.wav')
        joueur_7_son = pygame.mixer.Sound(r'sons//joueurs//7_joueurs.wav')
        joueur_8_son = pygame.mixer.Sound(r'sons//joueurs//8_joueurs.wav')
        joueur_9_son = pygame.mixer.Sound(r'sons//joueurs//9_joueurs.wav')
        joueur_10_son = pygame.mixer.Sound(r'sons//joueurs//10_joueurs.wav')


        #son passage au joueur suivant
        son_passage_j_1 = pygame.mixer.Sound(r'sons//tour_joueur//joueur_1.wav')
        son_passage_j_2 = pygame.mixer.Sound(r'sons//tour_joueur//joueur_2.wav')
        son_passage_j_3 = pygame.mixer.Sound(r'sons//tour_joueur//joueur_3.wav')
        son_passage_j_4 = pygame.mixer.Sound(r'sons//tour_joueur//joueur_4.wav')
        son_passage_j_5 = pygame.mixer.Sound(r'sons//tour_joueur//joueur_5.wav')
        son_passage_j_6 = pygame.mixer.Sound(r'sons//tour_joueur//joueur_6.wav')
        son_passage_j_7 = pygame.mixer.Sound(r'sons//tour_joueur//joueur_7.wav')
        son_passage_j_8 = pygame.mixer.Sound(r'sons//tour_joueur//joueur_8.wav')
        son_passage_j_9 = pygame.mixer.Sound(r'sons//tour_joueur//joueur_9.wav')
        son_passage_j_10 = pygame.mixer.Sound(r'sons//tour_joueur//joueur_10.wav')

        #score des joueurs
        score_joueur_1 = 0
        score_joueur_2 = 0
        score_joueur_3 = 0
        score_joueur_4 = 0
        score_joueur_5 = 0
        score_joueur_6 = 0
        score_joueur_7 = 0
        score_joueur_8 = 0
        score_joueur_9 = 0
        score_joueur_10 = 0

        score_joueur_tour = 0
        score_affichage = score_joueur_1
        texte_score = police50.render(str(score_affichage),False,(255,255,255))








        verification = True
    for chargement_boucle in range(4):

        screen.blit(fond_de_chargement, (0, 0))
        texte_chargement = police36.render(chargement, False,(0,0,0),)
        screen.blit(texte_chargement,(950, 650))
        pygame.display.update()
        #sleep permet de mettre en pause le programme pendant
        #un nombre de secondes definis
        sleep(0.5)
        chargement += "."

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
                pygame.quit()



#on rend le curseur visible
pygame.mouse.set_visible(True)
marche = True
while marche:
    #creation de la boucle d'acceuil
    while running == 1 :
            #affichage et creation de l'ecran d'accueil
            screen.blit(fond_principal,(0, 0))
            screen.blit(baniere_commencer_uno, (20,-20))
            #boutton son
            screen.blit(bouton_son_actif_inactif,coordonnee_boutton_son)

            if temp_affichage_score <= 30:
                cliquer_commencer = ""
                texte_commencement = police50.render(cliquer_commencer,False,(255,255,0))
                screen.blit(texte_commencement,(dimension_fenetre[0]//3-40,550))

                temp_affichage_score += 1

            elif temp_affichage_score >= 20:
                if temp_affichage_score >= 100:
                    temp_affichage_score = 0
                cliquer_commencer = "cliquer pour commencer"
                texte_commencement = police50.render(cliquer_commencer,False,(255,255,255))
                screen.blit(texte_commencement,(dimension_fenetre[0]//3-40,550))
                temp_affichage_score +=1





            coordonnee_souris = pygame.mouse.get_pos()
            pygame.display.update()
            for event in pygame.event.get():



                if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()


                #mise en place du boutton son
                if coordonnee_souris[0] > coordonnee_boutton_son[0] and coordonnee_souris[1] > coordonnee_boutton_son[1] \
                and coordonnee_souris[0] < coordonnee_boutton_son[0]+50 and coordonnee_souris[1] < coordonnee_boutton_son[1]+50\
                and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                    if son == True :
                        bouton_son_actif_inactif = pygame.image.load('Images//bouton_son_inactif.png')
                        bouton_son_actif_inactif = pygame.transform.scale(bouton_son_actif_inactif,(50,50))
                        son = False
                        volume = 0.0
                    elif son == False :
                        bouton_son_actif_inactif = pygame.image.load('Images//bouton_son_actif.png')
                        bouton_son_actif_inactif = pygame.transform.scale(bouton_son_actif_inactif,(50,50))
                        son = True
                        volume = 1

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                    running = 2
                    #mettre le curseur au coordonnee donnee
                    pygame.mouse.set_pos(coordonnee_boutton_son[0]+25,coordonnee_boutton_son[1]+25)
                    question_nbr_joueurs.set_volume(volume)
                    question_nbr_joueurs.play()






    while running == 2:
        #affichege du fond principal
        screen.blit(fond_principal,(0, 0))

        #affichage du texte
        screen.blit(texte_joueurs,(25,10))

        #boutton son
        screen.blit(bouton_son_actif_inactif,coordonnee_boutton_son)







        coordonnee_souris = pygame.mouse.get_pos()
        if coordonnee_souris[0] > position_joueur2[0] and coordonnee_souris[1] > position_joueur2[1] \
        and coordonnee_souris[0] < position_joueur2[0]+150 and coordonnee_souris[1] < position_joueur2[1]+224:
            joueur_2 = pygame.transform.scale(joueur_2,(160,234))



            screen.blit(joueur_2,(position_joueur2[0]-5,position_joueur2[1]-5))
            screen.blit(joueur_3,position_joueur3)
            screen.blit(joueur_4,position_joueur4)
            screen.blit(joueur_5,position_joueur5)
            screen.blit(joueur_6,position_joueur6)
            screen.blit(joueur_7,position_joueur7)
            screen.blit(joueur_8,position_joueur8)
            screen.blit(joueur_9,position_joueur9)
            screen.blit(joueur_10,position_joueur10)


            if voix == True:
                joueur_2_son.set_volume(volume)
                joueur_2_son.play()
                voix = False


        elif coordonnee_souris[0] > position_joueur3[0] and coordonnee_souris[1] > position_joueur3[1] \
        and coordonnee_souris[0] < position_joueur3[0]+150 and coordonnee_souris[1] < position_joueur3[1]+224:
            joueur_3 = pygame.transform.scale(joueur_3,(160,234))


            screen.blit(joueur_2,position_joueur2)
            screen.blit(joueur_3,(position_joueur3[0]-5,position_joueur3[1]-5))
            screen.blit(joueur_4,position_joueur4)
            screen.blit(joueur_5,position_joueur5)
            screen.blit(joueur_6,position_joueur6)
            screen.blit(joueur_7,position_joueur7)
            screen.blit(joueur_8,position_joueur8)
            screen.blit(joueur_9,position_joueur9)
            screen.blit(joueur_10,position_joueur10)


            if voix == True:
                joueur_3_son.set_volume(volume)
                joueur_3_son.play()
                voix = False

        elif coordonnee_souris[0] > position_joueur4[0] and coordonnee_souris[1] > position_joueur4[1] \
        and coordonnee_souris[0] < position_joueur4[0]+150 and coordonnee_souris[1] < position_joueur4[1]+224:
            joueur_4 = pygame.transform.scale(joueur_4,(160,234))


            screen.blit(joueur_2,position_joueur2)
            screen.blit(joueur_3,position_joueur3)
            screen.blit(joueur_4,(position_joueur4[0]-5,position_joueur4[1]-5))
            screen.blit(joueur_5,position_joueur5)
            screen.blit(joueur_6,position_joueur6)
            screen.blit(joueur_7,position_joueur7)
            screen.blit(joueur_8,position_joueur8)
            screen.blit(joueur_9,position_joueur9)
            screen.blit(joueur_10,position_joueur10)


            if voix == True:
                joueur_4_son.set_volume(volume)
                joueur_4_son.play()
                voix = False

        elif coordonnee_souris[0] > position_joueur5[0] and coordonnee_souris[1] > position_joueur5[1] \
        and coordonnee_souris[0] < position_joueur5[0]+150 and coordonnee_souris[1] < position_joueur5[1]+224:
            joueur_5 = pygame.transform.scale(joueur_5,(160,234))


            screen.blit(joueur_2,position_joueur2)
            screen.blit(joueur_3,position_joueur3)
            screen.blit(joueur_4,position_joueur4)
            screen.blit(joueur_5,(position_joueur5[0]-5,position_joueur5[1]-5))
            screen.blit(joueur_6,position_joueur6)
            screen.blit(joueur_7,position_joueur7)
            screen.blit(joueur_8,position_joueur8)
            screen.blit(joueur_9,position_joueur9)
            screen.blit(joueur_10,position_joueur10)


            if voix == True:
                joueur_5_son.set_volume(volume)
                joueur_5_son.play()
                voix = False

        elif coordonnee_souris[0] > position_joueur6[0] and coordonnee_souris[1] > position_joueur6[1] \
        and coordonnee_souris[0] < position_joueur6[0]+150 and coordonnee_souris[1] < position_joueur6[1]+224:
            joueur_6 = pygame.transform.scale(joueur_6,(160,234))


            screen.blit(joueur_2,position_joueur2)
            screen.blit(joueur_3,position_joueur3)
            screen.blit(joueur_4,position_joueur4)
            screen.blit(joueur_5,position_joueur5)
            screen.blit(joueur_6,(position_joueur6[0]-5,position_joueur6[1]-5))
            screen.blit(joueur_7,position_joueur7)
            screen.blit(joueur_8,position_joueur8)
            screen.blit(joueur_9,position_joueur9)
            screen.blit(joueur_10,position_joueur10)


            if voix == True:
                joueur_6_son.set_volume(volume)
                joueur_6_son.play()
                voix = False

        elif coordonnee_souris[0] > position_joueur7[0] and coordonnee_souris[1] > position_joueur7[1] \
        and coordonnee_souris[0] < position_joueur7[0]+150 and coordonnee_souris[1] < position_joueur7[1]+224:
            joueur_7 = pygame.transform.scale(joueur_7,(160,234))


            screen.blit(joueur_2,position_joueur2)
            screen.blit(joueur_3,position_joueur3)
            screen.blit(joueur_4,position_joueur4)
            screen.blit(joueur_5,position_joueur5)
            screen.blit(joueur_6,position_joueur6)
            screen.blit(joueur_7,(position_joueur7[0]-5,position_joueur7[1]-5))
            screen.blit(joueur_8,position_joueur8)
            screen.blit(joueur_9,position_joueur9)
            screen.blit(joueur_10,position_joueur10)


            if voix == True:
                joueur_7_son.set_volume(volume)
                joueur_7_son.play()
                voix = False

        elif coordonnee_souris[0] > position_joueur8[0] and coordonnee_souris[1] > position_joueur8[1] \
        and coordonnee_souris[0] < position_joueur8[0]+150 and coordonnee_souris[1] < position_joueur8[1]+224:
            joueur_8 = pygame.transform.scale(joueur_8,(160,234))


            screen.blit(joueur_2,position_joueur2)
            screen.blit(joueur_3,position_joueur3)
            screen.blit(joueur_4,position_joueur4)
            screen.blit(joueur_5,position_joueur5)
            screen.blit(joueur_6,position_joueur6)
            screen.blit(joueur_7,position_joueur7)
            screen.blit(joueur_8,(position_joueur8[0]-5,position_joueur8[1]-5))
            screen.blit(joueur_9,position_joueur9)
            screen.blit(joueur_10,position_joueur10)


            if voix == True:
                joueur_8_son.set_volume(volume)
                joueur_8_son.play()
                voix = False

        elif coordonnee_souris[0] > position_joueur9[0] and coordonnee_souris[1] > position_joueur9[1] \
        and coordonnee_souris[0] < position_joueur9[0]+150 and coordonnee_souris[1] < position_joueur9[1]+224:
            joueur_9 = pygame.transform.scale(joueur_9,(160,234))


            screen.blit(joueur_2,position_joueur2)
            screen.blit(joueur_3,position_joueur3)
            screen.blit(joueur_4,position_joueur4)
            screen.blit(joueur_5,position_joueur5)
            screen.blit(joueur_6,position_joueur6)
            screen.blit(joueur_7,position_joueur7)
            screen.blit(joueur_8,position_joueur8)
            screen.blit(joueur_9,(position_joueur9[0]-5,position_joueur9[1]-5))
            screen.blit(joueur_10,position_joueur10)


            if voix == True:
                joueur_9_son.set_volume(volume)
                joueur_9_son.play()
                voix = False

        elif coordonnee_souris[0] > position_joueur10[0] and coordonnee_souris[1] > position_joueur10[1] \
        and coordonnee_souris[0] < position_joueur10[0]+150 and coordonnee_souris[1] < position_joueur10[1]+224:
            joueur_10 = pygame.transform.scale(joueur_10,(160,234))


            screen.blit(joueur_2,position_joueur2)
            screen.blit(joueur_3,position_joueur3)
            screen.blit(joueur_4,position_joueur4)
            screen.blit(joueur_5,position_joueur5)
            screen.blit(joueur_6,position_joueur6)
            screen.blit(joueur_7,position_joueur7)
            screen.blit(joueur_8,position_joueur8)
            screen.blit(joueur_9,position_joueur9)
            screen.blit(joueur_10,(position_joueur10[0]-5,position_joueur10[1]-5))


            if voix == True:
                joueur_10_son.set_volume(volume)
                joueur_10_son.play()
                voix = False





        else :
            #remise a la taille normal des images des joueurs
            joueur_2 = pygame.image.load('Images//joueurs//2_joueurs.jpg')
            joueur_3 = pygame.image.load('Images//joueurs//3_joueurs.jpg')
            joueur_4 = pygame.image.load('Images//joueurs//4_joueurs.jpg')
            joueur_5 = pygame.image.load('Images//joueurs//5_joueurs.jpg')
            joueur_6 = pygame.image.load('Images//joueurs//6_joueurs.jpg')
            joueur_7 = pygame.image.load('Images//joueurs//7_joueurs.jpg')
            joueur_8 = pygame.image.load('Images//joueurs//8_joueurs.jpg')
            joueur_9 = pygame.image.load('Images//joueurs//9_joueurs.jpg')
            joueur_10 = pygame.image.load('Images//joueurs//10_joueurs.jpg')



            #affichage des images joueurs
            screen.blit(joueur_2,position_joueur2)
            screen.blit(joueur_3,position_joueur3)
            screen.blit(joueur_4,position_joueur4)
            screen.blit(joueur_5,position_joueur5)
            screen.blit(joueur_6,position_joueur6)
            screen.blit(joueur_7,position_joueur7)
            screen.blit(joueur_8,position_joueur8)
            screen.blit(joueur_9,position_joueur9)
            screen.blit(joueur_10,position_joueur10)
            voix = True










        pygame.display.update()
        for event in pygame.event.get():



            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            elif coordonnee_souris[0] > position_joueur2[0] and coordonnee_souris[1] > position_joueur2[1] \
            and coordonnee_souris[0] < position_joueur2[0]+150 and coordonnee_souris[1] < position_joueur2[1]+224 \
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                nbr_joueurs = 2
                running = 3

            elif coordonnee_souris[0] > position_joueur3[0] and coordonnee_souris[1] > position_joueur3[1] \
            and coordonnee_souris[0] < position_joueur3[0]+150 and coordonnee_souris[1] < position_joueur3[1]+224 \
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                nbr_joueurs = 3
                running = 3

            elif coordonnee_souris[0] > position_joueur4[0] and coordonnee_souris[1] > position_joueur4[1] \
            and coordonnee_souris[0] < position_joueur4[0]+150 and coordonnee_souris[1] < position_joueur4[1]+224 \
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                nbr_joueurs = 4
                running = 3

            elif coordonnee_souris[0] > position_joueur5[0] and coordonnee_souris[1] > position_joueur5[1] \
            and coordonnee_souris[0] < position_joueur5[0]+150 and coordonnee_souris[1] < position_joueur5[1]+224 \
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                nbr_joueurs = 5
                running = 3

            elif coordonnee_souris[0] > position_joueur6[0] and coordonnee_souris[1] > position_joueur6[1] \
            and coordonnee_souris[0] < position_joueur6[0]+150 and coordonnee_souris[1] < position_joueur6[1]+224 \
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                nbr_joueurs = 6
                running = 3

            elif coordonnee_souris[0] > position_joueur7[0] and coordonnee_souris[1] > position_joueur7[1] \
            and coordonnee_souris[0] < position_joueur7[0]+150 and coordonnee_souris[1] < position_joueur7[1]+224 \
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                nbr_joueurs = 7
                running = 3

            elif coordonnee_souris[0] > position_joueur8[0] and coordonnee_souris[1] > position_joueur8[1] \
            and coordonnee_souris[0] < position_joueur8[0]+150 and coordonnee_souris[1] < position_joueur8[1]+224 \
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                nbr_joueurs = 8
                running = 3

            elif coordonnee_souris[0] > position_joueur9[0] and coordonnee_souris[1] > position_joueur9[1] \
            and coordonnee_souris[0] < position_joueur9[0]+150 and coordonnee_souris[1] < position_joueur9[1]+224 \
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                nbr_joueurs = 9
                running = 3

            elif coordonnee_souris[0] > position_joueur10[0] and coordonnee_souris[1] > position_joueur10[1] \
            and coordonnee_souris[0] < position_joueur10[0]+150 and coordonnee_souris[1] < position_joueur10[1]+224 \
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                nbr_joueurs = 10
                running = 3

            #mise en place du boutton son
            elif coordonnee_souris[0] > coordonnee_boutton_son[0] and coordonnee_souris[1] > coordonnee_boutton_son[1] \
            and coordonnee_souris[0] < coordonnee_boutton_son[0]+50 and coordonnee_souris[1] < coordonnee_boutton_son[1]+50\
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                if son == True :
                    bouton_son_actif_inactif = pygame.image.load('Images//bouton_son_inactif.png')
                    bouton_son_actif_inactif = pygame.transform.scale(bouton_son_actif_inactif,(50,50))
                    son = False
                    volume = 0.0
                elif son == False :
                    bouton_son_actif_inactif = pygame.image.load('Images//bouton_son_actif.png')
                    bouton_son_actif_inactif = pygame.transform.scale(bouton_son_actif_inactif,(50,50))
                    son = True
                    volume = 1




    #boucle principal du jeu
    while running == 3:
        #affichage et creation de la place pricipal
        screen.blit(fond_principal,(0, 0))
        screen.blit(table_daffichage_cartes,(-50,-40))
        screen.blit(table_daffichage_tour_joueur, coordonnee_table_daffichage_tour_joueur)
        screen.blit(table_score,(-50,510))

        #affichage du score
        if temp_affichage_score > 0:
            screen.blit(score_en_activite,(coordonnee_baniere_passage[0]+60,coordonnee_baniere_passage[1]-300))
            temp_affichage_score -= 1


        if tour_joueur == 10:
            screen.blit(texte_score,(490, 568))
            screen.blit(texte_score_joueur,(110,575))
        else :
            screen.blit(texte_score_joueur,(110,575))
            screen.blit(texte_score,(480, 568))


        #boutton son
        screen.blit(bouton_son_actif_inactif,coordonnee_boutton_son)

        #affichage du tour du joueurs
        screen.blit(texte_tour_joueur,(930,100))




        if tour_joueur == 1:
            score_affichage = score_joueur_1
            texte_score = police50.render(str(score_affichage),False,(255,255,255))
            texte_tour_joueur = police36.render(str_joueur_1, False,couleur_blanche)
            texte_score_joueur = police36.render(str_joueur_1_score, False,couleur_blanche)
            if son_tour_joueur == True :
                son_passage_j_1.set_volume(volume)
                son_passage_j_1.play()
                son_tour_joueur = False

        elif tour_joueur == 2:
            score_affichage = score_joueur_2
            texte_score = police50.render(str(score_affichage),False,(255,255,255))
            texte_tour_joueur = police36.render(str_joueur_2, False,couleur_blanche)
            texte_score_joueur = police36.render(str_joueur_2_score, False,couleur_blanche)
            if son_tour_joueur == True :
                son_passage_j_2.set_volume(volume)
                son_passage_j_2.play()
                son_tour_joueur = False

        elif tour_joueur == 3:
            score_affichage = score_joueur_3
            texte_score = police50.render(str(score_affichage),False,(255,255,255))
            texte_tour_joueur = police36.render(str_joueur_3, False,couleur_blanche)
            texte_score_joueur = police36.render(str_joueur_3_score, False,couleur_blanche)
            if son_tour_joueur == True :
                son_passage_j_3.set_volume(volume)
                son_passage_j_3.play()
                son_tour_joueur = False

        elif tour_joueur == 4:
            score_affichage = score_joueur_4
            texte_score = police50.render(str(score_affichage),False,(255,255,255))
            texte_tour_joueur = police36.render(str_joueur_4, False,couleur_blanche)
            texte_score_joueur = police36.render(str_joueur_4_score, False,couleur_blanche)
            if son_tour_joueur == True :
                son_passage_j_4.set_volume(volume)
                son_passage_j_4.play()
                son_tour_joueur = False

        elif tour_joueur == 5:
            score_affichage = score_joueur_5
            texte_score = police50.render(str(score_affichage),False,(255,255,255))
            texte_tour_joueur = police36.render(str_joueur_5, False,couleur_blanche)
            texte_score_joueur = police36.render(str_joueur_5_score, False,couleur_blanche)
            if son_tour_joueur == True :
                son_passage_j_5.set_volume(volume)
                son_passage_j_5.play()
                son_tour_joueur = False

        elif tour_joueur == 6:
            score_affichage = score_joueur_6
            texte_score = police50.render(str(score_affichage),False,(255,255,255))
            texte_tour_joueur = police36.render(str_joueur_6, False,couleur_blanche)
            texte_score_joueur = police36.render(str_joueur_6_score, False,couleur_blanche)
            if son_tour_joueur == True :
                son_passage_j_6.set_volume(volume)
                son_passage_j_6.play()
                son_tour_joueur = False

        elif tour_joueur == 7:
            score_affichage = score_joueur_7
            texte_score = police50.render(str(score_affichage),False,(255,255,255))
            texte_tour_joueur = police36.render(str_joueur_7, False,couleur_blanche)
            texte_score_joueur = police36.render(str_joueur_7_score, False,couleur_blanche)
            if son_tour_joueur == True :
                son_passage_j_7.set_volume(volume)
                son_passage_j_7.play()
                son_tour_joueur = False

        elif tour_joueur == 8:
            score_affichage = score_joueur_8
            texte_score = police50.render(str(score_affichage),False,(255,255,255))
            texte_tour_joueur = police36.render(str_joueur_8, False,couleur_blanche)
            texte_score_joueur = police36.render(str_joueur_8_score, False,couleur_blanche)
            if son_tour_joueur == True :
                son_passage_j_8.set_volume(volume)
                son_passage_j_8.play()
                son_tour_joueur = False

        elif tour_joueur == 9:
            score_affichage = score_joueur_9
            texte_score = police50.render(str(score_affichage),False,(255,255,255))
            texte_tour_joueur = police36.render(str_joueur_9, False,couleur_blanche)
            texte_score_joueur = police36.render(str_joueur_9_score, False,couleur_blanche)
            if son_tour_joueur == True :
                son_passage_j_9.set_volume(volume)
                son_passage_j_9.play()
                son_tour_joueur = False

        elif tour_joueur == 10:
            score_affichage = score_joueur_10
            texte_score = police50.render(str(score_affichage),False,(255,255,255))
            texte_tour_joueur = police36.render(str_joueur_10, False,couleur_blanche)
            texte_score_joueur = police36.render(str_joueur_10_score, False,couleur_blanche)
            if son_tour_joueur == True :
                son_passage_j_10.set_volume(volume)
                son_passage_j_10.play()
                son_tour_joueur = False







        #grossissement des cartes en cas de passage avec la souris
        coordonnee_souris = pygame.mouse.get_pos()
        if coordonnee_souris[0] > 100 and coordonnee_souris[1] > 75 and coordonnee_souris[0] < 173 and coordonnee_souris[1] < 187:
            carte_0 = pygame.transform.scale(carte_0, (85,122))
            screen.blit(carte_0, (position_carte_0[0]-5, position_carte_0[1]-5))
            screen.blit(carte_1, position_carte_1)
            screen.blit(carte_2, position_carte_2)
            screen.blit(carte_3, position_carte_3)
            screen.blit(carte_4, position_carte_4)
            screen.blit(carte_5, position_carte_5)
            screen.blit(carte_6, position_carte_6)
            screen.blit(carte_7, position_carte_7)
            screen.blit(carte_8, position_carte_8)
            screen.blit(carte_9, position_carte_9)
            screen.blit(carte_plus2, position_carte_plus2)
            screen.blit(carte_plus4, position_carte_plus4)
            screen.blit(carte_c_c, position_carte_c_c)
            screen.blit(carte_c_s, position_carte_c_s)
            screen.blit(carte_s_i, position_carte_s_i)
                    #affichage boutton passage
            screen.blit(baniere_passez_joueur_suivant,coordonnee_baniere_passage)

        elif coordonnee_souris[0] > 200 and coordonnee_souris[1] > 75 and coordonnee_souris[0] < 273 and coordonnee_souris[1] < 187:
            carte_1 = pygame.transform.scale(carte_1, (85,122))
            screen.blit(carte_1, (position_carte_1[0]-5, position_carte_1[1]-5))

            screen.blit(carte_0, position_carte_0)
            screen.blit(carte_2, position_carte_2)
            screen.blit(carte_3, position_carte_3)
            screen.blit(carte_4, position_carte_4)
            screen.blit(carte_5, position_carte_5)
            screen.blit(carte_6, position_carte_6)
            screen.blit(carte_7, position_carte_7)
            screen.blit(carte_8, position_carte_8)
            screen.blit(carte_9, position_carte_9)
            screen.blit(carte_plus2, position_carte_plus2)
            screen.blit(carte_plus4, position_carte_plus4)
            screen.blit(carte_c_c, position_carte_c_c)
            screen.blit(carte_c_s, position_carte_c_s)
            screen.blit(carte_s_i, position_carte_s_i)
                    #affichage boutton passage
            screen.blit(baniere_passez_joueur_suivant,coordonnee_baniere_passage)

        elif coordonnee_souris[0] > 300 and coordonnee_souris[1] > 75 and coordonnee_souris[0] < 373 and coordonnee_souris[1] < 187:
            carte_2 = pygame.transform.scale(carte_2, (85,122))
            screen.blit(carte_2, (position_carte_2[0]-5, position_carte_2[1]-5))

            screen.blit(carte_0, position_carte_0)
            screen.blit(carte_1, position_carte_1)
            screen.blit(carte_3, position_carte_3)
            screen.blit(carte_4, position_carte_4)
            screen.blit(carte_5, position_carte_5)
            screen.blit(carte_6, position_carte_6)
            screen.blit(carte_7, position_carte_7)
            screen.blit(carte_8, position_carte_8)
            screen.blit(carte_9, position_carte_9)
            screen.blit(carte_plus2, position_carte_plus2)
            screen.blit(carte_plus4, position_carte_plus4)
            screen.blit(carte_c_c, position_carte_c_c)
            screen.blit(carte_c_s, position_carte_c_s)
            screen.blit(carte_s_i, position_carte_s_i)
                    #affichage boutton passage
            screen.blit(baniere_passez_joueur_suivant,coordonnee_baniere_passage)

        elif coordonnee_souris[0] > 400 and coordonnee_souris[1] > 75 and coordonnee_souris[0] < 473 and coordonnee_souris[1] < 187:
            carte_3 = pygame.transform.scale(carte_3, (85,122))
            screen.blit(carte_3, (position_carte_3[0]-5, position_carte_3[1]-5))

            screen.blit(carte_0, position_carte_0)
            screen.blit(carte_1, position_carte_1)
            screen.blit(carte_2, position_carte_2)
            screen.blit(carte_4, position_carte_4)
            screen.blit(carte_5, position_carte_5)
            screen.blit(carte_6, position_carte_6)
            screen.blit(carte_7, position_carte_7)
            screen.blit(carte_8, position_carte_8)
            screen.blit(carte_9, position_carte_9)
            screen.blit(carte_plus2, position_carte_plus2)
            screen.blit(carte_plus4, position_carte_plus4)
            screen.blit(carte_c_c, position_carte_c_c)
            screen.blit(carte_c_s, position_carte_c_s)
            screen.blit(carte_s_i, position_carte_s_i)
                    #affichage boutton passage
            screen.blit(baniere_passez_joueur_suivant,coordonnee_baniere_passage)

        elif coordonnee_souris[0] > 500 and coordonnee_souris[1] > 75 and coordonnee_souris[0] < 573 and coordonnee_souris[1] < 187:
            carte_4 = pygame.transform.scale(carte_4, (85,122))
            screen.blit(carte_4, (position_carte_4[0]-5, position_carte_4[1]-5))

            screen.blit(carte_0, position_carte_0)
            screen.blit(carte_1, position_carte_1)
            screen.blit(carte_2, position_carte_2)
            screen.blit(carte_3, position_carte_3)
            screen.blit(carte_5, position_carte_5)
            screen.blit(carte_6, position_carte_6)
            screen.blit(carte_7, position_carte_7)
            screen.blit(carte_8, position_carte_8)
            screen.blit(carte_9, position_carte_9)
            screen.blit(carte_plus2, position_carte_plus2)
            screen.blit(carte_plus4, position_carte_plus4)
            screen.blit(carte_c_c, position_carte_c_c)
            screen.blit(carte_c_s, position_carte_c_s)
            screen.blit(carte_s_i, position_carte_s_i)
                    #affichage boutton passage
            screen.blit(baniere_passez_joueur_suivant,coordonnee_baniere_passage)

        elif coordonnee_souris[0] > 100 and coordonnee_souris[1] > 225 and coordonnee_souris[0] < 173 and coordonnee_souris[1] < 337:
            carte_5 = pygame.transform.scale(carte_5, (85,122))
            screen.blit(carte_5, (position_carte_5[0]-5, position_carte_5[1]-5))

            screen.blit(carte_0, position_carte_0)
            screen.blit(carte_1, position_carte_1)
            screen.blit(carte_2, position_carte_2)
            screen.blit(carte_3, position_carte_3)
            screen.blit(carte_4, position_carte_4)
            screen.blit(carte_6, position_carte_6)
            screen.blit(carte_7, position_carte_7)
            screen.blit(carte_8, position_carte_8)
            screen.blit(carte_9, position_carte_9)
            screen.blit(carte_plus2, position_carte_plus2)
            screen.blit(carte_plus4, position_carte_plus4)
            screen.blit(carte_c_c, position_carte_c_c)
            screen.blit(carte_c_s, position_carte_c_s)
            screen.blit(carte_s_i, position_carte_s_i)
                    #affichage boutton passage
            screen.blit(baniere_passez_joueur_suivant,coordonnee_baniere_passage)

        elif coordonnee_souris[0] > 200 and coordonnee_souris[1] > 225 and coordonnee_souris[0] < 273 and coordonnee_souris[1] < 337:
            carte_6 = pygame.transform.scale(carte_6, (85,122))
            screen.blit(carte_6, (position_carte_6[0]-5, position_carte_6[1]-5))

            screen.blit(carte_0, position_carte_0)
            screen.blit(carte_1, position_carte_1)
            screen.blit(carte_2, position_carte_2)
            screen.blit(carte_3, position_carte_3)
            screen.blit(carte_4, position_carte_4)
            screen.blit(carte_5, position_carte_5)
            screen.blit(carte_7, position_carte_7)
            screen.blit(carte_8, position_carte_8)
            screen.blit(carte_9, position_carte_9)
            screen.blit(carte_plus2, position_carte_plus2)
            screen.blit(carte_plus4, position_carte_plus4)
            screen.blit(carte_c_c, position_carte_c_c)
            screen.blit(carte_c_s, position_carte_c_s)
            screen.blit(carte_s_i, position_carte_s_i)
                    #affichage boutton passage
            screen.blit(baniere_passez_joueur_suivant,coordonnee_baniere_passage)

        elif coordonnee_souris[0] > 300 and coordonnee_souris[1] > 225 and coordonnee_souris[0] < 373 and coordonnee_souris[1] < 337:
            carte_7 = pygame.transform.scale(carte_7, (85,122))
            screen.blit(carte_7, (position_carte_7[0]-5, position_carte_7[1]-5))

            screen.blit(carte_0, position_carte_0)
            screen.blit(carte_1, position_carte_1)
            screen.blit(carte_2, position_carte_2)
            screen.blit(carte_3, position_carte_3)
            screen.blit(carte_4, position_carte_4)
            screen.blit(carte_5, position_carte_5)
            screen.blit(carte_6, position_carte_6)
            screen.blit(carte_8, position_carte_8)
            screen.blit(carte_9, position_carte_9)
            screen.blit(carte_plus2, position_carte_plus2)
            screen.blit(carte_plus4, position_carte_plus4)
            screen.blit(carte_c_c, position_carte_c_c)
            screen.blit(carte_c_s, position_carte_c_s)
            screen.blit(carte_s_i, position_carte_s_i)
                    #affichage boutton passage
            screen.blit(baniere_passez_joueur_suivant,coordonnee_baniere_passage)

        elif coordonnee_souris[0] > 400 and coordonnee_souris[1] > 225 and coordonnee_souris[0] < 473 and coordonnee_souris[1] < 337:
            carte_8 = pygame.transform.scale(carte_8, (85,122))
            screen.blit(carte_8, (position_carte_8[0]-5, position_carte_8[1]-5))

            screen.blit(carte_0, position_carte_0)
            screen.blit(carte_1, position_carte_1)
            screen.blit(carte_2, position_carte_2)
            screen.blit(carte_3, position_carte_3)
            screen.blit(carte_4, position_carte_4)
            screen.blit(carte_5, position_carte_5)
            screen.blit(carte_6, position_carte_6)
            screen.blit(carte_7, position_carte_7)
            screen.blit(carte_9, position_carte_9)
            screen.blit(carte_plus2, position_carte_plus2)
            screen.blit(carte_plus4, position_carte_plus4)
            screen.blit(carte_c_c, position_carte_c_c)
            screen.blit(carte_c_s, position_carte_c_s)
            screen.blit(carte_s_i, position_carte_s_i)
                    #affichage boutton passage
            screen.blit(baniere_passez_joueur_suivant,coordonnee_baniere_passage)

        elif coordonnee_souris[0] > 500 and coordonnee_souris[1] > 225 and coordonnee_souris[0] < 573 and coordonnee_souris[1] < 337:
            carte_9 = pygame.transform.scale(carte_9, (85,122))
            screen.blit(carte_9, (position_carte_9[0]-5, position_carte_9[1]-5))

            screen.blit(carte_0, position_carte_0)
            screen.blit(carte_1, position_carte_1)
            screen.blit(carte_2, position_carte_2)
            screen.blit(carte_3, position_carte_3)
            screen.blit(carte_4, position_carte_4)
            screen.blit(carte_5, position_carte_5)
            screen.blit(carte_6, position_carte_6)
            screen.blit(carte_7, position_carte_7)
            screen.blit(carte_8, position_carte_8)
            screen.blit(carte_plus2, position_carte_plus2)
            screen.blit(carte_plus4, position_carte_plus4)
            screen.blit(carte_c_c, position_carte_c_c)
            screen.blit(carte_c_s, position_carte_c_s)
            screen.blit(carte_s_i, position_carte_s_i)
                    #affichage boutton passage
            screen.blit(baniere_passez_joueur_suivant,coordonnee_baniere_passage)

        elif coordonnee_souris[0] > 100 and coordonnee_souris[1] > 375 and coordonnee_souris[0] < 173 and coordonnee_souris[1] < 487:
            carte_plus2 = pygame.transform.scale(carte_plus2, (85,122))
            screen.blit(carte_plus2, (position_carte_plus2[0]-5, position_carte_plus2[1]-5))

            screen.blit(carte_0, position_carte_0)
            screen.blit(carte_1, position_carte_1)
            screen.blit(carte_2, position_carte_2)
            screen.blit(carte_3, position_carte_3)
            screen.blit(carte_4, position_carte_4)
            screen.blit(carte_5, position_carte_5)
            screen.blit(carte_6, position_carte_6)
            screen.blit(carte_7, position_carte_7)
            screen.blit(carte_8, position_carte_8)
            screen.blit(carte_9, position_carte_9)
            screen.blit(carte_plus4, position_carte_plus4)
            screen.blit(carte_c_c, position_carte_c_c)
            screen.blit(carte_c_s, position_carte_c_s)
            screen.blit(carte_s_i, position_carte_s_i)
                    #affichage boutton passage
            screen.blit(baniere_passez_joueur_suivant,coordonnee_baniere_passage)

        elif coordonnee_souris[0] > 200 and coordonnee_souris[1] > 375 and coordonnee_souris[0] < 273 and coordonnee_souris[1] < 487:
            carte_plus4 = pygame.transform.scale(carte_plus4, (85,122))
            screen.blit(carte_plus4, (position_carte_plus4[0]-5, position_carte_plus4[1]-5))

            screen.blit(carte_0, position_carte_0)
            screen.blit(carte_1, position_carte_1)
            screen.blit(carte_2, position_carte_2)
            screen.blit(carte_3, position_carte_3)
            screen.blit(carte_4, position_carte_4)
            screen.blit(carte_5, position_carte_5)
            screen.blit(carte_6, position_carte_6)
            screen.blit(carte_7, position_carte_7)
            screen.blit(carte_8, position_carte_8)
            screen.blit(carte_9, position_carte_9)
            screen.blit(carte_plus2, position_carte_plus2)
            screen.blit(carte_c_c, position_carte_c_c)
            screen.blit(carte_c_s, position_carte_c_s)
            screen.blit(carte_s_i, position_carte_s_i)
                    #affichage boutton passage
            screen.blit(baniere_passez_joueur_suivant,coordonnee_baniere_passage)

        elif coordonnee_souris[0] > 300 and coordonnee_souris[1] > 375 and coordonnee_souris[0] < 373 and coordonnee_souris[1] < 487:
            carte_c_c = pygame.transform.scale(carte_c_c, (85,122))
            screen.blit(carte_c_c, (position_carte_c_c[0]-5, position_carte_c_c[1]-5))

            screen.blit(carte_0, position_carte_0)
            screen.blit(carte_1, position_carte_1)
            screen.blit(carte_2, position_carte_2)
            screen.blit(carte_3, position_carte_3)
            screen.blit(carte_4, position_carte_4)
            screen.blit(carte_5, position_carte_5)
            screen.blit(carte_6, position_carte_6)
            screen.blit(carte_7, position_carte_7)
            screen.blit(carte_8, position_carte_8)
            screen.blit(carte_9, position_carte_9)
            screen.blit(carte_plus2, position_carte_plus2)
            screen.blit(carte_plus4, position_carte_plus4)
            screen.blit(carte_c_s, position_carte_c_s)
            screen.blit(carte_s_i, position_carte_s_i)
                    #affichage boutton passage
            screen.blit(baniere_passez_joueur_suivant,coordonnee_baniere_passage)

        elif coordonnee_souris[0] > 400 and coordonnee_souris[1] > 375 and coordonnee_souris[0] < 473 and coordonnee_souris[1] < 487:
            carte_c_s = pygame.transform.scale(carte_c_s, (85,122))
            screen.blit(carte_c_s, (position_carte_c_s[0]-5, position_carte_c_s[1]-5))

            screen.blit(carte_0, position_carte_0)
            screen.blit(carte_1, position_carte_1)
            screen.blit(carte_2, position_carte_2)
            screen.blit(carte_3, position_carte_3)
            screen.blit(carte_4, position_carte_4)
            screen.blit(carte_5, position_carte_5)
            screen.blit(carte_6, position_carte_6)
            screen.blit(carte_7, position_carte_7)
            screen.blit(carte_8, position_carte_8)
            screen.blit(carte_9, position_carte_9)
            screen.blit(carte_plus2, position_carte_plus2)
            screen.blit(carte_plus4, position_carte_plus4)
            screen.blit(carte_c_c, position_carte_c_c)
            screen.blit(carte_s_i, position_carte_s_i)
                    #affichage boutton passage
            screen.blit(baniere_passez_joueur_suivant,coordonnee_baniere_passage)

        elif coordonnee_souris[0] > 500 and coordonnee_souris[1] > 375 and coordonnee_souris[0] < 573 and coordonnee_souris[1] < 487:
            carte_s_i = pygame.transform.scale(carte_s_i, (85,122))
            screen.blit(carte_s_i, (position_carte_s_i[0]-5, position_carte_s_i[1]-5))

            screen.blit(carte_0, position_carte_0)
            screen.blit(carte_1, position_carte_1)
            screen.blit(carte_2, position_carte_2)
            screen.blit(carte_3, position_carte_3)
            screen.blit(carte_4, position_carte_4)
            screen.blit(carte_5, position_carte_5)
            screen.blit(carte_6, position_carte_6)
            screen.blit(carte_7, position_carte_7)
            screen.blit(carte_8, position_carte_8)
            screen.blit(carte_9, position_carte_9)
            screen.blit(carte_plus2, position_carte_plus2)
            screen.blit(carte_plus4, position_carte_plus4)
            screen.blit(carte_c_c, position_carte_c_c)
            screen.blit(carte_c_s, position_carte_c_s)
                    #affichage boutton passage
            screen.blit(baniere_passez_joueur_suivant,coordonnee_baniere_passage)










        else :
            #etat de base des cartes

            carte_0=pygame.image.load("Images//cartes//carte_0.jpg")
            carte_1=pygame.image.load("Images//cartes//carte_1.jpg")
            carte_2=pygame.image.load("Images//cartes//carte_2.jpg")
            carte_3=pygame.image.load("Images//cartes//carte_3.jpg")
            carte_4=pygame.image.load("Images//cartes//carte_4.jpg")
            carte_5=pygame.image.load("Images//cartes//carte_5.jpg")
            carte_6=pygame.image.load("Images//cartes//carte_6.jpg")
            carte_7=pygame.image.load("Images//cartes//carte_7.jpg")
            carte_8=pygame.image.load("Images//cartes//carte_8.jpg")
            carte_9=pygame.image.load("Images//cartes//carte_9.jpg")
            carte_plus2=pygame.image.load("Images//cartes//carte_+2.jpg")
            carte_plus4=pygame.image.load("Images//cartes//carte_+4.jpg")
            carte_c_c=pygame.image.load("Images//cartes//carte_c_c.jpg")
            carte_c_s=pygame.image.load("Images//cartes//carte_c_s.jpg")
            carte_s_i=pygame.image.load("Images//cartes//carte_s_i.jpg")
            baniere_passez_joueur_suivant = pygame.transform.scale(baniere_passez_joueur_suivant,(333,83))

            screen.blit(carte_0, position_carte_0)
            screen.blit(carte_1, position_carte_1)
            screen.blit(carte_2, position_carte_2)
            screen.blit(carte_3, position_carte_3)
            screen.blit(carte_4, position_carte_4)
            screen.blit(carte_5, position_carte_5)
            screen.blit(carte_6, position_carte_6)
            screen.blit(carte_7, position_carte_7)
            screen.blit(carte_8, position_carte_8)
            screen.blit(carte_9, position_carte_9)
            screen.blit(carte_plus2, position_carte_plus2)
            screen.blit(carte_plus4, position_carte_plus4)
            screen.blit(carte_c_c, position_carte_c_c)
            screen.blit(carte_c_s, position_carte_c_s)
            screen.blit(carte_s_i, position_carte_s_i)

            #affichage boutton passage
            screen.blit(baniere_passez_joueur_suivant,coordonnee_baniere_passage)





        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
            #mise en place du boutton son
            elif coordonnee_souris[0] > coordonnee_boutton_son[0] and coordonnee_souris[1] > coordonnee_boutton_son[1] \
            and coordonnee_souris[0] < coordonnee_boutton_son[0]+50 and coordonnee_souris[1] < coordonnee_boutton_son[1]+50\
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                if son == True :
                    bouton_son_actif_inactif = pygame.image.load('Images//bouton_son_inactif.png')
                    bouton_son_actif_inactif = pygame.transform.scale(bouton_son_actif_inactif,(50,50))
                    son = False
                    volume = 0.0
                elif son == False :
                    bouton_son_actif_inactif = pygame.image.load('Images//bouton_son_actif.png')
                    bouton_son_actif_inactif = pygame.transform.scale(bouton_son_actif_inactif,(50,50))
                    son = True
                    volume = 1

            elif coordonnee_souris[0] > coordonnee_baniere_passage[0] and coordonnee_souris[1] > coordonnee_baniere_passage[1] \
            and coordonnee_souris[0] < coordonnee_baniere_passage[0]+333 and coordonnee_souris[1] < coordonnee_baniere_passage[1]+83\
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and tour_joueur == nbr_joueurs:
                running = 4

            elif coordonnee_souris[0] > coordonnee_baniere_passage[0] and coordonnee_souris[1] > coordonnee_baniere_passage[1] \
            and coordonnee_souris[0] < coordonnee_baniere_passage[0]+333 and coordonnee_souris[1] < coordonnee_baniere_passage[1]+83\
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                if tour_joueur+1 >= nbr_joueurs:
                    baniere_passez_joueur_suivant = pygame.image.load('Images//baniere_afficher_score.png')
                    baniere_passez_joueur_suivant = pygame.transform.scale(baniere_passez_joueur_suivant,(333,83))
                    tour_joueur += 1


                elif tour_joueur < nbr_joueurs:
                    tour_joueur += 1

                baniere_passez_joueur_suivant = pygame.transform.scale(baniere_passez_joueur_suivant,(323,73))
                screen.blit(baniere_passez_joueur_suivant,(coordonnee_baniere_passage[0]+5,coordonnee_baniere_passage[1]+5))
                screen.blit(carte_0, position_carte_0)
                screen.blit(carte_1, position_carte_1)
                screen.blit(carte_2, position_carte_2)
                screen.blit(carte_3, position_carte_3)
                screen.blit(carte_4, position_carte_4)
                screen.blit(carte_5, position_carte_5)
                screen.blit(carte_6, position_carte_6)
                screen.blit(carte_7, position_carte_7)
                screen.blit(carte_8, position_carte_8)
                screen.blit(carte_9, position_carte_9)
                screen.blit(carte_plus2, position_carte_plus2)
                screen.blit(carte_plus4, position_carte_plus4)
                screen.blit(carte_c_c, position_carte_c_c)
                screen.blit(carte_c_s, position_carte_c_s)
                screen.blit(carte_s_i, position_carte_s_i)
                pygame.display.update()
                sleep(0.2)

                son_tour_joueur = True

                #ajout des points
            elif coordonnee_souris[0] > 100 and coordonnee_souris[1] > 75 and coordonnee_souris[0] < 173 and coordonnee_souris[1] < 187\
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                temp_affichage_score = 60
                score_en_activite = score_0
                if tour_joueur == 1:
                    score_joueur_1 += 0

                elif tour_joueur == 2:
                    score_joueur_2 += 0

                elif tour_joueur == 3:
                    score_joueur_3 += 0

                elif tour_joueur == 4:
                    score_joueur_4 += 0

                elif tour_joueur == 5:
                    score_joueur_5 += 0

                elif tour_joueur == 6:
                    score_joueur_6 += 0

                elif tour_joueur == 7:
                    score_joueur_7 += 0

                elif tour_joueur == 8:
                    score_joueur_8 += 0

                elif tour_joueur == 9:
                    score_joueur_9 += 0

                elif tour_joueur == 10:
                    score_joueur_10 += 0



            elif coordonnee_souris[0] > 200 and coordonnee_souris[1] > 75 and coordonnee_souris[0] < 273 and coordonnee_souris[1] < 187\
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                temp_affichage_score = 60

                score_en_activite = score_1
                if tour_joueur == 1:
                    score_joueur_1 += 1

                elif tour_joueur == 2:
                    score_joueur_2 += 1

                elif tour_joueur == 3:
                    score_joueur_3 += 1

                elif tour_joueur == 4:
                    score_joueur_4 += 1

                elif tour_joueur == 5:
                    score_joueur_5 += 1

                elif tour_joueur == 6:
                    score_joueur_6 += 1

                elif tour_joueur == 7:
                    score_joueur_7 += 1

                elif tour_joueur == 8:
                    score_joueur_8 += 1

                elif tour_joueur == 9:
                    score_joueur_9 += 1

                elif tour_joueur == 10:
                    score_joueur_10 += 1

            elif coordonnee_souris[0] > 300 and coordonnee_souris[1] > 75 and coordonnee_souris[0] < 373 and coordonnee_souris[1] < 187\
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                temp_affichage_score = 60


                score_en_activite = score_2
                if tour_joueur == 1:
                    score_joueur_1 += 2

                elif tour_joueur == 2:
                    score_joueur_2 += 2

                elif tour_joueur == 3:
                    score_joueur_3 += 2

                elif tour_joueur == 4:
                    score_joueur_4 += 2

                elif tour_joueur == 5:
                    score_joueur_5 += 2

                elif tour_joueur == 6:
                    score_joueur_6 += 2

                elif tour_joueur == 7:
                    score_joueur_7 += 2

                elif tour_joueur == 8:
                    score_joueur_8 += 2

                elif tour_joueur == 9:
                    score_joueur_9 += 2

                elif tour_joueur == 10:
                    score_joueur_10 += 2

            elif coordonnee_souris[0] > 400 and coordonnee_souris[1] > 75 and coordonnee_souris[0] < 473 and coordonnee_souris[1] < 187\
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                temp_affichage_score = 60


                score_en_activite = score_3
                if tour_joueur == 1:
                    score_joueur_1 += 3

                elif tour_joueur == 2:
                    score_joueur_2 += 3

                elif tour_joueur == 3:
                    score_joueur_3 += 3

                elif tour_joueur == 4:
                    score_joueur_4 += 3

                elif tour_joueur == 5:
                    score_joueur_5 += 3

                elif tour_joueur == 6:
                    score_joueur_6 += 3

                elif tour_joueur == 7:
                    score_joueur_7 += 3

                elif tour_joueur == 8:
                    score_joueur_8 += 3

                elif tour_joueur == 9:
                    score_joueur_9 += 3

                elif tour_joueur == 10:
                    score_joueur_10 += 3

            elif coordonnee_souris[0] > 500 and coordonnee_souris[1] > 75 and coordonnee_souris[0] < 573 and coordonnee_souris[1] < 187\
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                temp_affichage_score = 60


                score_en_activite = score_4
                if tour_joueur == 1:
                    score_joueur_1 += 4

                elif tour_joueur == 2:
                    score_joueur_2 += 4

                elif tour_joueur == 3:
                    score_joueur_3 += 4

                elif tour_joueur == 4:
                    score_joueur_4 += 4

                elif tour_joueur == 5:
                    score_joueur_5 += 4

                elif tour_joueur == 6:
                    score_joueur_6 += 4

                elif tour_joueur == 7:
                    score_joueur_7 += 4

                elif tour_joueur == 8:
                    score_joueur_8 += 4

                elif tour_joueur == 9:
                    score_joueur_9 += 4

                elif tour_joueur == 10:
                    score_joueur_10 += 4

            elif coordonnee_souris[0] > 100 and coordonnee_souris[1] > 225 and coordonnee_souris[0] < 173 and coordonnee_souris[1] < 337\
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                temp_affichage_score = 60


                score_en_activite = score_5
                if tour_joueur == 1:
                    score_joueur_1 += 5

                elif tour_joueur == 2:
                    score_joueur_2 += 5

                elif tour_joueur == 3:
                    score_joueur_3 += 5

                elif tour_joueur == 4:
                    score_joueur_4 += 5

                elif tour_joueur == 5:
                    score_joueur_5 += 5

                elif tour_joueur == 6:
                    score_joueur_6 += 5

                elif tour_joueur == 7:
                    score_joueur_7 += 5

                elif tour_joueur == 8:
                    score_joueur_8 += 5

                elif tour_joueur == 9:
                    score_joueur_9 += 5

                elif tour_joueur == 10:
                    score_joueur_10 += 5

            elif coordonnee_souris[0] > 200 and coordonnee_souris[1] > 225 and coordonnee_souris[0] < 273 and coordonnee_souris[1] < 337\
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                temp_affichage_score = 60


                score_en_activite = score_6
                if tour_joueur == 1:
                    score_joueur_1 += 6

                elif tour_joueur == 2:
                    score_joueur_2 += 6

                elif tour_joueur == 3:
                    score_joueur_3 += 6

                elif tour_joueur == 4:
                    score_joueur_4 += 6

                elif tour_joueur == 5:
                    score_joueur_5 += 6

                elif tour_joueur == 6:
                    score_joueur_6 += 6

                elif tour_joueur == 7:
                    score_joueur_7 += 6

                elif tour_joueur == 8:
                    score_joueur_8 += 6

                elif tour_joueur == 9:
                    score_joueur_9 += 6

                elif tour_joueur == 10:
                    score_joueur_10 += 6

            elif coordonnee_souris[0] > 300 and coordonnee_souris[1] > 225 and coordonnee_souris[0] < 373 and coordonnee_souris[1] < 337\
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                temp_affichage_score = 60


                score_en_activite = score_7
                if tour_joueur == 1:
                    score_joueur_1 += 7

                elif tour_joueur == 2:
                    score_joueur_2 += 7

                elif tour_joueur == 3:
                    score_joueur_3 += 7

                elif tour_joueur == 4:
                    score_joueur_4 += 7

                elif tour_joueur == 5:
                    score_joueur_5 += 7

                elif tour_joueur == 6:
                    score_joueur_6 += 7

                elif tour_joueur == 7:
                    score_joueur_7 += 7

                elif tour_joueur == 8:
                    score_joueur_8 += 7

                elif tour_joueur == 9:
                    score_joueur_9 += 7

                elif tour_joueur == 10:
                    score_joueur_10 += 7

            elif coordonnee_souris[0] > 400 and coordonnee_souris[1] > 225 and coordonnee_souris[0] < 473 and coordonnee_souris[1] < 337\
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                temp_affichage_score = 60


                score_en_activite = score_8
                if tour_joueur == 1:
                    score_joueur_1 += 8

                elif tour_joueur == 2:
                    score_joueur_2 += 8

                elif tour_joueur == 3:
                    score_joueur_3 += 8

                elif tour_joueur == 4:
                    score_joueur_4 += 8

                elif tour_joueur == 5:
                    score_joueur_5 += 8

                elif tour_joueur == 6:
                    score_joueur_6 += 8

                elif tour_joueur == 7:
                    score_joueur_7 += 8

                elif tour_joueur == 8:
                    score_joueur_8 += 8

                elif tour_joueur == 9:
                    score_joueur_9 += 8

                elif tour_joueur == 10:
                    score_joueur_10 += 8

            elif coordonnee_souris[0] > 500 and coordonnee_souris[1] > 225 and coordonnee_souris[0] < 573 and coordonnee_souris[1] < 337\
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                temp_affichage_score = 60


                score_en_activite = score_9
                if tour_joueur == 1:
                    score_joueur_1 += 9

                elif tour_joueur == 2:
                    score_joueur_2 += 9

                elif tour_joueur == 3:
                    score_joueur_3 += 9

                elif tour_joueur == 4:
                    score_joueur_4 += 9

                elif tour_joueur == 5:
                    score_joueur_5 += 9

                elif tour_joueur == 6:
                    score_joueur_6 += 9

                elif tour_joueur == 7:
                    score_joueur_7 += 9

                elif tour_joueur == 8:
                    score_joueur_8 += 9

                elif tour_joueur == 9:
                    score_joueur_9 += 9

                elif tour_joueur == 10:
                    score_joueur_10 += 9

            elif coordonnee_souris[0] > 100 and coordonnee_souris[1] > 375 and coordonnee_souris[0] < 173 and coordonnee_souris[1] < 487\
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                temp_affichage_score = 60


                score_en_activite = score_20
                if tour_joueur == 1:
                    score_joueur_1 += 20

                elif tour_joueur == 2:
                    score_joueur_2 += 20

                elif tour_joueur == 3:
                    score_joueur_3 += 20

                elif tour_joueur == 4:
                    score_joueur_4 += 20

                elif tour_joueur == 5:
                    score_joueur_5 += 20

                elif tour_joueur == 6:
                    score_joueur_6 += 20

                elif tour_joueur == 7:
                    score_joueur_7 += 20

                elif tour_joueur == 8:
                    score_joueur_8 += 20

                elif tour_joueur == 9:
                    score_joueur_9 += 20

                elif tour_joueur == 10:
                    score_joueur_10 += 20

            elif coordonnee_souris[0] > 200 and coordonnee_souris[1] > 375 and coordonnee_souris[0] < 273 and coordonnee_souris[1] < 487\
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                temp_affichage_score = 60

                score_en_activite = score_50
                if tour_joueur == 1:
                    score_joueur_1 += 50

                elif tour_joueur == 2:
                    score_joueur_2 += 50

                elif tour_joueur == 3:
                    score_joueur_3 += 50

                elif tour_joueur == 4:
                    score_joueur_4 += 50

                elif tour_joueur == 5:
                    score_joueur_5 += 50

                elif tour_joueur == 6:
                    score_joueur_6 += 50

                elif tour_joueur == 7:
                    score_joueur_7 += 50

                elif tour_joueur == 8:
                    score_joueur_8 += 50

                elif tour_joueur == 9:
                    score_joueur_9 += 50

                elif tour_joueur == 10:
                    score_joueur_10 += 50

            elif coordonnee_souris[0] > 300 and coordonnee_souris[1] > 375 and coordonnee_souris[0] < 373 and coordonnee_souris[1] < 487\
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                temp_affichage_score = 60


                score_en_activite = score_50
                if tour_joueur == 1:
                    score_joueur_1 += 50

                elif tour_joueur == 2:
                    score_joueur_2 += 50

                elif tour_joueur == 3:
                    score_joueur_3 += 50

                elif tour_joueur == 4:
                    score_joueur_4 += 50

                elif tour_joueur == 5:
                    score_joueur_5 += 50

                elif tour_joueur == 6:
                    score_joueur_6 += 50

                elif tour_joueur == 7:
                    score_joueur_7 += 50

                elif tour_joueur == 8:
                    score_joueur_8 += 50

                elif tour_joueur == 9:
                    score_joueur_9 += 50

                elif tour_joueur == 10:
                    score_joueur_10 += 50

            elif coordonnee_souris[0] > 400 and coordonnee_souris[1] > 375 and coordonnee_souris[0] < 473 and coordonnee_souris[1] < 487\
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                temp_affichage_score = 60


                score_en_activite = score_20
                if tour_joueur == 1:
                    score_joueur_1 += 20

                elif tour_joueur == 2:
                    score_joueur_2 += 20

                elif tour_joueur == 3:
                    score_joueur_3 += 20

                elif tour_joueur == 4:
                    score_joueur_4 += 20

                elif tour_joueur == 5:
                    score_joueur_5 += 20

                elif tour_joueur == 6:
                    score_joueur_6 += 20

                elif tour_joueur == 7:
                    score_joueur_7 += 20

                elif tour_joueur == 8:
                    score_joueur_8 += 20

                elif tour_joueur == 9:
                    score_joueur_9 += 20

                elif tour_joueur == 10:
                    score_joueur_10 += 20

            elif coordonnee_souris[0] > 500 and coordonnee_souris[1] > 375 and coordonnee_souris[0] < 573 and coordonnee_souris[1] < 487\
            and event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                temp_affichage_score = 60

                score_en_activite = score_20
                if tour_joueur == 1:
                    score_joueur_1 += 20

                elif tour_joueur == 2:
                    score_joueur_2 += 20

                elif tour_joueur == 3:
                    score_joueur_3 += 20

                elif tour_joueur == 4:
                    score_joueur_4 += 20

                elif tour_joueur == 5:
                    score_joueur_5 += 20

                elif tour_joueur == 6:
                    score_joueur_6 += 20

                elif tour_joueur == 7:
                    score_joueur_7 += 20

                elif tour_joueur == 8:
                    score_joueur_8 += 20

                elif tour_joueur == 9:
                    score_joueur_9 += 20

                elif tour_joueur == 10:
                    score_joueur_10 += 20




    #boucle d'affichage des score
    while running == 4:
        #affichage et creation de la place pricipal
        screen.blit(fond_principal,(0, 0))
        screen.blit(table_daffichage_score_final,(0,0))

        list_score = []



        if nbr_joueurs >= 2 :
            texte_score_joueur_1 = police36.render(str(score_joueur_1),False,(255,255,255))
            score_joueur_1_final = police36.render(str_joueur_1_score,False,(255,255,255))
            screen.blit(texte_score_joueur_1,(570,150))
            screen.blit(score_joueur_1_final,(200,150))
            list_score.append(score_joueur_1)


            texte_score_joueur_2 = police36.render(str(score_joueur_2),False,(255,255,255))
            score_joueur_2_final = police36.render(str_joueur_2_score,False,(255,255,255))
            screen.blit(texte_score_joueur_2,(570,200))
            screen.blit(score_joueur_2_final,(200,200))
            list_score.append(score_joueur_2)

        if nbr_joueurs >= 3 :
            texte_score_joueur_3 = police36.render(str(score_joueur_3),False,(255,255,255))
            score_joueur_3_final = police36.render(str_joueur_3_score,False,(255,255,255))
            screen.blit(texte_score_joueur_3,(570,250))
            screen.blit(score_joueur_3_final,(200,250))
            list_score.append(score_joueur_3)

        if nbr_joueurs >= 4 :
            texte_score_joueur_4 = police36.render(str(score_joueur_4),False,(255,255,255))
            score_joueur_4_final = police36.render(str_joueur_4_score,False,(255,255,255))
            screen.blit(texte_score_joueur_4,(570,300))
            screen.blit(score_joueur_4_final,(200,300))
            list_score.append(score_joueur_4)

        if nbr_joueurs >= 5 :
            texte_score_joueur_5 = police36.render(str(score_joueur_5),False,(255,255,255))
            score_joueur_5_final = police36.render(str_joueur_5_score,False,(255,255,255))
            screen.blit(texte_score_joueur_5,(570,350))
            screen.blit(score_joueur_5_final,(200,350))
            list_score.append(score_joueur_5)

        if nbr_joueurs >= 6 :
            texte_score_joueur_6 = police36.render(str(score_joueur_6),False,(255,255,255))
            score_joueur_6_final = police36.render(str_joueur_6_score,False,(255,255,255))
            screen.blit(texte_score_joueur_6,(570,400))
            screen.blit(score_joueur_6_final,(200,400))
            list_score.append(score_joueur_6)

        if nbr_joueurs >= 7 :
            texte_score_joueur_7 = police36.render(str(score_joueur_7),False,(255,255,255))
            score_joueur_7_final = police36.render(str_joueur_7_score,False,(255,255,255))
            screen.blit(texte_score_joueur_7,(570,450))
            screen.blit(score_joueur_7_final,(200,450))
            list_score.append(score_joueur_7)

        if nbr_joueurs >= 8 :
            texte_score_joueur_8 = police36.render(str(score_joueur_8),False,(255,255,255))
            score_joueur_8_final = police36.render(str_joueur_8_score,False,(255,255,255))
            screen.blit(texte_score_joueur_8,(570,500))
            screen.blit(score_joueur_8_final,(200,500))
            list_score.append(score_joueur_8)

        if nbr_joueurs >= 9 :
            texte_score_joueur_9 = police36.render(str(score_joueur_9),False,(255,255,255))
            score_joueur_9_final = police36.render(str_joueur_9_score,False,(255,255,255))
            screen.blit(texte_score_joueur_9,(570,550))
            screen.blit(score_joueur_9_final,(200,550))
            list_score.append(score_joueur_9)

        if nbr_joueurs >= 10 :
            texte_score_joueur_10 = police36.render(str(score_joueur_10),False,(255,255,255))
            score_joueur_10_final = police36.render(str_joueur_10_score,False,(255,255,255))
            screen.blit(texte_score_joueur_10,(580,600))
            screen.blit(score_joueur_10_final,(200,600))
            list_score.append(score_joueur_10)

        list_score.sort()
        texte_gagnant = "Le grand gagnant est : "


        if list_score[0] == score_joueur_1:
            joueur_gagnant =  str_joueur_1

        elif list_score[0] == score_joueur_2:
            joueur_gagnant =  str_joueur_2

        elif list_score[0] == score_joueur_3:
            joueur_gagnant =  str_joueur_3

        elif list_score[0] == score_joueur_4:
            joueur_gagnant =  str_joueur_4

        elif list_score[0] == score_joueur_5:
            joueur_gagnant =  str_joueur_5

        elif list_score[0] == score_joueur_6:
            joueur_gagnant =  str_joueur_6

        elif list_score[0] == score_joueur_7:
            joueur_gagnant =  str_joueur_7

        elif list_score[0] == score_joueur_8:
            joueur_gagnant =  str_joueur_8

        elif list_score[0] == score_joueur_9:
            joueur_gagnant =  str_joueur_9

        elif list_score[0] == score_joueur_10:
            joueur_gagnant =  str_joueur_10



        texte_joueur_gagnant = police50.render(joueur_gagnant,False,(130,180,245))
        texte_gagnant = police36.render(texte_gagnant,False,(130,180,245))
        screen.blit(texte_gagnant,(700,dimension_fenetre[1]-dimension_fenetre[1]//2))
        screen.blit(texte_joueur_gagnant,(810,dimension_fenetre[1]-dimension_fenetre[1]//2+50))














        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT :
                running = 1
                #reinitialisation des variables

                    #le tour du joueur est 1 car on commence par compter les points du joueur 1
                tour_joueur = 1

                #score des joueurs
                score_joueur_1 = 0
                score_joueur_2 = 0
                score_joueur_3 = 0
                score_joueur_4 = 0
                score_joueur_5 = 0
                score_joueur_6 = 0
                score_joueur_7 = 0
                score_joueur_8 = 0
                score_joueur_9 = 0
                score_joueur_10 = 0

                score_joueur_tour = 0
                score_en_activite = score_0

                #importation des images
                table_daffichage_cartes = pygame.image.load('Images//table_daffichage_cartes.png')
                fond_de_chargement = pygame.image.load('Images//fond_chargement.jpg')
                fond_principal = pygame.image.load('Images//fond_principal.png')
                baniere_commencer_uno = pygame.image.load('Images//baniere_commencer_Uno.png')
                table_daffichage_tour_joueur = pygame.image.load('Images//table_daffichage_cartes.png')
                baniere_passez_joueur_suivant = pygame.image.load('Images//passage_joueur_suivant.png')
                table_score = pygame.image.load('Images//table_daffichage_cartes.png')


                fond_de_chargement = pygame.transform.scale(fond_de_chargement, (1263, 720))
                fond_principal = pygame.transform.scale(fond_principal, (1263,720))
                baniere_commencer_uno = pygame.transform.scale(baniere_commencer_uno, dimension_fenetre)
                table_daffichage_cartes = pygame.transform.scale(table_daffichage_cartes, (750,650))
                table_daffichage_tour_joueur = pygame.transform.scale(table_daffichage_tour_joueur,(500, 800))
                baniere_passez_joueur_suivant = pygame.transform.scale(baniere_passez_joueur_suivant,(333,83))
                table_score = pygame.transform.scale(table_score,(750,200))
