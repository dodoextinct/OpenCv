import cv2
import numpy as np

#training cascade classifier
body_classifier = cv2.CascadeClassifier('/haarcascades/haarcascade_fullbody.xml')

#opening the webcam
cap= cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
	
    #resizing the frame
    frame = cv2.resize(frame, None, fx = 0.5, fy = 0.5, interpolation = INTER_LINEAR)

    #grayscaling
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detecting classifer
    bodies = body_classifier.detectMultiScale(gray, 1.2, 3)
    
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 255), 3)
        cv2.imshow('Detecting!!', frame)
    
    if cv2.waitKey(1) == 13:
        break
        
cap.release()
cap.destroyAllWindows()
