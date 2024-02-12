import cv2
import numpy as np
import time,os

cap = cv2.VideoCapture(0)

while (1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    dark = np.array([180, 40, 40])
    light = np.array([256, 100, 100])

    dark[0] = dark[0]/2
    dark[1] = dark[1]*2.55
    dark[2] = dark[2]*2.55

    light[0] = light[0]/2
    light[1] = light[1]*2.55
    light[2] = light[2]*2.55

    print (dark, light)

    mask = cv2.inRange(hsv, dark, light)

    result = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('Mask', mask)

    cv2.imshow('frame', frame)

    cv2.imshow('Result', result)

    cv2.waitKey(1)

cv2.destroyAllWindows()
cap.release()