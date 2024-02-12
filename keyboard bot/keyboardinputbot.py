from calendar import different_locale
from pynput.keyboard import Controller
import pyautogui
import time
import cv2
import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
keyboard = Controller()
# IMPORTING

loop = 4
image_res = [480, 420, 960, 130]

time.sleep(3)

while loop > 0:
# waiting to get out of coding window

    image = pyautogui.screenshot(region=(image_res))
    image.save(r'C:\\Users\\' + os.getlogin() + '\\.vscode\\code files\\Keyboard Bot\\textimage.png')
    # taking the image

    imagetext = cv2.imread(r'C:\\Users\\' + os.getlogin() + '\\.vscode\\code files\\Keyboard Bot\\textimage.png')
    Wordinput = pytesseract.image_to_string(imagetext)
    Wordinput = Wordinput.replace ('\n', ' ')
    # reading the image for text

    print(Wordinput)
    for Letter in Wordinput:
        keyboard.type(Letter)
        time.sleep(0.01)
    # typing the image text

    image_res = [480, 463, 960, 86]

    loop -= 1