import random

def generer_cle_chiffrement():
    # Générer une chaîne de 2000 chiffres aléatoires entre 0 et 9
    cle = "".join([str(random.randint(0, 9)) for i in range(100000)])
    
    # Enregistrer la clé dans un fichier
    with open("cle_chiffrage.txt", "w") as f:
        f.write(cle)
        
    return cle
