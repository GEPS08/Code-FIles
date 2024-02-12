from pynput.keyboard import Key, Controller
import pyautogui
import time
import os
import cv2
keyboard = Controller()

cv2.VideoCapture

time.sleep(5)
keyboard.press(Key.right)
keyboard.release(Key.right)
image = pyautogui.screenshot(region=(680, 345, 545, 480))
image.save(r'C:\\Users\\' + os.getlogin() + '\\.vscode\\code files\\snake\\textimage.png')
time.sleep(1.7)
keyboard.press(Key.up)
keyboard.release(Key.up)

time.sleep(0.9)
keyboard.press(Key.left)
keyboard.release(Key.left)

time.sleep(2.1)
keyboard.press(Key.down)
keyboard.release(Key.down)

time.sleep(1.9)
keyboard.press(Key.right)
keyboard.release(Key.right)
keyboard.press(Key.up)
keyboard.release(Key.up)

time.sleep(1.8)
keyboard.press(Key.right)
keyboard.release(Key.right)
keyboard.press(Key.down)
keyboard.release(Key.down)

time.sleep(1.8)
keyboard.press(Key.right)
keyboard.release(Key.right)
keyboard.press(Key.up)
keyboard.release(Key.up)
