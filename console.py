import ctypes
from time import sleep
from pynput.keyboard import Key, Controller

keyboard = Controller()

async def write(str):
    """
    Writes on CSGO console.\n
    Arguments:
        str: string to write
    """
    ctypes.windll.user32.BlockInput(True)
    sleep(0.1)
    keyboard.tap("'")
    sleep(0.1)
    keyboard.press(Key.ctrl_l)
    sleep(0.1)
    keyboard.tap('a')
    sleep(0.1)
    keyboard.release(Key.ctrl_l)
    sleep(0.1)
    keyboard.tap(Key.backspace)
    sleep(0.1)
    keyboard.type(str)
    sleep(0.1)
    keyboard.tap(Key.enter)
    sleep(0.1)
    keyboard.tap(Key.esc)
    sleep(0.1)
    ctypes.windll.user32.BlockInput(False)

# TODO: function to get player IDs by typing stat