'''
Haar Cascade Face detection with OpenCV  
    Based on tutorial by pythonprogramming.net
    Visit original post: https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/  
Adapted by Marcelo Rovai - MJRoBot.org @ 7Feb2018 
'''
import win32gui
import win32con
from os import getpid, system
from threading import Timer
import time
import numpy as np
import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
timer=0

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        
        scaleFactor=1.2,
        minNeighbors=5
        ,     
        minSize=(20, 20)
    )


    
    
    
    #print(type(faces))

    if(len(faces)==0):
        timer+=1
        print (timer)

    if(len(faces)>0):
        timer=0



    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        

        
       
        #print(len(faces))
        #if lenfaces:
        #    print(56)
        #print(x)
        #if faces==0:
         #   start = time.time()
          #  if start==5:
           #     print ("its been 5 seconds")
        
       

        
    cv2.imshow('video',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
    if timer==40:               #CHANGE THIS TO CHANGE TIME AWAY FROM SCREEN 
        

    
        def force_exit():
            pid = getpid()
            system('taskkill /pid %s /f' % pid)
            
        t = Timer(1, force_exit)
        t.start()
        SC_MONITORPOWER = 0xF170
        win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, SC_MONITORPOWER, 2)
        t.cancel()

cap.release()
cv2.destroyAllWindows()
