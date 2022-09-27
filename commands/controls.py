from time import sleep
from pynput.keyboard import Key, Controller
import keyboard as kb
import mouse
import console
import ctypes

keyboard = Controller()

def drop(): keyboard.tap('g')

def knife(): keyboard.tap('3')

def click(): mouse.click()

async def stop():
    await console.write("say Pausa para beber agua...")
    ctypes.windll.user32.BlockInput(True)
    sleep(6)
    ctypes.windll.user32.BlockInput(False)
    await console.write("say Voltei :)")

async def duck():
    keyboard.press(Key.ctrl)
    kb.block_key('ctrl')
    sleep(6)
    kb.unblock_key('ctrl')
    keyboard.release(Key.ctrl)

async def invert():
    mapping = { 'w':'s', 'a':'d', 's':'w', 'd':'a' }
    await console.write("m_pitch -0.022;say Teclas e mouse invertidos!")
    for k, v in mapping.items():
        kb.remap_key(k,v)
    sleep(10)
    for k, v in mapping.items():
        kb.unremap_key(k)
    await console.write("m_pitch 0.022;say Teclado e mouse voltaram ao normal :)")