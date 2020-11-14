import cv2
import os
import os.path
import sys
import tkinter as tk
from tkinter.filedialog import askopenfilename
import shutil
import os
import sys
from PIL import Image, ImageTk


print('Project Topic : Recognisation')

dirPath = "testpicture"
fileList = os.listdir(dirPath)
for fileName in fileList:
    
    os.remove(dirPath + "/" + fileName)

fileName = askopenfilename(initialdir='C:\\Users\\admin\\Desktop\\DRONEDETEON', title='Select image for analysis ',
                           filetypes=[('image files', '')])
dst = "C:/Users/admin/OneDrive/Desktop/DRONEDETEON/testpicture"
shutil.copy(fileName, dst)

video_src = (fileName)

cap = cv2.VideoCapture(video_src)

bike_cascade = cv2.CascadeClassifier('two_wheeler.xml')

people_cascade = cv2.CascadeClassifier('pedestrian.xml')

car_cascade = cv2.CascadeClassifier('cars.xml')

while True:
    ret, img = cap.read()
    
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    bikes = bike_cascade.detectMultiScale(gray,1.01, 1)
    people = people_cascade.detectMultiScale(gray,1.3,2)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in bikes:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,215),2)
        
    for(a,b,c,d) in people:
        cv2.rectangle(img,(a,b),(a+c,b+d),(0,255,210),4)

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),1)
        
    cv2.imshow('video', img)
    
    if cv2.waitKey(1) == 13:
        break

cv2.destroyAllWindows()
