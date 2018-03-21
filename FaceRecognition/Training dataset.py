import numpy as np
import cv2
from os import listdir
from os.path import isfile, join

dataPath = '/Res/face_me/'
onlyfiles = [f for f in listdir(dataPath) if isfile(join(dataPath, f))]

Training_Data, Labels = [], []

for i, files in enumerate(onlyfiles):
	image_path = dataPath + onlyfiles[i]
	images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
	Training_Data.append(np.asarray(images, dtype = np.uint8))
	Labels.append(i)

Labels = np.asarray(Labels, dtype = np.int32)
model = cv2.face.LBPHFaceRecognizer_create()

model.train(np.asarray(Training_Data), np.asarray(Labels))
print("MOdel trained!!")
