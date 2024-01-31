import time
import pyautogui

screenWidth, screenHeight = pyautogui.size()

print("screen = ", screenWidth)
def focus_on_window(window_title):
    try:
        # Trouver la fenêtre par le titre
        window = pyautogui.getWindowsWithTitle(window_title)[0]
        print("window ) ", window)
        # Activer la fenêtre
        window.activate()

        # Attendre un bref instant pour que la fenêtre soit activée
        time.sleep(0.5)
        print("fin de fenetre")
    except IndexError:
        print(f"La fenêtre avec le titre '{window_title}' n'a pas été trouvée.")



def test(key):
    print("GOOO")

    pyautogui.keyDown(key)
    pyautogui.keyUp(key)

def main():
    window_title = "World of Warcraft"  # Remplacez par le titre de votre fenêtre cible
    while True:
        print("TEST")
        print("pos = ", pyautogui.position())
        focus_on_window(window_title)
        time.sleep(1)
        test('z')

if __name__ == '__main__':
    main()

