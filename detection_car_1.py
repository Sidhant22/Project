

import cv2
print('Project Topic : Vehicle Classification')


cascade_src = 'cars.xml'

video_src = 'video.avi'

cap = cv2.VideoCapture(video_src)

car_cascade = cv2.CascadeClassifier(cascade_src)


while True:
    ret, img = cap.read()
   
    if (type(img) == type(None)):
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)


    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),1)

    
    cv2.imshow('video', img)
   
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
