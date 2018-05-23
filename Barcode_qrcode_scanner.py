"""reads barcode and qrcode from images and outputs information in contained in them"""

from pyzbar import pyzbar
import argparse
import cv2

#argument parsing to take arguments from commandline
ap = argparse.ArgumentParser()

#adding argument method to take what type of inputs
ap.add_argument("-i", "--image", required = True, help = "path to input image")

#parsing the arguments
args = vars(ap.parse_args())

#reading the image through imread parsed from command line
image = cv2.imread(args["image"])

#decoding the contents through pyzar module's decode method
codes = pyzbar.decode(image)

#scanning every barcodes or qr code
for code in codes:
	
	#getting the dimmensions of the coded images
	(x,y,w,h) = code.rect

	#drawing rectangles
	cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 2)
	
	#converting decoded datas into strings
	codeData = code.data.decode("utf-8")

	#checking the code type barcode or qrcode
	codeType = code.type

	#displaying the contents
	text = "{} ({})".format(barcodeData, barcodeType)

	#adding the text above the images
	cv2.putText(image, text, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)

	#printing the information in the terminal
	print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))

#showing the image
cv2.imshow("Image", image)

#waitkey enabled to close the image
cv2.waitKey(0)
