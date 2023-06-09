'''cv48: 霍夫(Hough)線偵測'''
import cv2
import numpy as np

img = cv2.imread('data/building.jpg')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5) #影像縮小一倍
img2 = img.copy() #複製影像
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) #轉成灰階影像
edges = cv2.Canny(gray, 50, 150, apertureSize = 3) #Canny邊緣檢測

lines = cv2.HoughLines(edges, 1, np.pi/180, 170) #Hough線偵測

#將每條線的資料，從極座標(rho, theta)，轉換成直角座標(x,y)，再繪製紅色直線
for rho,theta in lines[:,0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img2, (x1,y1), (x2,y2), (0,0,255), 2)

dst = np.hstack((img, img2))
cv2.imshow('src->houghlines', dst)
cv2.waitKey(0) # 按任意鍵離開
cv2.destroyAllWindows()

