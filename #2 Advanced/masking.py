import numpy as np
import cv2 as cv

image = cv.imread("2.jpg")

print(f"Image height is {image.shape[0]} and width is {image.shape[1]}")
blank = np.zeros(image.shape[:2], dtype='uint8')
#blank canvas has to be equal to the image size 
cv .imshow("BLANK", blank)

circle_mask = cv.circle(blank.copy(),(image.shape[1]//2,image.shape[0]//2),200,255,-1)
cv.imshow("CIRCLE MASK", circle_mask)

rectangle_mask = cv.rectangle(blank.copy(),(160,320),(480,640),255,-1)
cv.imshow("RECTANGLE MASK", rectangle_mask)

weird_mask = cv.bitwise_or(circle_mask,rectangle_mask)
cv.imshow("WEIRD MASK", weird_mask)

masked = cv.bitwise_and(image,image,mask=weird_mask)
cv.imshow("MASKED", masked)

cv .waitKey(0)