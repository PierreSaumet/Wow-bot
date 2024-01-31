import time
import pyautogui


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

moi = (0,0, 300, 120)
ennemi = (300, 0, 300, 120)


def test_find_ennemi():
    try:
        puma = pyautogui.locateOnScreen('./test2.png')
        print("oui")
        return True
    except pyautogui.ImageNotFoundException:
        print("pas de puma")
        return False

def too_far():
    try:
        far = pyautogui.locateOnScreen('./too_far.png')
        print("troploing")
        return True
    except pyautogui.ImageNotFoundException:
        print("")
        return False

def test_attack():
    print("GOOO")

    pyautogui.keyDown("a")
    pyautogui.keyUp("a")
    if too_far():
        pyautogui.keyDown("z")
        time.sleep(3)
        pyautogui.keyDown("space")
        pyautogui.keyUp("space")
        pyautogui.keyUp("z")
    
    time.sleep(1)
    pyautogui.keyDown("e")
    pyautogui.keyUp("e")

    time.sleep(1)
    pyautogui.keyDown("r")
    pyautogui.keyUp("r")

    time.sleep(2)
    pyautogui.keyDown("r")
    pyautogui.keyUp("r")

def move_find():
    pyautogui.keyDown("z")
    pyautogui.keyDown("e")
    time.sleep(1)
    pyautogui.keyUp("e")
    pyautogui.keyDown("space")
    pyautogui.keyUp("space")
    pyautogui.keyUp("z")

    pyautogui.keyDown("tab")
    time.sleep(3)
    pyautogui.keyUp("tab")



def main():
    while True:
        if test_find_ennemi():
            time.sleep(1)
            test_attack()
        else:
            move_find()
            time.sleep(1)


import pyautogui, sys
if __name__ == '__main__':
    #main()
    focus_screen()
    print('Press Ctrl-C to quit.')
    time.sleep(5)
    im1 = pyautogui.screenshot('test.png')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')