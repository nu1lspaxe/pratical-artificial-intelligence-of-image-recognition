'''cv22: HSV影像調色'''
import cv2
import numpy as np
path = 'data/s.jpg'  #影像路徑

def processing(x):
    #讀取調整值
    hue_shift = (cv2.getTrackbarPos('H','image') - 100)/100
    saturation_weight = cv2.getTrackbarPos('S','image')/100
    value_weight = cv2.getTrackbarPos('V','image')/100

    #調整影像HSV值
    HSVimg2=HSVimg1/255
    HSVimg2[:,:,0] = (HSVimg2[:,:,0] + hue_shift) % 1
    HSVimg2[:,:,1] = HSVimg2[:,:,1] * saturation_weight
    HSVimg2[:,:,2] = HSVimg2[:,:,2] * value_weight
    HSVimg2= (np.clip(HSVimg2, 0, 1) *255).astype("uint8")
    #將數值限制在[0 1]範圍，再轉換至uint8格式
    
    BGRimg2 = cv2.cvtColor(HSVimg2, cv2.COLOR_HSV2BGR) #轉換至BGR色空間
    imgs = np.hstack([BGRimg1, BGRimg2]) #左右堆疊影像
    h, w, ch = BGRimg1.shape #讀取影像高,寬,通道數

    #呈現HSV調整量
    cv2.putText(imgs, "Hue shift: %d"%(hue_shift*360), (w+20, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(imgs, "Saturation weight: %.2f"%saturation_weight, (w+20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(imgs, "Value weight: %.2f"%value_weight, (w+20, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.imshow('image', imgs)

print('HSV影像調色: 按 r 鍵重設滑桿數值, 按 Esc 離開')
BGRimg1 = cv2.imread(path) #讀取影像
HSVimg1 = cv2.cvtColor(BGRimg1, cv2.COLOR_BGR2HSV) #轉換至HSV色空間
cv2.namedWindow('image')

# 建立HSV調色桿
cv2.createTrackbar('H','image', 100, 200, processing)
cv2.createTrackbar('S','image', 100, 200, processing)
cv2.createTrackbar('V','image', 100, 200, processing)
processing(0) #初始化

while(1):
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27: #如果是 Esc (ASCII 第27號)，脫離迴圈
        break
    elif k==ord('r'):
         cv2.setTrackbarPos('H','image', 100)
         cv2.setTrackbarPos('S','image', 100)
         cv2.setTrackbarPos('V','image', 100)
         processing(0)
         
cv2.destroyAllWindows()

