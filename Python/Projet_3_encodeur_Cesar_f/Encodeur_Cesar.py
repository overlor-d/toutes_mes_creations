from generateur_cle_aleatoire import *

def encodage_fichier(chemin_f, cle):
    # Obtenir le texte
    with open(chemin_f, "r", encoding="utf-8") as f:
        donnees = f.read()

    cara_accent = {'à': 'a', 'â': 'a', 'ç': 'c', 'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'î': 'i', 'ï': 'i', 'ô': 'o', 'ö': 'o', 'ù': 'u', 'û': 'u', 'ü': 'u'}

    donnees_encod = ""
    for k in donnees:
        if k.isalpha():
            if k in cara_accent:
                k = cara_accent[k]
            if k.isupper():
                k_p = chr((ord(k) + cle - 65) % 26 + 65)
            else:
                k_p = chr((ord(k) + cle - 97) % 26 + 97)
        elif k == ".":
            k_p = "."
        else:
            k_p = k
        donnees_encod += k_p

    # Écrire dans un nouveau fichier les données
    chemin_f_encod = chemin_f
    with open(chemin_f_encod, "w", encoding="utf-8") as f:
        f.write(donnees_encod)

def decodage_fichier(file_path, cle):
    # Ouvrir le fichier à décoder
    with open(file_path, "r", encoding="utf-8") as f:
        donnees = f.read()

    cara_accent = {'à': 'a', 'â': 'a', 'ç': 'c', 'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'î': 'i', 'ï': 'i', 'ô': 'o', 'ö': 'o', 'ù': 'u', 'û': 'u', 'ü': 'u'}

    # Décoder le texte
    donnees_decod = ""
    for k in donnees:
        if k.isalpha():
            if k in cara_accent:
                k_p = cara_accent[k]
            if k.isupper():
                k_p = chr((ord(k) - cle - 65) % 26 + 65)
            else:
                k_p = chr((ord(k) - cle - 97) % 26 + 97)
        elif k == ".":
            k_p = "."
        else:
            k_p = k
        donnees_decod += k_p

    # Écrire dans un nouveau fichier les données
    decoded_file_path = file_path
    with open(decoded_file_path, "w", encoding="utf-8") as f:
        f.write(donnees_decod)


if __name__ == "__main__":

    # Exemple d'utilisation
    file_path = "test/test.txt"

    with open("cle_chiffrage.txt", "r", encoding="utf-8") as f:
            cle = f.read()


    if input("encoder ou decoder ?") == "encoder":
        cle = generer_cle_chiffrement()
        encodage_fichier(file_path, int(cle))
    else :
        with open("cle_chiffrage.txt", "r", encoding="utf-8") as f:
            cle = f.read()
        decodage_fichier(file_path, int(cle))
