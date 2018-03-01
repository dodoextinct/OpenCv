import cv2
import numpy as np

#loading haar cascade classifiers
face_cascade = cv2.CascadeClassifier('/home/yashkrishan/anaconda3/pkgs/opencv3-3.1.0-py36_0/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/yashkrishan/anaconda3/pkgs/opencv3-3.1.0-py36_0/share/OpenCV/haarcascades/haarcascade_eye.xml')

#defining the function for face detection
def face_detector(img, size = 0.5):
    
    #converting into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #detecting faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    #if image dosen't have a face display image only
    if faces is ():
        return img
    
    #detecting eyes in faces
    for (x,y,w,h) in faces:
        
        #slicing the window according to the face
        x = x - 50
        y = y - 50
        w = w + 50
        h = h + 50
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        #detecting the eyes
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
    roi_color = cv2.flip(roi_color, 1)
    return roi_color

#opening the webcam
cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    
    #calling the function
    cv2.imshow('Detecting faces since forever!!',face_detector(frame))
    
    #closing when pressed enter
    if cv2.waitKey(1) == 13:
        break


cap.release()
cv2.destroyAllWindows()
