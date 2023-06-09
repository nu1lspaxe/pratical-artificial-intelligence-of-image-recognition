'''c3-4 cv25: 套用 gamma 曲線，調整影像明暗
顯示科技教育聯盟│顯示影像色彩處理實作│孫沛立'''
import cv2  # 載入opencv模組
import numpy as np  # 載入numpy模組
path = "data/s.jpg"  #影像路徑

def gamma_curve(gamma): ## 產生 gamma 曲線對照表
    gamma_LUT=np.arange(256).astype("uint8")
    for i in range(0,256):  #根據 gamma 值 產生高斯分配
        gamma_LUT[i]=255*(i/255)**gamma
    return gamma_LUT

def processing(pos): ##套用對照表，產生影像
    gamma = cv2.getTrackbarPos('gamma','images')/100 #讀取 gamma 滑桿數值
    gamma_LUT = np.array(gamma_curve(gamma)) #產生 gamma 曲線1維對照表 

    img2 = np.zeros((256,256,3)).astype("uint8") #產生黑影像
    
    for y in range (1,256): #繪製對照表中的 gamma 曲線
        cv2.line(img2, (y-1, 255-gamma_LUT[y-1]), (y, 255-gamma_LUT[y]), (0,255,255), 4, cv2.LINE_AA)
##    for y in range (0,256): #繪製對照表中的 gamma 曲線
##        cv2.circle(img2, (y, 255 - gamma_LUT[y]), 3, (0,255,255), -1)
        
    img2 = cv2.resize(img2, (h, h)) #調整曲線影像的大小，使高度與輸入影像一致
    img3 = cv2.LUT(img1, np.array(gamma_LUT).astype("uint8")) #影像明暗套用對照表

    img4 = np.hstack([img1, img2, img3]) #影像水平堆疊
    cv2.putText(img4,'Input',(10, round(0.1*h)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
    cv2.putText(img4,'gamma = ' + str(gamma) ,(10+w, round(0.1*h)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
    cv2.putText(img4,'Output',(10+h+w, round(0.1*h)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2) 
    cv2.imshow("images", img4) #顯示影像

## 主程式起始處
print("套用 gamma 曲線，調整影像明暗：按 r 鍵重置 gamma 數值，按 Esc 離開")
img1 = cv2.imread(path, cv2.IMREAD_COLOR) #強制以彩色模式開啟影像，相當於參數1
h, w = img1.shape[:2] #讀取影像高寬
cv2.namedWindow('images') #視窗命名
cv2.createTrackbar('gamma','images', 100, 300, processing) # 建立 gamma 滑桿
processing(0) #初始化

while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27: #如果是 Esc (ASCII 第27號)，脫離迴圈
        break
    elif k==ord('r'): #按"r"重置 gamma 數值
         cv2.setTrackbarPos('gamma','images', 100)
         processing(0)
         
cv2.destroyAllWindows()




