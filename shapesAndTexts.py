import cv2
import numpy as np


img = np.zeros((512,512,3), np.uint8)#creates a empty black rgb image

print(img.shape)
#img[:] = 255,0,0 # change the interval to this valor, if empty [:] changes whole image


#create lines
# img start point and end point of the line, color, thickness
cv2.line(img,(0,0),(300,300),(0,255,0),3)
cv2.line(img,(10,0),(img.shape[0], img.shape[1]),(0,0,255),3)

#create retangle
#img ,startpoint, end point, color, thicknes
# 
cv2.rectangle(img,(0,0),(250,350),(255,0,0),2)
cv2.rectangle(img,(350,300),(450,350),(255,100,0),cv2.FILLED)

#circles
#img, startpoint, radios, color, thick
cv2.circle(img,(400,50),30,(200,200,0),2)


#text
cv2.putText(img," OPENCV ", (300,200), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,150,0),1 )

cv2.imshow("image",img)

cv2.waitKey(0)