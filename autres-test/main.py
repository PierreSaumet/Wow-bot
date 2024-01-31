import time

import pyautogui
from pynput import mouse, keyboard  #a voir



welcolme_msg = f"Hello, What do you want to do?"
choice_1 = f"Choice 1: Record a path."
choice_2 = f"Choice 2: Play a path."
choice_3 = f"To quit: 0\n"

help_user = f"You can only choose: 1 - to record a path. 2 - to play a path and 0 to exit.\n"

byebye_msg = f"Thank you Byebye."

def display_main_message() -> None:
    print(welcolme_msg, choice_1, choice_2, choice_3, sep="\n")

def check_choice(user_choice: int) -> int:
    if user_choice == 0:
        ft_byebye()
    elif user_choice == 1:
        return 1
    elif user_choice == 2:
        return 2
    else:
        print(help_user)
    return 0

def ft_byebye() -> None:
    print(f"{byebye_msg}")
    exit(0)

def record_path(void) -> int:
    """
        Return 0 if no error, otherwise return 1
        
    """


def main() -> None:
    """
        cette fonction affiche ce qui se passe et ce que le user veut faire

    """
    while True:
        display_main_message()
        try:
            user = int(input("Your choice: "))
        except ValueError as error:
            print(f"Error: {error}")
            print(byebye_msg)

        check_choice(user)
        print(f"Your choice: {user}\n")



if __name__ == '__main__':
    main()