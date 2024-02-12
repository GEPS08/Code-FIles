from tokenize import blank_re
from pynput.mouse import Button, Controller
import pyautogui
import time
import cv2
from tkinter import Tk
import os
import pytesseract
from termcolor import colored
mouse = Controller()

#copying highlighted email to clipboard
def copy_clipboard():
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.01)
    return Tk().clipboard_get()

image_res = [480, 420, 960, 130]
person = []
blacklist = []
personloop = 1

chat_pop = int(input('Please put the amount of people in the chat space\n(you can check the amount of people right under the name of the chat space)\n'))

blacklist_num = int(input('Please put the amount of people to blacklist\n'))

for i in range(0, blacklist_num):
    personloop = str(personloop)

    blacklist_inputs = input('Please put the email of person ' + personloop + ' in the blacklist\n')

    personloop = int(personloop)
    
    personloop += 1
    blacklist.append(blacklist_inputs)
      
print(blacklist)

time.sleep(1)

#going to desktop
mouse.position = (1919, 1079)
mouse.click(Button.left, 1)

time.sleep(0.1)

#opening chrome
mouse.position = (40, 150)
mouse.click(Button.left, 2)

#fullscreening chrome
time.sleep(1)
pyautogui.press('f11')

time.sleep(0.1)

#opening hangouts shortcut
mouse.position = (910, 385)

time.sleep(1)
mouse.click(Button.left, 1)

# add an open cv thing to recognise this image so it waits untill the page loads
# C:\Users\Joe\Downloads\{2277E4D7-3443-48E7-ACEC-8829EBA93990}.png
# replace this time.sleep with the open cv thing
time.sleep(3.5)

#opening the chatroom
mouse.position = (170, 615)
mouse.click(Button.left, 1)

time.sleep(1)

#opening the chatroom menu
mouse.position = (430, 100)
mouse.click(Button.left, 1)

time.sleep(1)

#veiwing the members of the chatroom
mouse.position = (440, 155)
mouse.click(Button.left, 1)

time.sleep(1.5)

#highlighting person1's email
mouse.position = (805, 444)
mouse.click(Button.left, 3)

clipboard = copy_clipboard()

clipboard = clipboard.replace ('\n', '')

if clipboard in blacklist:
    #selecting options for person1 in the persons list
    mouse.position = (1250, 435)
    time.sleep(0.1)
    mouse.click(Button.left, 1)

    time.sleep(0.2)

    #removing person1 from space
    mouse.position = (1150, 545)
    mouse.click(Button.left, 1)

    time.sleep(0.3)

#highlighting person2's email
time.sleep(0.1)
mouse.position = (805, 496)
mouse.click(Button.left, 3)

clipboard = copy_clipboard()

clipboard = clipboard.replace ('\n', '')

if clipboard in blacklist:
    #selecting options for person2 in the persons list
    mouse.position = (1250, 480)
    time.sleep(0.1)
    mouse.click(Button.left, 1)

    time.sleep(0.2)

    #removing person2 from space
    mouse.position = (1150, 590)
    mouse.click(Button.left, 1)

    time.sleep(0.3)

#highlighting person3's email
time.sleep(0.1)
mouse.position = (805, 548)
mouse.click(Button.left, 3)

clipboard = copy_clipboard()

clipboard = clipboard.replace ('\n', '')

if clipboard in blacklist:
    #selecting options for person3 in the persons list
    mouse.position = (1250, 545)
    time.sleep(0.1)
    mouse.click(Button.left, 1)

    time.sleep(0.2)

    #removing person3 from space
    mouse.position = (1150, 655)
    mouse.click(Button.left, 1)

    time.sleep(0.3)

#highlighting person4's email
time.sleep(0.1)
mouse.position = (805, 600)
mouse.click(Button.left, 3)

clipboard = copy_clipboard()

clipboard = clipboard.replace ('\n', '')

if clipboard in blacklist:
    #selecting options for person4 in the persons list
    mouse.position = (1250, 595)
    time.sleep(0.1)
    mouse.click(Button.left, 1)

    time.sleep(0.2)

    #removing person4 from space
    mouse.position = (1150, 700)
    mouse.click(Button.left, 1)

    time.sleep(0.3)

#highlighting person5's email
time.sleep(0.1)
mouse.position = (805, 652)
mouse.click(Button.left, 3)

clipboard = copy_clipboard()

clipboard = clipboard.replace ('\n', '')

if clipboard in blacklist:
    #selecting options for person5 in the persons list
    mouse.position = (1250, 645)
    time.sleep(0.1)
    mouse.click(Button.left, 1)

    time.sleep(0.2)

    #removing person5 from space
    mouse.position = (1150, 750)
    mouse.click(Button.left, 1)

    time.sleep(0.3)

#highlighting person6's email
time.sleep(0.1)
mouse.position = (805, 704)
mouse.click(Button.left, 3)

clipboard = copy_clipboard()

clipboard = clipboard.replace ('\n', '')

if clipboard in blacklist:
    #selecting options for person6 in the persons list
    mouse.position = (1250, 695)
    time.sleep(0.1)
    mouse.click(Button.left, 1)

    time.sleep(0.2)

    #removing person6 from space
    mouse.position = (1150, 785)
    mouse.click(Button.left, 1)

    time.sleep(0.3)

#highlighting person7's email
time.sleep(0.1)
mouse.position = (805, 756)
mouse.click(Button.left, 3)

clipboard = copy_clipboard()

clipboard = clipboard.replace ('\n', '')

if clipboard in blacklist:
    #selecting options for person7 in the persons list
    mouse.position = (1250, 745)
    time.sleep(0.1)
    mouse.click(Button.left, 1)

    time.sleep(0.2)

    #removing person7 from space
    mouse.position = (1150, 785)
    mouse.click(Button.left, 1)

    time.sleep(0.3)

#highlighting person8's email
time.sleep(0.1)
mouse.position = (805, 808)
mouse.click(Button.left, 3)

clipboard = copy_clipboard()

clipboard = clipboard.replace ('\n', '')

if clipboard in blacklist:
    #selecting options for person8 in the persons list
    mouse.position = (1250, 800)
    time.sleep(0.1)
    mouse.click(Button.left, 1)

    time.sleep(0.2)

    #removing person8 from space
    mouse.position = (1150, 785)
    mouse.click(Button.left, 1)

    time.sleep(0.3)


if chat_pop > 8:
    while chat_pop > 0:
        mouse.scroll(0,-0.53)
        mouse.click(Button.left, 3)

        clipboard = copy_clipboard()

        clipboard = clipboard.replace ('\n', '')

        if clipboard in blacklist:
            #selecting options for person8 in the persons list
            mouse.position = (1250, 800)
            time.sleep(0.1)
            mouse.click(Button.left, 1)

            time.sleep(0.2)

            #removing person8 from space
            mouse.position = (1150, 785)
            mouse.click(Button.left, 1)

            time.sleep(0.3)

        chat_pop -= 1

    #opening the chatroom menu
    mouse.position = (430, 100)
    mouse.click(Button.left, 1)
    time.sleep(0.05)
    mouse.click(Button.left, 1)

    time.sleep(1)

    #veiwing the members of the chatroom
    mouse.position = (440, 155)
    mouse.click(Button.left, 1)

    time.sleep(1.5)
    