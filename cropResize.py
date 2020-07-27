import cv2
import numpy as np

img = cv2.imread("resources/000000058350.jpg")
print(img.shape)
#resize
imgResize = cv2.resize(img,(300,200))

#cropp
imgCropped = img[0:200, 200:500]

cv2.imshow("img",img)
cv2.imshow("resized",imgResize)
cv2.imshow("crop",imgCropped)



cv2.waitKey(0)