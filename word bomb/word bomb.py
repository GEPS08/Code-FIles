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

image_res = [630, 635, 360, 100]

with open(r"C:\Users\Joe\.vscode\code files\word bomb\english.txt", "r") as file:
    textfile = file.read()
    words = list(map(str, textfile.split()))

print (words)

while True:
# waiting to get out of coding window

    if keyboard2.is_pressed('b'):
        break

    image = pyautogui.screenshot(region=(image_res))
    image.save(r'C:\\Users\\' + os.getlogin() + '\\.vscode\\code files\\word bomb\\textimage.png')
    # taking the image

    imagetext = cv2.imread(r'C:\\Users\\' + os.getlogin() + '\\.vscode\\code files\\word bomb\\textimage.png')
    letters = pytesseract.image_to_string(imagetext)
    # reading the image for text
    print (f'before ar: {letters}')
    letters = 'AR'.lower()
    for word in range(len(words)):
        if letters in words[word]:
            for splitting in words[word]:
                #keyboard.type(splitting)
                time.sleep(random.uniform(0.1, 0.01))
            #pyautogui.press('enter')
            words.pop(word)
            print(words[word])
            break

    # typing the image text

random.choice