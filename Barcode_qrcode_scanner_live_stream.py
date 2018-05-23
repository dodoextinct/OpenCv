"""reading barcodes and qr codes from live stream"""

#importing libraries
from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import datetime
import time
import cv2
import argparse

#parsing arguments to take command line values
ap = argparse.ArgumentParser()

#output to a csv file all the informations scanned
ap.add_argument("-o", "--output", type = str, default="barcodes.csv", help = "path to output CSV file containing barcodes")
args = vars(ap.parse_args())

#indication of stram starting
print("[INFO] starting video stream ...")

#starting videostream through webcam
vs = VideoStream(src=0).start()

#waiting time for warming up the camera, this can be eliminated
time.sleep(2.0)

#opening the csv file
csv = open(args["output"], "w")

#to keep the file unique
found = set()

while True:
	
	#reading video stream
	frame = vs.read()

	#resizing the window
	frame = imutils.resize(frame, width = 700)
	
	#decoding the codes scanned
	codes = pyzbar.decode(frame)

	#iterating each code scanned
	for code in codes:

		#drawing a rectangle round the codes
		(x,y,w,h) = code.rect
		cv2.rectangle(frame, (x,y), (x+w, y+h), (255,255,0), 2)

		#decoding the contents into string
		codeData = code.data.decode("utf-8")

		#type of code
		codeType = code.type

		#putting into texts
		text = "{} ({})".format(codeData, codeType)
		cv2.putText(frame, text, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)

		#hecking if data found is unique or previously scanned
		if codeData not in found:
			
			#if not previously scanned then adding the data in csv
			csv.write("{}, {}\n".format(datetime.datetime.now(),codeData))
			csv.flush()
	
			#also adding into found set
			found.add(codeData)

	#showing the result
	cv2.imshow("Scanner", frame)
	key = cv2.waitKey(1) & 0xFF
	
	#quit if pressed q
	if key == ord("q"):
		break

#cleaning and closing
print("[INFO] cleaning...")
csv.close()
cv2.destroyAllWindows()
vs.stop()

