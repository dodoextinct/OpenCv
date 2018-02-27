import cv2
import numpy as np

image = cv2.imread('/home/yashkrishan/Desktop/OpenCV MiniProjects/Res/waldo.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Where is waldo?', image)
cv2.waitKey(0)

template = cv2.imread('/home/yashkrishan/Desktop/OpenCV MiniProjects/Res/waldo_sample.jpg',0)

result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
min_value, max_value, min_loc, max_loc = cv2.minMaxLoc(result)

top_left = max_loc
bottom_right = (top_left[0] + 50, top_left[1] + 50)
cv2.rectangle(image, top_left, bottom_right, (0,0,255), 5)

cv2.imshow('Waldo!!', image)
cv2.waitKey(0)
cv2/destroyAllWindows()

