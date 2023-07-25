'''cv49: 霍夫(Hough)圓偵測'''
import cv2
import numpy as np

img = cv2.imread('data/coins.png',0)
img = cv2.medianBlur(img,5) #中值濾波
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR) #灰階轉彩色

#霍夫圓偵測
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT, 1, 20,
                            param1=50, param2=30, minRadius=20, maxRadius=30)

circles = np.uint16(np.around(circles)) #將圓的數據轉成16-bit正整數
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg, (i[0],i[1]), i[2], (0,255,0), 2) #繪製圓(綠色)
    # draw the center of the circle
    cv2.circle(cimg, (i[0],i[1]), 2, (0,0,255), 3) #繪製圓心(紅色)

cv2.imshow('circles',img)
cv2.imshow('detected circles',cimg)
cv2.waitKey(0) # 按任意鍵離開
cv2.destroyAllWindows()
