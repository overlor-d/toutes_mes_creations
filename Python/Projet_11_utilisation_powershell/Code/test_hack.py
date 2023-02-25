import keyboard
from time import sleep


keyboard.press_and_release('cmd + r')
sleep(1)
keyboard.write('powershell')
sleep(0.2)
keyboard.press_and_release('enter')
sleep(1)

keyboard.write('cd E:')
sleep(0.2)
keyboard.press_and_release('enter')
sleep(1)

keyboard.write('cd D:')
sleep(0.2)
keyboard.press_and_release('enter')
sleep(1)

keyboard.write('cd programmes_hack')
sleep(0.2)
keyboard.press_and_release('enter')
sleep(1)

keyboard.write('Main')
sleep(0.2)
keyboard.press_and_release('tab')
sleep(1)
keyboard.press_and_release('enter')
sleep(1)

keyboard.write('exit')
sleep(0.2)
keyboard.press_and_release('enter')
sleep(1)
