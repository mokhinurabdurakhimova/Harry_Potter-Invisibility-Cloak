#libaries which we will use install them using terminal or Python interpreter
import time
import numpy as np
import cv2
import time

captureDevice = cv2.VideoCapture(0) #captureDevice = camera
#I used my computer's camera so in brackets 0. If you will use webcam instade of it use number 1
time.sleep(3)
#at this time when you will run a code camera will automaticly take a photo in 3 minutes
background = 0
for i in range(30):
    ret,background= captureDevice.read()
background = np.flip(background, axis=1)

while True:
    ret, img = captureDevice.read()
    img = np.flip(img, axis=1)
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    blur=cv2.GaussianBlur(hsv, (35,35),0)

    lower=np.array([0,120,70])
    upper=np.array([10,255,255])
    mask01=cv2.inRange(hsv,lower,upper)
#RGB. Use red clothes or cloak everthing you want but use red thing because here I wrote that if color will be red program should show background
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask02 = cv2.inRange(hsv, lower_red, upper_red)

    mask=mask01+mask02

    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN, np.ones((5,5),np.uint8))

    img[np.where(mask==255)] = background[np.where(mask==255)]
    cv2.imshow('my frame', img)
    cv2.imshow('background', background)
    cv2.imshow("mask01", mask01)
    k=cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captureDevice.release()
cv2.destroyAllWindows()
