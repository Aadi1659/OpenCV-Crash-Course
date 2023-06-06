import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread("2.jpg")
cv.imshow("Cat", image)

#grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#hsv
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

#l*a*b
lab = cv.cvtColor(image, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

#rgb
rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

#hsv 2 bgr
bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("BGR", bgr)

#matplotlib takes the default color of RGB whereas the opencv takes the BGR color
# plt.imshow(bgr)
# plt.show()

cv.waitKey(0)
