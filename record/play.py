import json
import time

import pyautogui


screenWidth, screenHeight = pyautogui.size()
window_title = "World of Warcraft"

def focus_screen():
    try:
        window = pyautogui.getWindowsWithTitle(window_title)[0]
        window.activate()
        time.sleep(1)
    except IndexError:
        print(f"No Window find with this name: {window_title}")

# def find_file

def open_json():
    file = open('./record_1.json')
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


def main():
    data = open_json()
    time.sleep(5)
    print("GO\n")

    for elem in data:
        for key, value in elem.items():
            if key == "Mouse":
                mouse( value["action"],  value["total"],  value["pos_x"],  value["pos_y"])
            elif key == "description":
                pass
            else:
                if isinstance(value, dict) and 'total' in value:
                    keyboard(key, value['total'])

if __name__ == '__main__':
    main()
