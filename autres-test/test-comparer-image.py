"""
    TEST COMPARER DES IMAGES


"""
import time
import cv2
import numpy as np
import pyautogui

"""
def detect_objects(image_path1, image_path2):
    # Charger les images
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    # Convertir les images en niveaux de gris
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Utiliser le détecteur de points clés ORB (Oriented FAST and Rotated BRIEF)
    orb = cv2.ORB_create()

    # Trouver les points clés et les descripteurs avec ORB
    keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)

    # Utiliser le matcher de BF (Brute-Force) avec la norme de Hamming
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors1, descriptors2)

    # Trier les correspondances en fonction de leur distance
    matches = sorted(matches, key=lambda x: x.distance)

    # Dessiner les correspondances sur une nouvelle image
    result_image = cv2.drawMatches(image1, keypoints1, image2, keypoints2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    # Afficher l'image résultante
    cv2.imshow("Matches", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Exemple d'utilisation
image_path_before = "screenshot_before.png"
image_path_after = "screenshot_after.png"

detect_objects(image_path_before, image_path_after)





window_title = "World of Warcraft"
screenWidth, screenHeight = pyautogui.size()
def focus_screen():
    try:
        window = pyautogui.getWindowsWithTitle(window_title)[0]
        window.activate()
        time.sleep(1)
    except IndexError:
        print(f"No Window find with this name: {window_title}")

focus_screen()
time.sleep(2)

im2 = pyautogui.screenshot('screenshot1.png')
time.sleep(1)
im2 = pyautogui.screenshot('screenshot2.png')

import cv2
import numpy as np
"""


"""
 #deuxieme tese

def detect_objects(image_path1, image_path2):
    # Charger les images
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    # Convertir les images en niveaux de gris
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Utiliser le détecteur de points clés ORB (Oriented FAST and Rotated BRIEF)
    orb = cv2.ORB_create()

    # Trouver les points clés et les descripteurs avec ORB
    keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)

    # Utiliser le matcher de BF (Brute-Force) avec la norme de Hamming
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors1, descriptors2)

    # Trier les correspondances en fonction de leur distance
    matches = sorted(matches, key=lambda x: x.distance)

    # Dessiner les correspondances sur une nouvelle image
    result_image = cv2.drawMatches(image1, keypoints1, image2, keypoints2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    # Afficher l'image résultante
    cv2.imshow("Matches", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Exemple d'utilisation
image_path_before = "screenshot1.png"
image_path_after = "screenshot2.png"

detect_objects(image_path_before, image_path_after)



"""


# load the input images
img1 = cv2.imread('screenshot1.png')
img2 = cv2.imread('screenshot2.png')

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
print("Coordinates of different pixels:", coordinates)

for coord in coordinates:
    #print("dessine : ", coord)
    cv2.circle(img2, tuple(coord[::-1]), 2, (0, 0, 255), -1)

cv2.imshow("difference", diff)
cv2.imshow("Image with Red Points", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()