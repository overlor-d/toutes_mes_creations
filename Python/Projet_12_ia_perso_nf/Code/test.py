import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def condi_mdp(text):
    if text == "arrêt":
        reponse = "mot de passe"
        speak(reponse)
        res = listen_and_respond()
        print(res)
        if res == "1 5 6 0":
            return False
        else : return True

def conditions(text):
    if condi_mdp(text):
        return False


    
    elif text == "bonjour":
        reponse = "Bonjour"

    elif text == "comment vas-tu" :
        reponse = "je vais bien merci et vous"

    elif text == "je vais bien merci":
        reponse = "super je suis heureuse de le savoir."

    elif text == "qu'est-ce que tu sais faire" :
        reponse = "pour l'instant je suis en auto apprentissage. Je fais au mieux pour apprendre le plus vite possible et pour ensuite répondre à vos demande."

    else :
        reponse = "je ne sais pas quoi répondre je suis désolé"
        speak(reponse)
        reponse = "qu'est ce que je dois dire lorsque vous me dites :" + text

    speak(reponse)
    return True

def listen_and_respond():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="fr-FR")
        print(text)
        return text
    except sr.UnknownValueError:
        return "Je n'ai pas compris ce que vous avez dit. Pouvez-vous répéter?"

def speak(text):
    engine.say(text)
    engine.runAndWait()

marche = True

while marche:
    res = listen_and_respond()
    res = conditions(res)
    if res == False:
        marche = False
