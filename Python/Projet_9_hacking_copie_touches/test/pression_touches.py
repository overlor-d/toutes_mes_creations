from pynput import keyboard

def touche_pressee(key):
    try:
        print(key.char)

    except AttributeError:
        print(key)
        if key == keyboard.Key.esc:
            return False


with keyboard.Listener(on_press=touche_pressee) as listener:
    listener.join()

