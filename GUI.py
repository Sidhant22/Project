from tkinter import *
import os
from datetime import datetime;

root=Tk()

root.configure(background="white")

def function1():
    
    os.system("Final_Code.py")
    
def function2():
    
    os.system("detection_pedestrian.py")

def function3():
    
    os.system("detection_car_1.py")


def function4():
    
    os.system("FACE.py")
   
def function6():

    root.destroy()



root.title("Drone Based Recognisation System")


Label(root, text="Drone Based Recognisation System",font=("times new roman",20),fg="black",bg="#3BFF02",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="ALL RECOGNIZATION",font=("times new roman",20),bg="#02FFF4",fg='black',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

Button(root,text="PEOPLE RECOGNIZATION",font=("times new roman",20),bg="#02FFF4",fg='black',command=function2).grid(row=5,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

Button(root,text="FACE RECOGNIZATION",font=("times new roman",20),bg="#02FFF4",fg='black',command=function4).grid(row=7,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

Button(root,text="Exit",font=('times new roman',20),bg="#3BFF02",fg="black",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

root.mainloop()
