'''cv23: HSV色彩區塊偵測'''
import cv2 # 匯入 openCV 套件
import numpy as np # 匯入 NumPy 套件
path = 'data/s.jpg'

def processing(pos):
    #讀取調整值
    H_lower = cv2.getTrackbarPos('H_lower','image')
    H_upper = cv2.getTrackbarPos('H_upper','image')
    S_lower = cv2.getTrackbarPos('S_lower','image')
    S_upper = cv2.getTrackbarPos('S_upper','image')
    V_lower = cv2.getTrackbarPos('V_lower','image')
    V_upper = cv2.getTrackbarPos('V_upper','image')

    #限制調整範圍
    if (H_lower > H_upper):
        cv2.setTrackbarPos('H_lower','image', H_upper)
    if (S_lower > S_upper):
        cv2.setTrackbarPos('S_lower','image', S_upper)       
    if (V_lower > V_upper):
        cv2.setTrackbarPos('V_lower','image', V_upper)
       
    lower_range = np.array([H_lower, S_lower, V_lower])
    upper_range = np.array([H_upper, S_upper, V_upper])

    # 根據範圍產生二值遮罩
    mask = cv2.inRange(HSVimg, lower_range, upper_range)

    #破洞處理
    if option==1:
        # 膨脹 (Dilation) -> 腐蝕(Erosion)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7, 7))
        mask = cv2.erode(mask, kernel)
        mask = cv2.dilate(mask, kernel)
        
    elif option==2:
        # 中值濾波 (除脈衝雜訊)
        mask = cv2.medianBlur(mask, 7)

    color_mask= cv2.bitwise_and(BGRimg, BGRimg, mask= mask) # 根據遮罩複製影像 
    cv2.imshow('image', np.hstack([BGRimg, color_mask])) # 水平堆疊顯示


print('HSV色彩區塊偵測: 按 r 鍵重設滑桿數值, 按 Esc 離開')
BGRimg = cv2.imread(path, 1) #讀取影像
HSVimg = cv2.cvtColor(BGRimg, cv2.COLOR_BGR2HSV) #轉換至HSV色空間
cv2.namedWindow('image')
cv2.imshow('image', BGRimg)
option = int(input("破洞處理(1.膨脹腐蝕, 2.中值濾波, 3.不處理)= ? "))

# 建立HSV調色桿
cv2.createTrackbar('H_lower','image', 15, 127, processing)
cv2.createTrackbar('H_upper','image', 40, 127, processing)
cv2.createTrackbar('S_lower','image', 0, 255, processing)
cv2.createTrackbar('S_upper','image', 255, 255, processing)
cv2.createTrackbar('V_lower','image', 0, 255, processing)
cv2.createTrackbar('V_upper','image', 255, 255, processing)
processing(0) #初始化
    
# 迴圈
while(1):  
    k = cv2.waitKey(1) & 0xFF
    if k == 27: # 如果按 'esc', 離開程式
        break
    elif k==ord('r'): # 重設調色桿
         cv2.setTrackbarPos('H_lower','image', 15)
         cv2.setTrackbarPos('H_upper','image', 40)
         cv2.setTrackbarPos('S_lower','image', 0)
         cv2.setTrackbarPos('S_upper','image', 255)
         cv2.setTrackbarPos('V_lower','image', 0)
         cv2.setTrackbarPos('V_upper','image', 255)
         
cv2.destroyAllWindows() #關閉視窗


