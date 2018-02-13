import cv2
import numpy as np

images = cv2.imread('/home/yashkrishan/Desktop/abc.jpg')
cv2.imshow("images", images)
cv2.waitKey(0)
gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
 
edged = cv2.Canny(gray,30,200)

image2, contours, hirearchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for c in contours:
    approx = cv2.approxPolyDP(c, 0.01 * cv2.arcLength(c,True), True)
    
    if(len(approx) == 3):
        shape_name = "Triangle"
        cv2.drawContours(images, [c], 0, (0,255,0), -1)
        
        M = cv2.moments(c)
        if M["m00"] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
        else:
            cx, cy = 0,0
        cv2.putText(images, shape_name, (cx,cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)
    
    elif(len(approx) == 4):
        x,y,w,h = cv2.boundingRect(c)
        M = cv2.moments(c)
        if M["m00"] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
        else:
            cx, cy = 0,0
        
        if (abs(w-h)<=3):
            shape_name = "Square"
            cv2.drawContours(images, [c], 0, (0,255,0), -1)
            cv2.putText(images, shape_name, (cx,cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)
        else:
            shape_name = "Rectangle"
            cv2.drawContours(images, [c], 0, (0,255,0), -1)
            cv2.putText(images, shape_name, (cx,cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)
    elif(len(approx) == 5):
        shape_name = "Pentagon"
        cv2.drawContours(images, [c], 0, (0,255,0), -1)
        
        M = cv2.moments(c)
        if M["m00"] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
        else:
            cx, cy = 0,0
        cv2.putText(images, shape_name, (cx,cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)
        
    if(len(approx)>= 15):
        shape_name = "Circle"
        cv2.drawContours(images, [c], 0, (0,255,0), -1)
        
        M = cv2.moments(c)
        if M["m00"] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
        else:
            cx, cy = 0,0
        cv2.putText(images, shape_name, (cx,cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1)

cv2.imshow("Image", images)
cv2.waitKey()
