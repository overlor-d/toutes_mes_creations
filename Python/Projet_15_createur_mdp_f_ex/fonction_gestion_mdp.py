from random import *


def fonction_gestion_mdp():
    '''
    cette fonction sert a creer un mdp et demande à l'utilisateur sil lui plait puis il enregistre avec le nom decide par lutilisateur
    '''


    fichier_mdp = open(r'../Fichiers/mdp.txt','a' )

    #creation des variables de boucle
    continuer = True
    satisfait = True

    #creation des listes permantant d'avoir le vocab pour les mdp 
    liste_lettres_majuscule = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    liste_lettres_minuscule = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    liste_chiffres = ['0','1','2','3','4','5','6','7','8','9']
    liste_caractere_speciaux = ['&','+','-','*','€']

    code = []
    code_final = ''

    while continuer :

        while satisfait :

            for i in range(3):
                caractere_actif = randint(0,len(liste_lettres_majuscule)-1)
                code.append(liste_lettres_majuscule[caractere_actif])
            for k in range(4):
                caractere_actif = randint(0,len(liste_lettres_minuscule)-1)
                code.append(liste_lettres_minuscule[caractere_actif])
            for x in range(4):
                caractere_actif = randint(0,len(liste_chiffres)-1)
                code.append(liste_chiffres[caractere_actif])
            for z in range(1):
                caractere_actif = randint(0,len(liste_caractere_speciaux)-1)
                code.append(liste_caractere_speciaux[caractere_actif])
            
            shuffle(code)
            for lettre in range(len(code)-1):
                code_final += code[lettre]

                
       
            fichier_mdp.write('\n' + input("nom utillite code:"))
            fichier_mdp.write('\n{0}'.format(code_final))
            fichier_mdp.write('\n'+ input('description code 250 caractère max'))

            
            continuer = False
            satisfait = False


    fichier_mdp.close()

fonction_gestion_mdp()