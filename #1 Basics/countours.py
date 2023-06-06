import cv2 as cv
import numpy as np

image = cv.imread("2.jpg")
cv.imshow("Cat",image)


blank = np.zeros(image.shape,dtype='uint8')
cv.imshow("Blank",blank)

#make it gray scale
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#blurring the image with Gaussian blur
blur = cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)

#get the edges with canny
canny = cv.Canny(blur,125,175)
cv.imshow("Canny",canny)

#find countours
contours,hierarchy = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE) # RETR_LIST means that we need all the countours
print(f'{len(contours)} contours detected!')


#NOTE: we can also use the threshold method to draw contours
ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY) #this means that all the contours whose value is less than 125 are 0 and the rest are 1
cv.imshow("Thresh",thresh)

#drawing the contours
cv.drawContours(blank,blank,-1,(0,255,0),1)
cv.imshow("Contours",blank)

cv.waitKey(0)
