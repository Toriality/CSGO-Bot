import keyboard as kb
from pynput.keyboard import Key, Controller

keyboard = Controller()

def get_keyboard_kb(): return keyboard, kb
def get_keys(): return Key