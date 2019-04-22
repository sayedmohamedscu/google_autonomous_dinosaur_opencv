
import pyautogui
import time
from PIL import ImageGrab
import numpy as np
import cv2
time.sleep(6)
#screenWidth, screenHeight = pyautogui.size()
#print(screenWidth, screenHeight)
while(True):
    img = ImageGrab.grab(bbox=(480,150,1000,250)) #bbox specifies specific region (bbox= x,y,width,height)
    
    img_np = np.array(img)
    
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    retval,frame = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY_INV)
    #frame=frame+255
    
    if np.sum(frame)>8000000:
        retval,frame = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY_INV)
        
    
    im=frame[50:,40:80]
    
    q=np.sum(im)
    if q>20000:
        print("high")
        #pyautogui.press('left')
        pyautogui.hotkey('space')
    #cv2.imshow("test", frame)
    #cv2.imshow("test2", im)
    
    #time.sleep(0.1)
    cv2.waitKey(0)
#cv2.destroyAllWindows()
