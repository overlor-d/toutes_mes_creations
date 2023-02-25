##########_____importation des modules_____##########

import csv
import requests
import urllib.request
from PIL import Image
import sqlite3
from classes import *
from random import randint

conn=sqlite3.connect("Fichiers/movie_db.db")

########################_______________________________________############################

def prendre_nom_film():
    '''cette fonction permet de renvoyer une liste avec tous les noms des films qui sont dans le csv
    elle sera à remplacer par la suite avec le sql'''

    names = []
    with open("Fichiers/csv/movies.csv", newline='', encoding="utf-8") as csvfile:
        lignes = csv.reader(csvfile)
        next(lignes)
        for li in lignes:
            names.append(li[0])
    return names
###########################################################################################



########################_______________________________________############################

def prendre_url_image(movie_name):
    '''cette fonction permet de prendre l'url du poster en utilisant une api de film et ensuite de renvoyer
    cette url elle prends en argument le nom du film dont on souhaite l'img et si le film n'est pas trouvé l'img
    est remplacée par une img barrée'''

    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_name}"
    response = requests.get(url)
    data = response.json()
    try :
        poster_path = data['results'][0]['poster_path']
        poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
    except:
        poster_url = "https://thestovestore.ie/wp-content/uploads/2014/07/placehold.it-500x750.gif"

    return poster_url
###########################################################################################



########################_______________________________________############################

def tele_img(url, file_name):
    '''cette fonction permet de télécharger une image en fonction de son url et la sotcke dans le dossier
    indiqué en argument si le film n'est pas trouvé l'img est remplacée par une img barrée'''

    try :

        urllib.request.urlretrieve(url, file_name)
    except :
        urllib.request.urlretrieve("https://thestovestore.ie/wp-content/uploads/2014/07/placehold.it-500x750.gif", file_name)
###########################################################################################



########################_______________________________________############################

def affichage_image(nom_film):
    '''cette fonction permet de faire une recherche d'un film en fonction d'un bout de son nom et affiche le
    poster de ce film'''


    names = prendre_nom_film()
    dossier = "Images/poster_film"
    numero = []

    for k in range(len(names)):
        if nom_film in names[k]:
            numero.append(k)

    print("voici la liste avec tous les films contenant {0}".format(nom_film))
    for k in numero:
        print(names[k])
    if len(numero) == 1:
        nom_image = "movie_poster" + str(numero[0]) + ".jpg"
        chemin_image = dossier + "/" + nom_image
        image = Image.open(chemin_image)
        image.show()


    elif len(numero) != 0:
        r = int(input("poster du film que vous voulez voir parmi la liste "))
        while r != 8000:
            nom_image = "movie_poster" + str(numero[r]) + ".jpg"
            chemin_image = dossier + "/" + nom_image
            image = Image.open(chemin_image)
            image.show()
            r = int(input())
###########################################################################################

def Search_2(request):
    cursor=conn.cursor()
    if not isinstance(request, int):
        request="%"+request+"%"
    cursor.execute('SELECT * FROM Film WHERE nom LIKE ? OR genre LIKE ? OR company LIKE ? OR main LIKE ? OR directeur LIKE ? OR scenariste LIKE ? OR year LIKE ? OR pays LIKE ?',(request,request,request,request,request,request,request,request,))
    rows=cursor.fetchall()
    cursor.close()

    id = randint(0,len(rows))
    liste_film = rows[id -1]



    return liste_film


def Search(request,indice):
    if len(request) > 3:
        cursor=conn.cursor()
        if not isinstance(request, int):
            request="%"+request+"%"
        cursor.execute('SELECT * FROM Film WHERE nom LIKE ? OR genre LIKE ? OR company LIKE ? OR main LIKE ? OR directeur LIKE ? OR scenariste LIKE ? OR year LIKE ? OR pays LIKE ?',(request,request,request,request,request,request,request,request,))
        rows=cursor.fetchall()
        cursor.close()
        liste_film = []

        if len(rows) >= indice[1]:
            for k in range(indice[0], indice[1]):
                liste_film.append(rows[k])
        else :
            for k in range(indice[0], len(rows)):
                liste_film.append(rows[k])

        if liste_film !=[]:
            return liste_film,rows
        else :
            return False,False
    else:
        return False,False


def Login(user,mdp):
    cursor=conn.cursor()
    cursor.execute('SELECT motdepasse FROM Client WHERE pseudo=?',(user,))
    rows=cursor.fetchall()
    if rows==[]:
        return "0"
    elif rows[0][0]==mdp:
        return "1"
    else:
        return "2"


def Register(nom,prenom,mdp,pseudo):
    cursor=conn.cursor()
    cursor.execute('SELECT pseudo FROM Client WHERE pseudo=?',(pseudo,))
    rows=cursor.fetchall()
    if rows!=[]:
        return False
    else:
        cursor.execute('INSERT INTO Client(nom,prenom,motdepasse,pseudo) VALUES (?,?,?,?)',(nom,prenom,mdp,pseudo,))
        conn.commit()
        cursor.close()
        return True


def DeleteUser(pseudo):
    cursor=conn.cursor()
    cursor.execute('SELECT n_user FROM Client WHERE pseudo=?',(pseudo,))
    rows=cursor.fetchall()
    cursor.execute('DELETE FROM Client WHERE n_user=?',(rows[0][0],))
    conn.commit()
    cursor.close()
    print("Compte supprimé !")

def StatutFilm(pseudo,nfilm):
    cursor=conn.cursor()
    cursor.execute('SELECT n_user FROM Client WHERE pseudo=? ',(pseudo,))
    nuser=cursor.fetchall()[0][0]
    cursor.execute('SELECT statut FROM Filmographie WHERE n_user=? AND n_film=?',(nuser,nfilm,))
    rows=cursor.fetchall()
    
    if rows==[]:
        cursor.execute('INSERT INTO Filmographie VALUES (?,?,?)',(1,nfilm,0,))
        conn.commit()
        cursor.close()
        return "Statut modifié"
    if rows[0][0]==0:
        cursor.execute('UPDATE Filmographie SET statut=? WHERE n_user=? AND n_film=?',(1,nuser,nfilm,))
        conn.commit()
        cursor.close()
        return "Statut modifié"

def VoirStatut(pseudo,film):
    cursor=conn.cursor()
    cursor.execute('SELECT n_film FROM Film WHERE nom=?',(film,))
    nfilm=cursor.fetchall()[0][0]
    cursor.execute('SELECT n_user FROM Client WHERE pseudo=? ',(pseudo,))
    nuser=cursor.fetchall()[0][0]
    cursor.execute('SELECT statut FROM Filmographie WHERE n_user=? AND n_film=?',(nuser,nfilm,))
    rows=cursor.fetchall()[0][0]
    if rows==[]:
        attente=False
        vu=False
    if rows==0:
        attente=True
        vu=False
    if rows==1:
        attente=True
        vu=True
    return attente,vu

def AttenteFilm(pseudo):
    cursor=conn.cursor()
    cursor.execute('SELECT n_user FROM Client WHERE pseudo=? ',(pseudo,))
    nuser=cursor.fetchall()[0][0]
    cursor.execute('SELECT Film.* FROM Filmographie JOIN Film ON Filmographie.n_film=Film.n_film WHERE n_user=? AND statut=0',(nuser,))
    rows=cursor.fetchall()
    if rows!=[]:
        return rows
    return False

def VuFilm(pseudo, indice):
    liste_film = []
    cursor=conn.cursor()
    cursor.execute('SELECT n_user FROM Client WHERE pseudo=? ',(pseudo,))
    nuser=cursor.fetchall()[0][0]
    cursor.execute('SELECT Film.* FROM Filmographie JOIN Film ON Filmographie.n_film=Film.n_film WHERE n_user=? and statut=1',(nuser,))
    rows=cursor.fetchall()
    print(rows)
    if len(rows) >= indice[1]:
            for k in range(indice[0], indice[1]):
                liste_film.append(rows[k])
    else :
        for k in range(indice[0], len(rows)):
            liste_film.append(rows[k])

    if liste_film != []:
        return liste_film,rows
    else :
        return False,False

def affichage_images_rech(txt_recher, division_e, indice, scene_1_bis):
    liste = Search(txt_recher.txt,indice)
    liste_film_recher = liste[0]
    row = liste[1]
    liste_affichage = []
    liste_texte = []
    liste_image = []

    if liste_film_recher != False:
        if indice[0] == 0:
            if 10 in scene_1_bis:
                for k in range(len(scene_1_bis)):
                    if scene_1_bis[k] == 10:
                        scene_1_bis.pop(k)
                        break
        else:
            if 10 not in scene_1_bis:
                scene_1_bis.append(10)

        if indice[1] >= len(row):

            if 11 in scene_1_bis:
                for k in range(len(scene_1_bis)):
                    if scene_1_bis[k] == 11:
                        scene_1_bis.pop(k)
                        break
        else:
            if 11 not in scene_1_bis:
                scene_1_bis.append(11)

    else :
        if 10 in scene_1_bis:
            for k in range(len(scene_1_bis)):
                if scene_1_bis[k] == 11:
                    scene_1_bis.pop(k)
                    break

        if 11 in scene_1_bis:
            for k in range(len(scene_1_bis)):
                if scene_1_bis[k] == 11:
                    scene_1_bis.pop(k)
                    break

    if len(txt_recher.txt) > 3 and liste_film_recher != False:
        mu = 0
        multi = 0
        for k in range(len(liste_film_recher)):
            if mu <= 2000 and k % 4 !=  0:
                mu += 500
            else :
                mu = 100

            if k % 4 == 0 and k != 0:
                multi += 1

            liste_affichage.append(Txt(mu,250 + 450*multi,liste_film_recher[k][1],(255,255,255),division_e, 50))
            liste_texte.append(Txt(mu,250 + 450*multi,liste_film_recher[k][1],(255,255,255),division_e, 50))

            if liste_affichage[-1].surface.get_width() > 200 // division_e:
                while liste_affichage[-1].surface.get_width() > 200 // division_e:
                    liste_affichage[-1].suprimer()
                liste_affichage[-1].ajouter("...")

            img = Im([1], "poster_film/poster_film{0}.jpg".format(str(liste_film_recher[k][0]-1)) , [mu, 290 + 450*multi])
            img.resi()
            liste_affichage.append(img)
            liste_image.append(img)

    elif len(txt_recher.txt) <= 3 :
        liste_affichage.append( Txt(500,550,"La recherche est trop courte entrez au moins trois lettres",(255,255,255),division_e,50))

        if 10 in scene_1_bis:
            for k in range(len(scene_1_bis)):
                if scene_1_bis[k] == 11:
                    scene_1_bis.pop(k)
                    break

        if 11 in scene_1_bis:
            for k in range(len(scene_1_bis)):
                if scene_1_bis[k] == 11:
                    scene_1_bis.pop(k)
                    break

    else :
        liste_affichage.append( Txt(825,550,"Aucun résultats",(255,255,255),division_e,50))

        if 10 in scene_1_bis:
            for k in range(len(scene_1_bis)):
                if scene_1_bis[k] == 11:
                    scene_1_bis.pop(k)
                    break

        if 11 in scene_1_bis:
            for k in range(len(scene_1_bis)):
                if scene_1_bis[k] == 11:
                    scene_1_bis.pop(k)
                    break


    return liste_affichage, liste_film_recher, liste_image, scene_1_bis

def page_films(liste, indice, division_e):
    liste_recher = liste[1][indice]
    image = liste[2][indice]
    liste_affichage_poster = []
    rectangle = []
    titre = ["Nom :","Genre :","Année :","Producteur :","Scripter :","Acteur principal :","Compagnie :", "Pays :",""]

    rectangle.append(Rectangle(600, 850, (33,33,33),[0],[1000,200],"tot",50))
    image.reini_resi()
    image.x = rectangle[0].x + 50
    image.y = rectangle[0].y + 50

    rectangle.append(Rectangle(500, 500, (33,33,33),[0],[80,500],"tot",50))

    liste_affichage_poster.append(rectangle[0])
    liste_affichage_poster.append(rectangle[1])
    liste_affichage_poster.append(image)

    for k in range(1,len(liste_recher)):
        liste_affichage_poster.append(Txt(130,500 + 50*k, str(titre[k-1]) + " " + str(liste_recher[k]) ,(255,255,255),division_e,30))

        if liste_affichage_poster[-1].surface.get_width() > 400 // division_e:
            while liste_affichage_poster[-1].surface.get_width() > 400 // division_e:
                liste_affichage_poster[-1].suprimer()
            liste_affichage_poster[-1].ajouter("...")



    return liste_affichage_poster, rectangle

def page_principale(division_e, indice):
    style_horreur = Search_2("Horror")
    style_action = Search_2("Action")
    style_drama = Search_2("Drama")
    style_comedie = Search_2("Comedy")
    style_fantaisie = Search_2("Fantasy")
    style_aventure = Search_2("adventure")
    style_Famille = Search_2("Family")

    mu = 230
    multi = 0

    liste_style = [style_horreur,style_action,style_drama,style_comedie,style_fantaisie]
    nom_style = ["Horreur","Action","Drama","Comedy","Fantaisie","Aventure","Familiale"]

    liste_a = []
    liste_img = []

    for k in range(len(liste_style)):

        if k != 0:
            mu += 300

        liste_a.append(Txt(mu + 10,500, str(nom_style[k]),(255,255,255),division_e,70))
        img = Im([1], "poster_film/poster_film{0}.jpg".format(str(liste_style[k][0]-1)) , [mu, 550])

        img.resi()
        liste_img.append(img)
        liste_a.append(img)


    return liste_a, liste_style, liste_img

def affichage_films_vu(pseudo, division_e, indice, scene_7_bis) :
    
    if pseudo != "": 
        
        liste = VuFilm(pseudo,indice)
        print(liste)
        liste_film_recher = liste[0]
        row = liste[1]
        liste_affichage = []
        liste_texte = []
        liste_image = []

        if liste_film_recher != False:
            if indice[0] == 0:
                if 10 in scene_7_bis:
                    for k in range(len(scene_7_bis)):
                        if scene_7_bis[k] == 10:
                            scene_7_bis.pop(k)
                            break
            else:
                if 10 not in scene_7_bis:
                    scene_7_bis.append(10)

            if indice[1] >= len(row):

                if 11 in scene_7_bis:
                    for k in range(len(scene_7_bis)):
                        if scene_7_bis[k] == 11:
                            scene_7_bis.pop(k)
                            break
            else:
                if 11 not in scene_7_bis:
                    scene_7_bis.append(11)

        else :
            if 10 in scene_7_bis:
                for k in range(len(scene_7_bis)):
                    if scene_7_bis[k] == 11:
                        scene_7_bis.pop(k)
                        break

            if 11 in scene_7_bis:
                for k in range(len(scene_7_bis)):
                    if scene_7_bis[k] == 11:
                        scene_7_bis.pop(k)
                        break

        if liste_film_recher != False:
            mu = 0
            multi = 0
            for k in range(len(liste_film_recher)):
                if mu <= 2000 and k % 4 !=  0:
                    mu += 500
                else :
                    mu = 100

                if k % 4 == 0 and k != 0:
                    multi += 1

                liste_affichage.append(Txt(mu,250 + 450*multi,liste_film_recher[k][1],(255,255,255),division_e, 50))
                liste_texte.append(Txt(mu,250 + 450*multi,liste_film_recher[k][1],(255,255,255),division_e, 50))

                if liste_affichage[-1].surface.get_width() > 200 // division_e:
                    while liste_affichage[-1].surface.get_width() > 200 // division_e:
                        liste_affichage[-1].suprimer()
                    liste_affichage[-1].ajouter("...")

                img = Im([1], "poster_film/poster_film{0}.jpg".format(str(liste_film_recher[k][0]-1)) , [mu, 290 + 450*multi])
                img.resi()
                liste_affichage.append(img)
                liste_image.append(img)

        else :
            liste_affichage.append( Txt(825,550,"Aucun résultats",(255,255,255),division_e,50))

            if 10 in scene_7_bis:
                for k in range(len(scene_7_bis)):
                    if scene_7_bis[k] == 11:
                        scene_7_bis.pop(k)
                        break

            if 11 in scene_7_bis:
                for k in range(len(scene_7_bis)):
                    if scene_7_bis[k] == 11:
                        scene_7_bis.pop(k)
                        break

        return liste_affichage, liste_film_recher, liste_image, scene_7_bis

if __name__ == "__main__":
    '''
    while 1:
        affichage_image(str(input("entrez le nom de votre film: \n")).lower())
    '''

    #ces lignes ci dessous permettent de télécharger l'ensemble des données de l'applications
    r = input("voulez-vous télécharger tous les posters des films ? o/n")
    if r == "o":
        names = prendre_nom_film()
        api_key = '2a8ccc40158ddf7b708208040bc1af18'
        for k in range(6140, len(names)):
            poster_url = prendre_url_image(names[k])
            file_name = "Images/poster_film/poster_film" + str(k) + ".jpg"
            tele_img(poster_url, file_name)
