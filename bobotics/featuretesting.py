from pynput.keyboard import Controller
import pyautogui
import random
import time
import cv2
import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
keyboard = Controller()
import keyboard as keyboard2
import numpy as np

runtime = 0
prevtime = -6
dropping = False

prevtimeb = 0
bx = False
b = 0

pos = 0

state = 0
statesafe= False

targ = 1000
enc = 0
pwr = 0
error = 1000

Kp = 1.1
Ki = 0
Kd = 0

'''while True:
    enc += pwr

    error = targ-enc

    pwr = np.clip(error*Kp, a_max=1, a_min=0)

    error -= 10

    print(pwr)

    runtime +=1
    time.sleep(0.001)

    if keyboard2.is_pressed('b'):
        break'''

rutime = 0

while True:
    if keyboard2.is_pressed('b'):
        print('dropping')
        dropping = True
    if not keyboard2.is_pressed('b') and dropping:
        #if dropping:
        prevtime = runtime
        print('loading')
        dropping = False
    if runtime-prevtime == 5:
        print('loading done')
        break



    print(runtime)
    runtime +=1
    time.sleep(0.001)

while True:
    if keyboard2.is_pressed('a') and not bx:
        b += 1
        bx = True
    if not keyboard2.is_pressed('a'):
        bx = False

    if bx:
        if b%2==1:
            if pos > 0:
                pos -=1
            else:
                print
        else:
            if pos < 100:
                pos +=1
            else:
                print                

    print(pos)

    time.sleep(0.01)

    if keyboard2.is_pressed('b'):
        break

while True:
    if keyboard2.is_pressed('a') and not statesafe:
        state +=1
        statesafe = True

    if not keyboard2.is_pressed('a'):
        statesafe = False

    if not statesafe:
        if state == 0:
            print('close')
            print('close')
        elif state == 1:
            print('close')
            print('open')
        elif state == 2:
            print('open')
            print('open')
        elif state == 3:
            print('open')
            print('close')
        if state > 3:
            state = 0
    
    if keyboard2.is_pressed('b'):
        break
