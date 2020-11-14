import cv2
import numpy as np
import time
import sys
from PIL import Image , ImageTk;
import xlwt 
from xlwt import Workbook
from datetime import datetime, date
import datetime
import tkinter as tk
from tkinter import Message ,Text
import os
import shutil
import csv
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
wb = Workbook()
date_format = xlwt.XFStyle()
date_format.num_format_str = 'D/M/YYYY'
date_format_time = xlwt.XFStyle()
date_format_time.num_format_str = 'h:mm'
style = xlwt.easyxf('font: bold 1, color red;')
style2 = xlwt.easyxf('font: bold 1, color green;')
style3 = xlwt.easyxf('font: bold 1, color black;')
def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
recognizer = cv2.face.LBPHFaceRecognizer_create()
assure_path_exists("trainer/")
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX
cam = cv2.VideoCapture(0)
sheet1 = wb.add_sheet('Sheet 1', cell_overwrite_ok=True)
sheet1.write(0, 0,'DATE',style3)
sheet1.write(0, 1,'TIME',style3)
sheet1.write(0, 2,'NAME',style3)
sheet1.write(0, 3,'STATUS',style2)
col_names =  ['Id','Name','Date','Time']
count=0
counta=0
countb=0
countc=0
countd=0
counte=0
countf=0
countg=0
counth=0
counti=0
countj=0
countk=0
countl=0
countm=0
countn=0
counto=0
countp=0
countq=0
countr=0
counts=0
countt=0
countu=0
countv=0
counter1=0
counter2=0
counter3=0
counter4=0
counter5=0
counter6=0

while True:
    ret, image_frame =cam.read()
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(image_frame, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)
        Id,confidence =recognizer.predict(gray[y:y+h,x:x+w])
        if(confidence > 50):
         if(Id == 1):
             counta=counta+1
             print(counta)
             if(counta > 20 or ((countb or countc or countd or counte or countf or countg or counth or counti or countj or countk or countl or countm or countn or counto or countp or countq or countr or counts or countt or countu or countv))):
                 print("Greater COUNT")
                 if(counter1==0):
                     print("SIDHANT")
                     Id = "SIDHANT"
                     sheet1.write(1, 0,datetime.datetime.now(),date_format );
                     sheet1.write(1, 1, datetime.datetime.now(),date_format_time);
                     sheet1.write(1, 2, 'SIDHANT',style);
                     sheet1.write(1, 3, 'PRESENT',style2)
                     print("SIDHANT=present")
                     count=0
                     counta=0
                     countb=0
                     countc=0
                     countd=0
                     counte=0
                     countf=0
                     countg=0
                     counth=0
                     counti=0
                     countj=0
                     countk=0
                     countl=0
                     countm=0
                     countn=0
                     counto=0
                     countp=0
                     countq=0
                     countr=0
                     counts=0
                     countt=0
                     countu=0
                     countv=0
                     counter1=1
                     
            

        
         elif(Id==2):
             countb=countb+1
             if(countb> 20 or (counta or countc or countd or counte or countf or countg or counth or counti or countj or countk or countl or countm or countn or counto or countp or countq or countr or counts or countt or countu or countv)):
                 if(counter2==0):
                     
                     Id = "UNKNOWN PERSON"
                     sheet1.write(2, 0,datetime.datetime.now(),date_format );
                     sheet1.write(2, 1, datetime.datetime.now(),date_format_time);
                     sheet1.write(2, 2, 'UNKNOWN PERSON',style);
                     sheet1.write(2, 3, 'PRESENT',style2)
                     print("UNKNOWN PERSON=present")
                     count=0
                     counta=0
                     countb=0
                     countc=0
                     countd=0
                     counte=0
                     countf=0
                     countg=0
                     counth=0
                     counti=0
                     countj=0
                     countk=0
                     countl=0
                     countm=0
                     countn=0
                     counto=0
                     countp=0
                     countq=0
                     countr=0
                     counts=0
                     countt=0
                     countu=0
                     countv=0
                     counter2=1

       
         elif(Id==3):
             countc=countc+1
             if(countc> 20 or (countb or countj or countd or counta or counte or countg or counth or countf or counti or countk or countl or countm or countn or counto or countp or countq or countr or counts or countt or countu or countv)):
                 if(counter3==0):
                     Id = "UNKNOWN PERSON"
                     sheet1.write(10, 0,datetime.datetime.now(),date_format );
                     sheet1.write(10, 1, datetime.datetime.now(),date_format_time);
                     sheet1.write(10, 2, 'UNKNOWN PERSON',style);
                     sheet1.write(10, 3, 'PRESENT',style2)
                     print("UNKNOWN PERSON=present")
                     count=0
                     counta=0
                     countb=0
                     countc=0
                     countd=0
                     counte=0
                     countf=0
                     countg=0
                     counth=0
                     counti=0
                     countj=0
                     countk=0
                     countl=0
                     countm=0
                     countn=0
                     counto=0
                     countp=0
                     countq=0
                     countr=0
                     counts=0
                     countt=0
                     countu=0
                     countv=0
                     counter3=1
                     
         elif(Id==4):
             countd=countd+1
             if(countd> 20 or (countb or countc or countj or counta or counte or countg or counth or countf or counti or countk or countl or countm or countn or counto or countp or countq or countr or counts or countt or countu or countv)):
                 if(counter4==0):
                     Id = "UNKNOWN PERSON"
                     sheet1.write(10, 0,datetime.datetime.now(),date_format );
                     sheet1.write(10, 1, datetime.datetime.now(),date_format_time);
                     sheet1.write(10, 2, 'UNKNOWN PERSON',style);
                     sheet1.write(10, 3, 'PRESENT',style2)
                     print("UNKNOWN PERSON=present")
                     count=0
                     counta=0
                     countb=0
                     countc=0
                     countd=0
                     counte=0
                     countf=0
                     countg=0
                     counth=0
                     counti=0
                     countj=0
                     countk=0
                     countl=0
                     countm=0
                     countn=0
                     counto=0
                     countp=0
                     countq=0
                     countr=0
                     counts=0
                     countt=0
                     countu=0
                     countv=0
                     counter4=1
         
         elif(Id==5):
             countj=countj+1
             if(countj> 20 or (countb or countc or countd or counta or counte or countg or counth or countf or counti or countk or countl or countm or countn or counto or countp or countq or countr or counts or countt or countu or countv)):
                 if(counter5==0):
                     Id = "UNKNOWN PERSON"
                     sheet1.write(10, 0,datetime.datetime.now(),date_format );
                     sheet1.write(10, 1, datetime.datetime.now(),date_format_time);
                     sheet1.write(10, 2, 'UNKNOWN PERSON',style);
                     sheet1.write(10, 3, 'PRESENT',style2)
                     print("UNKNOWN PERSON=present")
                     count=0
                     counta=0
                     countb=0
                     countc=0
                     countd=0
                     counte=0
                     countf=0
                     countg=0
                     counth=0
                     counti=0
                     countj=0
                     countk=0
                     countl=0
                     countm=0
                     countn=0
                     counto=0
                     countp=0
                     countq=0
                     countr=0
                     counts=0
                     countt=0
                     countu=0
                     countv=0
                     counter5=1
        else:
            
            Id= "UNKNOWN PERSON"
        cv2.rectangle(image_frame, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(image_frame, str(Id), (x,y-40), font, 1, (255,255,255), 3)

    cv2.imshow('image_frame',image_frame)
    wb.save("Status2020.csv")

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cam.release()
cv2.destroyAllWindows()
