import os
import json
import time

import pyautogui

from myconfig import PLAYING_DESCRIPTION_MSG, CHOOSE_RECORD_MSG, LOADING_MSG

screenWidth, screenHeight = pyautogui.size()
window_title = "World of Warcraft"
all_files = {}

def focus_screen():
    try:
        window = pyautogui.getWindowsWithTitle(window_title)[0]
        window.activate()
        time.sleep(1)
    except IndexError:
        print(f"No Window find with this name: {window_title}")

def open_json(name_file):
    file = open(name_file)
    data = json.load(file)
    file.close()

    return data

def keyboard(key, timing):
    print(f"Pressing: {key} for {timing} sec")

    pyautogui.keyDown(key)
    if timing is not None:
        time.sleep(timing)
    pyautogui.keyUp(key)

def mouse(click, timing, x, y):
    print(f"Clicking with: {click} at x={x}/y={y} for {timing} sec")
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown(button=click)
    if timing is not None:
        time.sleep(timing)
    pyautogui.mouseUp(button=click)


def find_record():
    folder_name = "./record/"

    print(f"\n{CHOOSE_RECORD_MSG}")
    for file in os.listdir(folder_name):
        if os.path.isfile(folder_name + file) and file.startswith("record_") and file.endswith(".json"):
            data = open_json(folder_name + file)
            print(f"Record number: \t{file[7: len(file) - 5]}\nDescription:\t{data[0]['description']}\n")
            all_files[file[7: len(file) - 5]] = folder_name + file

def check_key():
    while True:
        user_input = input("your record: ")
        if user_input in all_files:
            return user_input
        else:         
            print("Sorry, choose another number.\n")


def start_play():
    find_record()

    name = check_key()
    data = open_json(all_files[name])

    print(f"{LOADING_MSG}")
    time.sleep(2)
    print(f"{PLAYING_DESCRIPTION_MSG} {data[0]['description']}\n")
    focus_screen()
    for elem in data:
        for key, value in elem.items():
            if key == "Mouse":
                mouse( value["action"],  value["total"],  value["pos_x"],  value["pos_y"])
            elif key == "description":
                pass
            else:
                if isinstance(value, dict) and 'total' in value:
                    keyboard(key, value['total'])
