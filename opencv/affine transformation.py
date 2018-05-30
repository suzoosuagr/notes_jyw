import cv2
import numpy as np

img = cv2.imread('balckpussy.png', cv2.IMREAD_GRAYSCALE)

rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)

print(M)

M[:,-1] += np.array([(rows - cols)/2 , (cols - rows)/2]).T

#
img2 = cv2.warpAffine(img,M2,(cols,rows))
#
#
#
print(M)

print(img.shape)
print(img2.shape)

cv2.imshow('original', img)
cv2.imshow('affine', img2)
cv2.waitKey()



