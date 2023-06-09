'''cv46: hsv空間膚色偵測'''
import cv2 # 匯入 openCV 套件
import numpy as np # 匯入 NumPy 套件

cap = cv2.VideoCapture(0) # 建立視訊物件

while(1): # 擷取視訊影像之迴圈

    # 擷取畫面
    _, frame = cap.read()
    frame = cv2.resize(frame, (0,0), fx=0.75, fy=0.75) # 影像縮小一倍
    #frame = cv2.resize(frame, (800,400))

    # 從 BGR 轉換至 HSV 色空間
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 定義 HSV (hue, saturation, value) 空間的色彩範圍 
    lower_skin = np.array([0,50,50])
    upper_skin = np.array([80,200,200]) # maximum [180, 256, 256]

    # 取得色彩範圍內影像區域遮罩
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    #Dilation -> Erosion
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7, 7))
    dilated = cv2.dilate(mask, kernel)
    mask = cv2.erode(dilated, kernel)

    # # 中值濾波 (除脈衝雜訊)
    # mask = cv2.medianBlur(mask, 7)
    
    # 根據遮罩複製影像
    res= cv2.bitwise_and(frame, frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27: # 如果按 'esc', 離開程式
        break

cap.release()
cv2.destroyAllWindows() #關閉視窗
