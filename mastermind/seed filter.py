from tokenize import blank_re
from pynput.mouse import Button, Controller
import pyautogui
import time
import cv2
from tkinter import Tk
import os
import pytesseract
from termcolor import colored
import keyboard
mouse = Controller()

def copy_clipboard():
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.01)
    return Tk().clipboard_get()

time.sleep(5)

print(mouse.position)

while True:
    mouse.position = (1089, 940)
    mouse.click(Button.left, 1)

    mouse.position = (732, 940)
    mouse.click(Button.left, 1)
    pyautogui.typewrite('1234')

    mouse.position = (909, 940)
    mouse.click(Button.left, 1)

    mouse.position = (909, 666)
    mouse.click(Button.left, 2)
    firstnum = int(copy_clipboard())

    mouse.position = (1089, 666)
    mouse.click(Button.left, 2)
    secondnum = int(copy_clipboard())

    seed = 0

    print(firstnum)
    if firstnum > 3:
        seed = 1
        print('firstnum is good')

    print(secondnum)
    if secondnum > 3:
        seed = 1
        print('secondnum is good')

    if not seed == 1:
        mouse.position = (1089, 940)
        mouse.click(Button.left, 1)

    if seed == 1:
        mouse.position = (732, 940)
        mouse.click(Button.left, 1)
        print('seed is good. please continue')
        break

    if firstnum + secondnum == 4:
        mouse.position = (732, 940)
        mouse.click(Button.left, 1)
        print('seed is good. please continue')
        break

    if keyboard.is_pressed('escape'):
        print('user canceled the process')
        break