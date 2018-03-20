import numpy as np
import cv2
import HandwritingRecognition_2, HandwritingRecognition_1


#reading the image
image = cv2.imread('/images/numbers.jpg')
#grayscaling
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#blurring
blurred = cv2.GaussianBlur(gray, (5,5), 0)

#getting canny edges to clear noise
edged = cv2.Canny(blurred, 30, 150)

#finding contours
_, contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)



full_number = []

#checking for all contours
for c in contours:

	(x,y,w,h) = cv2.boundingRect(c)

	if w >= 5 and h >= 25:
		roi = blurred[y:y + h, x:x + w]
		ret, roi = cv2.threshold(roi, 127,255, cv2.THRESH_BINARY_INV)
		squared = HandwritingRecognition_2.makeSquare(roi)
		final = HandwritingRecognition_2.resize_to_pixel(20, squared)
		cv2.imshow("final", final)
		final_array = final.reshape((1,400))
		final_array = final_array.astype(np.float32)
		ret, result, neighbours, dist = HandwritingRecognition_1.knn.findNearest(final_array, k = 1)
		number = str(int(float(result[0])))
		
		cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
		cv2.putText(image, number, (x,y + 155), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0),2)
		cv2.imshow("image",image)
		cv2.waitKey(0)

cv2.destroyAllWindows()
print("The no. is:" + ''.join(full_number))

