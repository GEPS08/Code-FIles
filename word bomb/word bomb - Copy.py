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

imagetext = cv2.imread(r'C:\\Users\\' + os.getlogin() + '\\.vscode\\code files\\word bomb\\textimage1.png')
cv2.imshow('Original',imagetext)
#imagetext = cv2.cvtColor(imagetext, cv2.COLOR_BGR2GRAY)

#cv2.imshow('Grayscale', imagetext)
af = cv2.addWeighted(imagetext, 5, imagetext, 0, 80)

cv2.imshow('asdf', af)

rgb = cv2.cvtColor(af, cv2.COLOR_HLS2RGB)
gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
_, af = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('img_to_binary',af)

letters = pytesseract.image_to_string(af)

'''
print(pytesseract.image_to_boxes(af))
poses = (pytesseract.image_to_boxes(af)).split(' ')
poses = (pytesseract.image_to_boxes(af)).split('\n')

poses.pop(-1)

for i in range(len(poses)):
    poses[i] = poses[i].split(' ')
    
for i in range(len(poses)):
    print (poses[i])

    x = int(poses[i][1])
    y = int(poses[i][2])

    w = int(poses[i][3])
    h = int(poses[i][4])

    image = cv2.rectangle(af, (x, 120-y), (x + 120-w, 120-y + 120-h), (36,255,12), 1)







    for ii in range(len(poses[i])):
        print(poses[i][ii])
        
cv2.imshow('adsfsadf', image)'''
    
cv2.waitKey(0)

print(f'letters: {letters}')

#print(pytesseract.image_to_data(af))