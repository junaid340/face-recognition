# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 13:17:37 2020

@author: junaid
"""

import cv2
import os

cascPath =  'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

cap = cv2.VideoCapture(0)
cap.set(3, 640) #Set Width
cap.set(4, 480) #Set Height

face_id = input('\n Enter Name for the person and Press Enter ==> ')
print("\n [INFO] Initializing face capture. Look the camera while moving your head left to right very slowly and wait it will take a while...")

os.makedirs('dataset', exist_ok = True)
pth = 'dataset/'+face_id+'/'
#Initialize individual Sampleing Face Count
count = 0
while (True):
  ret, img = cap.read()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
  faces = faceCascade.detectMultiScale(
          gray, scaleFactor = 1.1,
          minNeighbors = 7, minSize = (30, 30))
  
  for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    count += 1
    
    #Save the captured face into the dataset directory
    cv2.imwrite(pth + face_id + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
    cv2.imshow('image', img)
  
  k = cv2.waitKey(30) & 0xff
  if k == 27: #Press 'ESC' to quit
    break
  elif count >= 500: #Take 50 face samples and stop the video
    break

print("\n [INFO] Exiting the Program!")  
cap.release()
cv2.destroyAllWindows()