#HSV é a abreviatura para o sistema de cores formadas pelas componentes hue (matiz), saturation (saturação) e value (valor). 
import cv2
import numpy as np
def TrackbarController(a):
    # h_min = cv2.getTrackbarPos("Hue min","TrackBars")
    # h_max = cv2.getTrackbarPos("Hue max","TrackBars")
    # sat_min = cv2.getTrackbarPos("Saturation min","TrackBars")
    # sat_max = cv2.getTrackbarPos("Saturation max","TrackBars")
    # val_min = cv2.getTrackbarPos("Val min","TrackBars")
    # val_max = cv2.getTrackbarPos("Val max","TrackBars")
    # print(h_min,h_max,sat_min,sat_max,val_min,val_max)
    # #filter mask
    # lower = np.array([h_min,sat_min,val_min])
    # upper = np.array([h_max,sat_max,val_max])
    # mask = cv2.inRange(imgHSV,lower,upper)
    # imgResult = cv2.bitwise_and(img,img,mask=mask) # do the and operation for each pixel with the mask and the original image
    # cv2.imshow("mask",mask)
    # cv2.imshow("imgResult",imgResult)
    pass


def trackbartomask():
    h_min = cv2.getTrackbarPos("Hue min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue max","TrackBars")
    sat_min = cv2.getTrackbarPos("Saturation min","TrackBars")
    sat_max = cv2.getTrackbarPos("Saturation max","TrackBars")
    val_min = cv2.getTrackbarPos("Val min","TrackBars")
    val_max = cv2.getTrackbarPos("Val max","TrackBars")
    #print(h_min,h_max,sat_min,sat_max,val_min,val_max)
    #filter mask
    lower = np.array([h_min,sat_min,val_min])
    upper = np.array([h_max,sat_max,val_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask) # do the and operation for each pixel with the mask and the original image
    # cv2.imshow("mask",mask)
    # cv2.imshow("imgResult",imgResult)
    return imgResult, mask

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,310)
#hue max do opencv é 179 e não 360
#inicial values for tracking the pizza in the test image 0 19 157 255 199 255
cv2.createTrackbar("Hue min", "TrackBars",0,179,TrackbarController)
cv2.createTrackbar("Hue max", "TrackBars",179,179,TrackbarController)
cv2.createTrackbar("Saturation min", "TrackBars",0,255,TrackbarController)
cv2.createTrackbar("Saturation max", "TrackBars",255,255,TrackbarController)
cv2.createTrackbar("Val min", "TrackBars",0,255,TrackbarController)
cv2.createTrackbar("Val max", "TrackBars",255,255,TrackbarController)


#reading webcam

cap = cv2.VideoCapture(0) # wegcam 0
cap.set(3,640)#set video widht
cap.set(4,480)#set video height
cap.set(10,100)#brightness 
while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    imgresult, mask = trackbartomask()
    cv2.imshow("result", imgresult)
    cv2.imshow("mask", mask)
    if cv2.waitKey(1) & 0xFF == ord('q'): #show img e break with q
        break

# #while True:
# img = cv2.imread("resources/000000058350.jpg")
# imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# #print(imgHSV)

# h_min = cv2.getTrackbarPos("Hue min","TrackBars")
# print(h_min)

# cv2.imshow("Original", img)
# cv2.imshow("Hsv", imgHSV)

# cv2.waitKey(0)
# #if cv2.waitKey(1) & 0xFF == ord('q'): #sho img e break with q
#  #   break
