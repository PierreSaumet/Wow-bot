import pyautogui, sys
import time

window_title = "World of Warcraft"

def focus_screen():
    try:
        window = pyautogui.getWindowsWithTitle(window_title)[0]
        window.activate()
        time.sleep(1)
    except IndexError:
        print(f"No Window find with this name: {window_title}")

focus_screen()
im1 = pyautogui.screenshot('test.png')


def test_find_ennemi():
    try:
        jaune = pyautogui.locateOnScreen('./jaune2.png')
        print("oui faune, ", jaune)
        time.sleep(10)
        return True
    except pyautogui.ImageNotFoundException:
        print("pas de jaune")
        return False
if __name__ == '__main__':
    while True:
        test_find_ennemi()