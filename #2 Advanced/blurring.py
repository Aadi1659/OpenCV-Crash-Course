import cv2 as cv

image = cv.imread("2.jpg")

cv.imshow("image", image)

#averaging (prolly the most common type of blurring)
average = cv.blur(image,(3,3))
cv.imshow("average", average)

#gaussian blur
gaussian = cv.GaussianBlur(image,(3,3),0)
cv.imshow("gaussian", gaussian)

#median blur
medain = cv.medianBlur(image,3)
cv.imshow("median", medain)

#bilateral blur
#the best type of blurring it takes into account the edges also and hence tries to retain them, we can adjust how much we want the blur to retain the edges
bilateral = cv.bilateralFilter(image,10,35,75)
cv.imshow("bilateral", bilateral)

cv.waitKey(0)