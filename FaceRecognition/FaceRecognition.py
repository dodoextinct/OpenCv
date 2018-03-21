import cv2
import numpy as np
import FaceRecognition_2

face_classifier = cv2.CascadeClassifier('/haarcascades/haarcascade_frontalface_default.xml')

def face_detector(img, size = 0.5):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_classifier.detectMultiScale(gray, 1.3, 5)

	if faces is ():
		return img, []

	for (x,y,w,h) in faces:
		cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,255), 2)
		roi = img[y:y+h, x:x+w]
		roi = cv2.resize(roi, (200,200))
	return img, roi

cap = cv2.VideoCapture(0)

while True:
	
	ret, frame = cap.read()
	image, face = face_detector(frame)

	try:
		face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

		results = FaceRecognition_2.model.predict(face)

		if results[1] < 500:
			confidence = int(100 * (1 - (results[1])/300))
			display = '{0}% Confidence it is user'.format(str(confidence))

		cv2.putText(image, display, (100,120), cv2.FONT_HERSHEY_COMPLEX, 1, (160, 160, 150), 2)

		if confidence > 75:
			cv2.putText(image, "Unlocked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
			cv2.imshow('Face Cropper', image)
		else:
			
			cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
			cv2.imshow('Face Cropper', image)

	except:
		cv2.putText(image, "No Face Found", (250, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
		cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
		cv2.imshow('Face Cropper', image)
		pass

	
	if cv2.waitKey(1) == 13:
		break

cap.release()
cv2.destroyAllWindows()
