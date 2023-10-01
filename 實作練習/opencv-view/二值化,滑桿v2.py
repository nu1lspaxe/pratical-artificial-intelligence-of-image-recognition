import cv2
import numpy as np

def processing(x): #自訂函式
    t = cv2.getTrackbarPos('threshold', 'image')  #讀取滑桿數值 t
    ret,thresh = cv2.threshold(img, t, 255, cv2.THRESH_BINARY)  #根據 t 值做影像二值化
    cv2.imshow('image', thresh)  #顯示二值化後的影像

                
img = cv2.imread('data/s.jpg', 0) #將影像以灰階形式開啟
cv2.namedWindow('image') #視窗命名
cv2.createTrackbar('threshold', 'image', 128, 255, processing) #建立滑桿
#cv2.createTrackbar(滑桿名稱, 從屬視窗名稱, 調整值, 最大值, 反應函式)
processing(0)

while(1): #無限迴圈
    k = cv2.waitKey(1) & 0xFF #等待任意鍵輸入
    if k == 27: #如果是 Esc (ASCII 第27號)，脫離迴圈
        break

cv2.destroyAllWindows()
