import time

from pynput import mouse, keyboard


def key_press(key: any) -> dict:
    """
        This fuction is called when a key is pressed
    """
    try:
        key_str = key.char
    except AttributeError:
        key_str = str(key)

    print("ici key = ", key_str)
    if key_str == "!":
        print("BINGO")
        
        exit()

    tmp_dict = {}
    tmp_dict[key_str] = time.time()


    print("Dans key_presse , = ", tmp_dict, type(tmp_dict), len(tmp_dict))
    return tmp_dict


def key_release(key: any, my_dict: dict) -> list:
    """
    """
    try:
        key_str = key.char
    except AttributeError:
        key_str = str(key)
    
    mylist = []
    if key_str in my_dict:
        start_time = my_dict[key_str]
        duration = time.time() - start_time
        mylist.append({"key": key_str, "duration": round(duration, 2)})
    
    print(mylist)

    return mylist
        
def main():
    print("GO:")
    keyboard_listener = keyboard.Listener(on_press=key_press, on_release=key_release)

    keyboard_listener.start()
    time.sleep(60)

if __name__ == '__main__':

    main()