from pynput.mouse import Button, Controller
import pyautogui
import time
import os
from tkinter import Tk
mouse = Controller()

time.sleep(5)

time.sleep(1)

#opening the chatroom menu
#veiwing the members of the chatroom
mouse.position = (440, 155, 1)
mouse.smooth_move(Button.left, 1)