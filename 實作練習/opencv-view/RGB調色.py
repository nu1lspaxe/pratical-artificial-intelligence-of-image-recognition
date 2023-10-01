import cv2
import numpy as np
font = cv2.FONT_HERSHEY_SIMPLEX
path = 'data/s.jpg' #影像路徑

def processing(pos):
    #讀取調整值
    R_weight = cv2.getTrackbarPos('R','image')/100
    G_weight = cv2.getTrackbarPos('G','image')/100
    B_weight = cv2.getTrackbarPos('B','image')/100

    #調整影像RGB值
    BGRimg2 = BGRimg1 / 255
    BGRimg2[:,:,0] = BGRimg2[:,:,0] * B_weight
    BGRimg2[:,:,1] = BGRimg2[:,:,1] * G_weight
    BGRimg2[:,:,2] = BGRimg2[:,:,2] * R_weight
    BGRimg2= (np.clip(BGRimg2, 0, 1) *255).astype("uint8")
    #將數值限制在[0 1]範圍，再轉換至uint8格式
    
    imgs = np.hstack((BGRimg1, BGRimg2)) #左右堆疊影像
    h, w, ch = BGRimg1.shape #讀取影像高,寬,通道數

     #呈現RGB調整量   
    cv2.putText(imgs, "R weight: %.2f"%R_weight, (w+20, 20),
                        font, 0.7, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(imgs, "G weight: %.2f"%G_weight, (w+20, 50),
                        font, 0.7, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(imgs, "B weight: %.2f"%B_weight, (w+20, 80),
                        font, 0.7, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.imshow('image',imgs)

print('RGB影像調色: 按 r 鍵重設滑桿數值, 按 Esc 離開')
BGRimg1 = cv2.imread(path) #讀取影像
cv2.namedWindow('image')

# 建立RGB調色桿
cv2.createTrackbar('R','image', 100, 200, processing)
cv2.createTrackbar('G','image', 100, 200, processing)
cv2.createTrackbar('B','image', 100, 200, processing)
processing(0) #初始化

while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27: #如果是 Esc (ASCII 第27號)，脫離迴圈
        break
    elif k==ord('r'):
         cv2.setTrackbarPos('R','image', 100)
         cv2.setTrackbarPos('G','image', 100)
         cv2.setTrackbarPos('B','image', 100)
         processing(0)        

cv2.destroyAllWindows()


