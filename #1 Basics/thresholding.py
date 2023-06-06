#Thresholding is a technique in which if the pixel values are less than the threshold value then they are set to 0 and if they are above the threshold value they are set to 1. There are 2 kind of thresholding, simple and adaptive thresholding

import cv2 as cv

image = cv.imread("2.jpg")
cv.imshow("Original Image", image)

gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray)

#simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) #if the pixel is greater than 150 then set it to 255 otherwise set it to 0
cv.imshow("Simple thresholded image",thresh)

threshold, thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV) #inverse threshold
cv.imshow("Simple inverse thresholded image",thresh_inv)


################################################################
#Adaptive thresholding

#in simple thresholding we have to calculate the threshold value, but in the adaptive threshold method the computer itself sets an optimal threshold value

adaptive_threshold = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,9) 
#11 is the blocksize (kernel value) and 9 is the value of C
cv.imshow("Adaptive thresholded image",adaptive_threshold)

cv.waitKey(0)