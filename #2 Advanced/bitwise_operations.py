import numpy as np
import cv2 as cv

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow("RECTANGLE",rectangle)
cv.imshow("CIRCLE",circle)
 
#BITWISE AND
#retuns the intersecting regions
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow("BITWISE AND",bitwise_and)

#BITWISE OR
#returns all the regions, imagine rectangle on top of circle
#non-intersecting regions
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow("BITWISE OR",bitwise_or)

#BITWISE XOR
#non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("BITWISE XOR",bitwise_xor)

#BITWISE NOT
#just inverts the bits
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("BITWISE NOT",bitwise_not)    

cv.waitKey(0)