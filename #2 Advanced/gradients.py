import cv2 as cv
import numpy as np

image = cv.imread("2.jpg")

cv.imshow("image", image)
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

#Laplacian edge detection method
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)

#Sobel 
#computes edges along axes x and y

sobelx = cv.Sobel(gray,cv.CV_64F,1,0) #x direction as 1 and y as 0
sobely = cv.Sobel(gray,cv.CV_64F,0,1) #y direction as 1 and x as 0
combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow("SOBEL X",sobelx)
cv.imshow("SOBEL Y",sobely)
cv.imshow("Combined sobel",combined_sobel)


#Canny edge detection
canny = cv.Canny(gray,125,175)
cv.imshow("Canny",canny)

cv.waitKey(0)