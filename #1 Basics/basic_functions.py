import cv2 as cv

#read
image = cv.imread("2.jpg")
cv.imshow("cat", image)

#grayscale
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

#blur
blur = cv.GaussianBlur(image,(7,7),cv.BORDER_DEFAULT) # (7,7) is the kernel value, use an odd number only, increase to increase the blur factor
cv.imshow("blur", blur)

#edges
#using the canny edges method to find out the edges
edges = cv.Canny(blur,125,175) #threshold 1 and threshold 2 values
cv.imshow("edges", edges)

#dilating
dilated = cv.dilate(edges,(7,7),iterations=1)
cv.imshow("dilated", dilated)

#eroding
eroded = cv.erode(dilated,(7,7),iterations=1)
cv.imshow("eroded", eroded)

#resizing
resized = cv.resize(image,(500,500),interpolation=cv.INTER_AREA)
cv.imshow("resized", resized)

#cropping
cropped = image[50:500,200:300]
cv.imshow("cropped", cropped)

cv.waitKey(0)