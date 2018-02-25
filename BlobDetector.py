import cv2
import numpy as np

image = cv2.imread("image_path", 0)
cv2.imshow("Images!!", image)
cv2.waitKey(0)

detector = cv2.SimpleBlobDetector_create()

keypoints = detector.detect(image)

blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

no_of_blobs = len(keypoints)
text = "Total Blobs:" + str(len(keypoints))
cv2.putText(blobs, text, (20,550), cv2.FONT_HERSHEY_COMPLEX,1, (100,0,255), 2)

cv2.imshow("Blobs", blobs)
cv2.waitKey(0)

params = cv2.SimpleBlobDetector_Params()

params.filterByArea = True
params.minArea = 100

params.filterByCircularity = True
params.minCircularity = 0.9

params.filterByConvexity = False
params.minConvexity = 0.2

params.filterByInertia = True
params.minInertiaRatio = 0.01

detector = cv2.SimpleBlobDetector_create(params)

keypoint = detector.detect(image)

blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

no_of_blobs = len(keypoints)
text = "Total Blobs:" + str(len(keypoints))
cv2.putText(blobs, text, (20,550), cv2.FONT_HERSHEY_COMPLEX,1, (100,0,255), 2)
