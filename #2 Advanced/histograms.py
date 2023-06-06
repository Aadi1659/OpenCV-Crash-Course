import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

image = cv.imread("2.jpg")
cv.imshow("Cat",image)

blank = np.zeros(image.shape[:2], dtype='uint8')
cv.imshow("Blank",blank)

gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#mask
mask = cv.circle(blank,(image.shape[1]//2,image.shape[0]//2),100,255,-1)
cv.imshow("Mask",mask)

masked = cv.bitwise_and(image,image,mask=mask)
cv.imshow("Mask",masked)

#grayscale histogram
#gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])
#this function takes the input as list, then it asks for the code 0 for grayscale, None for the masking part, then the bins (256) and finally the range of all pixel values

#masked_hist = cv.calcHist([gray],[0],mask,[256],[0,256])

# plt.figure()
# plt.title("Grayscale histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()


# plt.figure()
# plt.title("Masked histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.plot(masked_hist)
# plt.xlim([0,256])
# plt.show()

#COLOR HISTOGRAM

plt.figure()
plt.title("Colored Masked histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
colors = ('b','g','r')
for i,col in enumerate(colors):
    histogram = cv.calcHist([image],[i],mask,[256],[0,256])
    plt.plot(histogram,color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)
