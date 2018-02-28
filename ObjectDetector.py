import cv2
import numpy as np

def shift_detector(new_image, image_template):
	#for template matching-
	image1 = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
	image2 = image_template
	
	#SHIFT detector object
	shift = cv2.xfeatures2d.SIFT_create()

	#gathering keypoints

	keypoints1, detectors1 = shift.detectAndCompute(image1, None)
	keypoints2, detectors2 = shift.detectAndCompute(image2, None)
	
	FLANN_INDEX_KDTREE = 0
	index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 3)
	search_params = dict(checks = 100)

	flann = cv2.FlannBasedMatcher(index_params, search_params)

	matches = flann.knnMatch(detectors1, detectors2, k=2)
	
	good_matches = []
	for m,n in matches:
		if m.distanc<0.7 * n.distance:
			good_matches.append(m)
	return len(good_matches)

cap = cv2.VideoCapture(0)

image_template = cv2.imread('/home/yashkrishan/Desktop/OpenCV MiniProjects/Res/Screenshot_20180122-194511.png',0)
while True:
	ret, frame = cap.read()

	try:
		height, width = frame.shape[:2]
	except AttributeError:
		print('Shape Not Found!!')
	top_left_x =(int)( width/3)
	top_left_y = (int)((height /2 ) + (height / 4))
	bottom_right_x = (int)((width/3)*2)
	bottom_right_y = (int)((height/2) - (height/4))

	cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), 255, 3)
    
	try:
		cropped = frame[bottom_right_y:top_left_y, top_left_x:bottom_right_x]
	except AttributeError:
		print('Shape Not Found!!')

	frame = cv2.flip(frame,1)
	
	matches = shift_detector(cropped, image_template)

	cv2.putText(frame, str(matches), (450,450), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0),1)

	threshold = 10
	
	if matches> threshold:
		cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255,0),3)
		cv2.putText(frame, 'Object Found', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0),2)
  
	cv2.imshow('Object Detctor by SIFT', frame)
	if cv2.waitKey(1) == 13:
		break

cap.release()
cv2.destroyAllWindows()
	

	
