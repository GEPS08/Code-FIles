from pynput.mouse import Button, Controller
import pyautogui
import time
import os
mouse = Controller()

time.sleep(10)

loop = 50

while loop > 0:
    #selecting options for the video in the list
    mouse.position = (1860, 207)
    time.sleep(0.1)
    mouse.click(Button.left, 1)

    time.sleep(0.2)

    #deleting the video in the list
    mouse.position = (1760, 380)
    time.sleep(0.1)
    mouse.click(Button.left, 1)
    
    time.sleep(0.2)

    loop -= 1