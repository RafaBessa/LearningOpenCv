#HSV é a abreviatura para o sistema de cores formadas pelas componentes hue (matiz), saturation (saturação) e value (valor). 
import cv2
import numpy as np
# def TrackbarController(a):
#     pass


# def trackbartomask():
#     h_min = cv2.getTrackbarPos("Hue min","TrackBars")
#     h_max = cv2.getTrackbarPos("Hue max","TrackBars")
#     sat_min = cv2.getTrackbarPos("Saturation min","TrackBars")
#     sat_max = cv2.getTrackbarPos("Saturation max","TrackBars")
#     val_min = cv2.getTrackbarPos("Val min","TrackBars")
#     val_max = cv2.getTrackbarPos("Val max","TrackBars")
#     #print(h_min,h_max,sat_min,sat_max,val_min,val_max)
#     #filter mask
#     lower = np.array([h_min,sat_min,val_min])
#     upper = np.array([h_max,sat_max,val_max])
#     mask = cv2.inRange(imgHSV,lower,upper)
#     imgResult = cv2.bitwise_and(img,img,mask=mask) # do the and operation for each pixel with the mask and the original image
#     # cv2.imshow("mask",mask)
#     # cv2.imshow("imgResult",imgResult)
#     return imgResult, mask


#recebe uma mascara, e uma região, calcula a quantidade de pixels dentro e fora da mascara
def MaskAnalise(p1,p2,mask):
    branco = 255
    preto = 0
    npMask = np.array(mask)
    region = npMask[p1[0]:p2[0],p1[1]:p2[1]]
    shape = npMask.shape
    totalPixelMask = shape[0] * shape[1]
    totalPixelRegion = (p2[0] - p1[0]) * (p2[1] - p1[1])
    percentacertoRegion = (np.count_nonzero(region == branco))/totalPixelRegion
    percentacertoMask = (np.count_nonzero(npMask == preto) - np.count_nonzero(region == preto)) / (totalPixelMask - totalPixelRegion)
    return percentacertoRegion, percentacertoMask
    

def generateMask(param):
    lower = np.array([param["h_min"],param["sat_min"],param["val_min"]])
    upper = np.array([param["h_max"],param["sat_max"],param["val_max"]])
    mask = cv2.inRange(imgHSV,lower,upper)
    return mask


def evaluateMask(p1,p2,mask):#calcula a media com pesos da mascara
    percentReg, percentMask = MaskAnalise(p1,p2,mask)
    return (percentReg + percentMask)/2

def GenerateImageMaskMerge(img,mask):
    return cv2.bitwise_and(img,img,mask=mask) # do the and operation for each pixel with the mask and the original image

step = 5
margin = 0.001
def MaskOtimization(param,p1,p2,lastmask,lastresult,changparam, aumentando):
    #retornar mascara, imgresult, param, aumentando, end
    tempParam = param.copy()
    if aumentando == 0:
        if "min" in changparam:
            aumentando = 1
        else:
            aumentando = -1

    if aumentando == 1: 
        tempParam[changparam] += step
    else:
        tempParam[changparam] -= step

    tempmask = generateMask(tempParam)
    
    result = evaluateMask(p1,p2,tempmask)
    
    if result > lastresult  * (1.0-margin):
        param = tempParam
        mask = tempmask
        end = False 
    else: 
        mask = lastmask
        end = True
        aumentando = 0    

    imgResult = GenerateImageMaskMerge(img,mask)
    
    # cv2.imshow("mask",mask)
    # cv2.imshow("imgResult",imgResult)
    return imgResult, mask, result, param, aumentando, end

# cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars",640,310)
#hue max do opencv é 179 e não 360
#inicial values for tracking the pizza in the test image 0 19 157 255 199 255
# cv2.createTrackbar("Hue min", "TrackBars",0,179,TrackbarController)
# cv2.createTrackbar("Hue max", "TrackBars",179,179,TrackbarController)
# cv2.createTrackbar("Saturation min", "TrackBars",0,255,TrackbarController)
# cv2.createTrackbar("Saturation max", "TrackBars",255,255,TrackbarController)
# cv2.createTrackbar("Val min", "TrackBars",0,255,TrackbarController)
# cv2.createTrackbar("Val max", "TrackBars",255,255,TrackbarController)


#reading webcam

cap = cv2.VideoCapture(0) # wegcam 0
cap.set(3,640)#set video widht
cap.set(4,480)#set video height
cap.set(10,100)#brightness
posIni = (150,150)
posFin = (300,300) 
#valores a serem alterados
param =   {
    "h_min" : 0,
    "h_max" : 179,
    "sat_min" : 0,
    "sat_max" : 255,
    "val_min" : 0,
    "val_max" : 255
    }


#Start loop Just for preparing to start, s to start
while True:
    success, img = cap.read()
   # cv2.rectangle(img,(150,150),(300,300),(255,0,0),2)
    cv2.imshow("video", img)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask = generateMask(param)
    imgresult = GenerateImageMaskMerge(img,mask)
    cv2.rectangle(imgresult,posIni,posFin,(255,0,0),2)
    #cv2.imshow("masktest", x)
    cv2.imshow("result", imgresult)
    cv2.imshow("mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('s'): #show img e break with q
        break




success, img = cap.read()
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
mask = generateMask(param)
result = evaluateMask(posIni,posFin,mask)
#Optimization loop   
for changparam in param: # for each param, we increase or decrease it, until the MaskOtimization say its ok, the otimization is based on the means of 
    end = False          # pixels corected labeled inside and outside of the  box 
    aumentando = 0
    while not end:
        success, img = cap.read()
        imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        cv2.imshow("video", img)
        imgResult, mask, result, param, aumentando, end = MaskOtimization(param, posIni, posFin, mask, result, changparam, aumentando)
        print(result)
        print(param)
        cv2.rectangle(imgresult,posIni,posFin,(255,0,0),2)
        #cv2.imshow("masktest", x)
        cv2.imshow("result", imgresult)
        cv2.imshow("mask", mask)
        if cv2.waitKey(1) & 0xFF == ord('q'): #show img e break with q
            break

print("CAMERA OPTIMIZED ")
#normal loop
while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask = generateMask(param)
    imgresult = GenerateImageMaskMerge(img,mask)
    #cv2.rectangle(imgresult,posIni,posFin,(255,0,0),2)
    #cv2.imshow("masktest", x)
    cv2.imshow("result", imgresult)
    cv2.imshow("mask", mask)

 

    if cv2.waitKey(1) & 0xFF == ord('q'): #show img e break with q
        break

