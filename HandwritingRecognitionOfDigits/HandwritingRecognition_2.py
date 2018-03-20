import numpy as np
import cv2

#function to make squares around the digits
def makeSquare(not_square):
	BLACK = [0,0,0]
	img_dim = not_square.shape
	height = img_dim[0]
	width = img_dim[1]
	
	if(height == width):
		square = not_square
		return square
	else:
		doublesize = cv2.resize(not_square,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
		height = height * 2
		width = width * 2
		
		if(height>width):
			pad = (height - width)// 2
			doublesize_square = cv2.copyMakeBorder(doublesize,0,0,pad,pad,cv2.BORDER_CONSTANT,value = BLACK)

		else:
			pad = (width- height)//2
			doublesize_square = cv2.copyMakeBorder(doublesize,0,0,pad,pad,cv2.BORDER_CONSTANT,value = BLACK)

	doublesize_square_dim = doublesize_square.shape

	return doublesize_square

#function to resize the pexels size
def resize_to_pixel(dimmensions, image):
	
	buffer_pix = 4
	dimmensions = dimmensions - buffer_pix
	squared = image
	r = float(dimmensions)/squared.shape[1]
	dim = (dimmensions, int(squared.shape[0] * r))
	resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
	img_dim2 = resized.shape
	height_r = img_dim2[0]
	width_r = img_dim2[1]
	BLACK = [0,0,0]
	
	if(height_r>width_r):
		resized  = cv2.copyMakeBorder(resized,0,0,0,1,cv2.BORDER_CONSTANT, value=BLACK)
	if(height_r<width_r):
		resized = cv2.copyMakeBorder(resized,1,0,0,0,cv2.BORDER_CONSTANT,value = BLACK)
	p = 2
	ReSizedImg = cv2.copyMakeBorder(resized,p,p,p,p,cv2.BORDER_CONSTANT, value = BLACK)
	img_dim = ReSizedImg.shape
	height = img_dim[0]
	width = img_dim[1]

	return ReSizedImg
