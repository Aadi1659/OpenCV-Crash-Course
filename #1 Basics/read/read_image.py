import cv2 as cv

img = cv.imread("1.jpg")
img = cv.resize(img,(800,600))

cv.imshow("Parking" , img)


cv.waitKey(0) #The function waitKey waits for a key event infinitely or for delay milliseconds, when it is positive.