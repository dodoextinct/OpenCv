import cv2
import numpy as np

def sketch(image):
    
    #Conversion into gray
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    #Cleaning the image by bluring
    blur_gray = cv2.GaussianBlur(gray, (5,5), 0)
    
    #Detecting the edges
    canny = cv2.Canny(blur_gray, 10, 70)
    
    #Invert binarize the image
    ret, mask = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY_INV)
    return mask

cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()
    cv2.imshow('Live Sketch', sketch(frame))
    
    if cv2.waitKey(1) == 13:
        break
        
cap.release()
cap.destroyAllWindows()
    
