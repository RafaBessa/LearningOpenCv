import cv2
import numpy as np
#convert to grayscale

img = cv2.imread("resources/000000058350.jpg")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#blur
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0) #img kernel e sigmaX
#edge dectection
imgCanny = cv2.Canny(img,100,100) #im th1 th2 (bigger th = less edge)
#inclease edge thickness
imgDialation = cv2.dilate(imgCanny,kernel, iterations=1)#img kernel numiteration/thickness
#reduce edge thickness
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("out",imgGray)
cv2.imshow("blur", imgBlur)
cv2.imshow("edge", imgCanny)
cv2.imshow("dialation", imgDialation)
cv2.imshow("erro", imgEroded)
cv2.waitKey(0)