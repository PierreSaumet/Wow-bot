
import time
import cv2
import numpy as np
import pyautogui

def focus_screen():
    try:
        window = pyautogui.getWindowsWithTitle(window_title)[0]
        window.activate()
        time.sleep(1)
    except IndexError:
        print(f"No Window find with this name: {window_title}")

def count_down():
    for t in reversed(range(5)):
        print(t)
        time.sleep(1)

def take_screenshot(name):
    print(f"Picture: {name}")
    im2 = pyautogui.screenshot(f'{name}.png')

def main():
    live = 1
    focus_screen()
    while live:
        picture1 = input("name picture 1: ")
        picture2 = input("name picture 2: ")
        count_down()
        take_screenshot(picture1)
        count_down()
        take_screenshot(picture2)


if __name__ == "__main__":
    
    window_title = "World of Warcraft"
    screenWidth, screenHeight = pyautogui.size()
    main()