from pynput import keyboard

def touche_pressee(key):
    print(key)
    if key == keyboard.Key.esc:
        return True


with keyboard.Listener(on_press=touche_pressee) as listener:
    listener.join()
    