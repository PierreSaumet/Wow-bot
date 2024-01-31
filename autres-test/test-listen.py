from pynput import mouse, keyboard
import time
import json
import threading

full_list = []

# Dictionnaires pour stocker les horodatages de début et de fin de chaque action
keyboard_start_times = {}
mouse_start_times = {}

# Fonction appelée lorsqu'une touche du clavier est pressée
def on_press(key):
    print("fonctionpresse")
    try:
        key_str = key.char
    except AttributeError:
        key_str = str(key)

    if key_str not in keyboard_start_times:
        keyboard_start_times[key_str] = time.time()
        

# Fonction appelée lorsqu'une touche du clavier est relâchée
def on_release(key):
    print("fonciotn releads")

    try:
        key_str = key.char
    except AttributeError:
        key_str = str(key)
    print("ka? = ", key_str)
    if key_str in keyboard_start_times:
        print("ici?")
        start_time = keyboard_start_times[key_str]
        me = time.time()
        duration = me - start_time
        print(f"{duration} car fin = {me} et début = {start_time}")
        print(f"Key: {key_str}, Duration: {duration:.2f} seconds")
        full_list.append({"key": key_str, "duration": duration})

# Fonction appelée lorsqu'un bouton de la souris est pressé
def on_click(x, y, button, pressed):
    action = f"Left Click" if button == mouse.Button.left else f"Right Click"
    
    if pressed:
        mouse_start_times[action] = time.time()
    else:
        if action in mouse_start_times:
            start_time = mouse_start_times[action]
            duration = time.time() - start_time
            print(f"Mouse Action: {action}, Duration: {duration:.3f} seconds")
            full_list.append({"Mouse Action": action, "duration": round(duration)})


# Configurer les écouteurs pour le clavier et la souris
keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
mouse_listener = mouse.Listener(on_click=on_click)

# Démarrer les écouteurs
keyboard_listener.start()
mouse_listener.start()

# Enregistrement des actions pendant 1 minute
time.sleep(30)

# Arrêter les écouteurs
keyboard_listener.stop()
mouse_listener.stop()

print("FULL LIST event = ", full_list)

