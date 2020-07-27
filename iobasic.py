#https://www.youtube.com/watch?v=WQeoO7MI0Bs
import cv2

#reading image
img = cv2.imread("resources/000000058350.jpg")

cv2.imshow("output", img)
cv2.waitKey(2000) #so that the imshow does not close ( 0 - inifite, >0 time in ms)

#reading video
cap = cv2.VideoCapture("resources/sample-mp4-file.mp4")
#cap seq of images

while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): #sho img e break with q
        break
    

#reading webcam

cap = cv2.VideoCapture(0) # wegcam 0
cap.set(3,640)#set video widht
cap.set(4,480)#set video height
cap.set(10,100)#brightness 
while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): #sho img e break with q
        break
    
# #ids for set
# 0 -V_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
# 1 - CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
# 2 - CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file: 0 - start of the film, 1 - end of the film.
# 3 - CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
# 4 - CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
# CV_CAP_PROP_FPS Frame rate.
# CV_CAP_PROP_FOURCC 4-character code of codec.
# CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
# CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
# CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
# 10 - CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
# CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
# CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
# CV_CAP_PROP_HUE Hue of the image (only for cameras).
# CV_CAP_PROP_GAIN Gain of the image (only for cameras).
# CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
# CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
# CV_CAP_PROP_WHITE_BALANCE_U The U value of the whitebalance setting (note: only supported by DC1394 v 2.x backend currently)
# CV_CAP_PROP_WHITE_BALANCE_V The V value of the whitebalance setting (note: only supported by DC1394 v 2.x backend currently)
# CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)
# CV_CAP_PROP_ISO_SPEED The ISO speed of the camera (note: only supported by DC1394 v 2.x backend currently)
# CV_CAP_PROP_BUFFERSIZE Amount of frames stored in internal buffer memory (note: only supported by DC1394 v 2.x backend currently)