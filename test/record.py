""" 
    tester pour enregisterer la sourois
"""
import os
import json
import time
from pynput import mouse, keyboard

mouse_start_times = {}
keyboard_cmd = {}

all_commands = []


def get_next_val():
    tmp_lst = []
    for f in os.listdir('.'):
        if os.path.isfile(f) and f.startswith("record_") and f.endswith(".json"):          
            tmp_lst.append(int(f[7: len(f) - 5]))

    if len(tmp_lst) == 0:
        return "0"
    return str(max(tmp_lst) + 1)

def save_record_to_json():
    json_data = json.dumps(all_commands, indent=2)

    with open("record_" + get_next_val() + ".json", "w") as json_file:
        json_file.write(json_data)

def record_mouse(x, y, button, pressed):
    action = f"Left Click" if button == mouse.Button.left else f"Right Click"

    if pressed:
        mouse_start_times[action] = time.time()
    else:
        if action in mouse_start_times:
            duration = time.time() - mouse_start_times[action]
            # print(f"Mouse Action: {action}, Duration: {duration:.3f} seconds,  Position X: {x}, Position Y: {y}")
            all_commands.append({"Mouse Action": action, "Duration": round(duration, 2), "pos_x": x, "pos_y": y})

def key_press(key):
    try:
        key_str = key.char
    except AttributeError:
        key_str = str(key)

    if key_str not in keyboard_cmd:
        keyboard_cmd[key_str] = {"start": time.time(), "end": None, "total": None}

def key_release(key):
    try:
        key_str = key.char
    except AttributeError:
        key_str = str(key)
    
    if key_str in keyboard_cmd:
        keyboard_cmd[key_str]['end'] = time.time()
        
        total = round(keyboard_cmd[key_str]['end'] - keyboard_cmd[key_str]["start"], 2)
        keyboard_cmd[key_str]["total"] = total

        all_commands.append(keyboard_cmd.copy())
        keyboard_cmd.clear()

def start_record():
    description = input("Write a small description and press enter to start: ")
    all_commands.append({"description": description} 
                                               )
    mouse_listener = mouse.Listener(on_click=record_mouse)
    keyboard_listener = keyboard.Listener(on_press=key_press, on_release=key_release)

    print("To stop recording press ctrl-c\n")
    try:
        mouse_listener.start()
        keyboard_listener.start()
        mouse_listener.join()
        keyboard_listener.join()
    except KeyboardInterrupt:
        print("\nRecording interrupted by user (Ctrl-C).")
        mouse_listener.stop()
        keyboard_listener.stop()

if __name__ == '__main__':
    start_record()
    save_record_to_json()