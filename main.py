import sys

import myconfig

from test.record import start_record

def ft_quit():
    res = input("\n\nCtrl-c was pressed, Do you want to exit? y/n\n")
    if res == "y":
        sys.exit(0)

def main():
    """
    """

    while True:
        try:
            print(f"{myconfig.MEMU_MSG}")
            user_choice = input("Your choice: ")
            if user_choice == "0" or user_choice == "exit" or user_choice == "EXIT":
                sys.exit(0)
            elif user_choice == "1":
                start_record()
            elif user_choice == "2":
                pass
        except KeyboardInterrupt:
            ft_quit()


if __name__ == '__main__':
    main()
