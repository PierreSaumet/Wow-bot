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

def delete_item():
    print("Fonction delete item\n")
    # Position de l'item à enlever:
    x = 1771
    y = 897

    # Ouvre les sacs
    pyautogui.keyDown("b")
    pyautogui.keyUp("b")

    # Déplace le curseur vers l'item à supprimer
    pyautogui.moveTo(x, y, 1)
    time.sleep(1)

    # Drag l'ogjet à supprimer
    pyautogui.dragTo(1797, 1023, button='left')
    time.sleep(1)

    # Clique pour le supprimer
    pyautogui.click()

    # Accepte de le supprimer
    pyautogui.moveTo(875, 230, 0.5)
    pyautogui.click()
    
    time.sleep(2)
    # Ferme les sacs
    pyautogui.keyDown("esc")
    pyautogui.keyUp("esc")
    time.sleep(2)

def find_corpse():
    # Coordonnées
    x_left = 800
    x_right = 1100
    y = 450

    print("Dans la fonction find corpse\n")
    while y <= 600:
        x = x_left
        while x <= x_right:
            # Déplace la souris sur l'axe x
            pyautogui.moveTo(x, y)
            # Clique droit et réupère si le corps est présent
            pyautogui.click(button='right')
            x += 50
        # Déplace la souris sur l'axe y 
        y += 50

def find_ennemi():
    x_min = 675
    x_max = 1200
    x, y = 0, 250

    while y <= 600:
        x_min += 25
        x = x_min
        while x <= x_max:
            #print(f"x = {x}, y = {y}")
            pyautogui.moveTo(x, y)
            pyautogui.click(button="left")
            x += 25
        if x_max > 950:
            x_max -= 50
        y += 50



import time
import cv2
import numpy as np
import pyautogui

"""

"""



# load the input images
img1 = cv2.imread('middle_life.png')
img2 = cv2.imread('full_life.png')

# convert the images to grayscale
if img1 is None or img2 is None:
    print("Erreur: Impossible de charger l'une des images.")
    exit()
else:
    # Continuer avec le reste du code
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# define the function to compute MSE between two images
def mse(img1, img2):
    h, w = img1.shape
    diff = cv2.subtract(img1, img2)
    err = np.sum(diff**2)
    mse = err/(float(h*w))
    return mse, diff

error, diff = mse(img1, img2)
print("Image matching Error between the two images:",error)
# Trouver les coordonnées des pixels différents
coordinates = np.column_stack(np.where(diff != 0))
#print("Coordinates of different pixels:", coordinates)

for coord in coordinates:
    #print("dessine : ", coord)
    cv2.circle(img2, tuple(coord[::-1]), 2, (0, 0, 255), -1)

if error > 10:
    print("YESSS")
#cv2.imshow("difference", diff)
#cv2.imshow("Image with Red Points", img2)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

"""
if __name__ == '__main__':
    focus_screen()
    time.sleep(1)
    im = pyautogui.screenshot('low_life  .png', region=(120, 60, 135, 5))
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')


if __name__ == '__main__':
    focus_screen()
    time.sleep(1)
    #main()
    #find_corpse()
    find_ennemi()

    

    
try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')

    en haut
    y = 449d
    en haut a gauche
    x = 800
    en haut à droite
    x = 1100

    en bas =
    y 600
    
    part de en haut a gacuhe
    x = 800 y = 449
    x = 1100 y = 449

    x = 800 y = 600
    x = 1100 y = 600


    """

