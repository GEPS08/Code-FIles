from pynput.mouse import Button, Controller
import pyautogui
import time
import os
mouse = Controller()

loop = int(input('Please put the amount of people in the chat space\n(you can check the amount of people right under the name of the chat space)\n'))

#going to desktop
mouse.position = (1919, 1079, 1)
mouse.click(Button.left, 1)

time.sleep(0.1)

#opening chrome
mouse.position = (40, 150, 1)
mouse.click(Button.left, 2)

#fullscreening chrome
time.sleep(1)
pyautogui.press('f11')

time.sleep(0.1)

#opening hangouts shortcut
mouse.position = (910, 385, 1)

time.sleep(1)
mouse.click(Button.left, 1)

# add an open cv thing to recognise this image so it waits untill the page loads
# C:\Users\Joe\Downloads\{2277E4D7-3443-48E7-ACEC-8829EBA93990}.png
# replace this time.sleep with the open cv thing
time.sleep(3.5)

#opening the chatroom
mouse.position = (170, 615, 1)
mouse.click(Button.left, 1)

time.sleep(1)

#opening the chatroom menu
mouse.position = (430, 100, 1)
mouse.click(Button.left, 1)

time.sleep(1)

#veiwing the members of the chatroom
mouse.position = (440, 155, 1)
mouse.click(Button.left, 1)

time.sleep(1.5)


while loop > 0:
    #selecting options for person1 in the persons list
    mouse.position = (1250, 435, 1)
    time.sleep(0.1)
    mouse.click(Button.left, 1)

    time.sleep(0.2)

    #removing person1 from space
    mouse.position = (1150, 545, 1)
    mouse.click(Button.left, 1)

    time.sleep(0.5)

    #selecting options for person2 in the perons list
    mouse.position = (1250, 480, 1)
    time.sleep(0.1)
    mouse.click(Button.left, 1)

    time.sleep(0.2)

    #removing person2 from space
    mouse.position = (1150, 590, 1)
    mouse.click(Button.left, 1)

    time.sleep(0.5)

    #selecting options for person3 in the perons list
    mouse.position = (1250, 545, 1)
    time.sleep(0.1)
    mouse.click(Button.left, 1)

    time.sleep(0.2)

    #removing person3 from space
    mouse.position = (1150, 655, 1)
    mouse.click(Button.left, 1)

    time.sleep(0.5)
    
    loop -= 1