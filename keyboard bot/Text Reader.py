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

imagetext = cv2.imread(r'C:\\Users\\' + os.getlogin() + '\\.vscode\\code files\\Keyboard Bot\\textimage.png')
Wordinput = pytesseract.image_to_string(imagetext)
Wordinput = Wordinput.replace ('\n', ' ')
print (Wordinput)
# reading the image for text