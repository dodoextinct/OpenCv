import numpy as np
import cv2

#loading the image
image = cv2.imread('/images/digits.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #grayscalling
small = cv2.pyrDown(image) #downsampling the given image


#splitting the dataset into rows and columns
cells = [np.hsplit(row, 100) for row in np.vsplit(gray,50)]

#converting into numpy arrays
x = np.array(cells)

#separating the test set and train set from the array created
train = x[:,:70].reshape(-1,400).astype(np.float32)
test = x[:,70:100].reshape(-1,400).astype(np.float32)

#labeling the sets
k = [0,1,2,3,4,5,6,7,8,9]

train_labels = np.repeat(k,350)[:,np.newaxis]
test_labels = np.repeat(k,150)[:,np.newaxis]

#finding through K-nearest algorithm
knn = cv2.ml.KNearest_create()
knn.train(train,cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, distance = knn.findNearest(test, k = 3)

#finding the accuracy
matches = result == test_labels
correct = np.count_nonzero(matches)
accuracy = correct * (100.0 / result.size)

print(accuracy)
