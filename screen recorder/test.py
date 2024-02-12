from calendar import different_locale
from pynput import keyboard
import pyautogui
import time
import cv2
import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# IMPORTING

extention = 0
exit_loop = False
fps = 30
seconds_long = input ('please put the amount of seconds you would like to record for\n')
seconds_long = int(seconds_long)
seconds_long *= 30

while seconds_long > 0:
    extention = str(extention)
    image = pyautogui.screenshot(region=[0, 0, 1920, 1080])
    image.save(r'C:\\Users\\' + os.getlogin() + '\\.vscode\\code files\\screen recorder\\images\\' + extention + '.png')

    print('C:\\Users\\' + os.getlogin() + '\\.vscode\\code files\\screen recorder\\images\\' + extention + '.png')

    extention = int(extention)
    extention += 1
    # reading the image for text



    seconds_long -= 1
    time.sleep(0.033333333333333333333333333333333333333333333333333333333333333333333333333333333333333)

extention = str(extention)

image_folder = (r'C:\\users\\' + os.getlogin() + '\\.vscode\\code files\\screen recorder\\images')
video_name = 'video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, fps, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()

