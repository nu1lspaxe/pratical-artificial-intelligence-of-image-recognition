import cv2  # 載入opencv模組
import numpy as np  # 載入numpy模組
path = "data/ntust.jpg"

def sharpening(pos): #自定義影像模糊化/銳化函式
    t = cv2.getTrackbarPos('sharpness', 'images')  #讀取滑桿數值 t
    
    if (t<17): ## 用 ksize x ksize 大小的範圍用高斯模糊模糊原圖
        ksize = 2*(17 - t)+1 #必須是奇數
        dst = cv2.GaussianBlur(img, (ksize, ksize), 0)
        str1 = 'Blurring (' + str(ksize) + 'x' + str(ksize) + ')'
        
    elif (t>=17): ## 用遮色片銳利化(USM)
        n = t - 17
        dst = cv2.GaussianBlur(img, (7,7), 0)
        dst = cv2.addWeighted(img, 1+n/3.0, dst, -n/3.0, 0)
        str1 = 'Sharping (' + str(round(n/3, 2)) + ')'
        
    cv2.rectangle(dst, (10, 20), (240, 70), 0, -1) #文字的黑色背景框
    cv2.putText(dst , str1, (20, 50), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (255 - t*(255/34), 255, t*(255/34)), 2)    #變色文字     
    output = np.hstack([img, dst]) #水平排列 img 與 dst
    cv2.imshow('images', output)  #顯示處理後的影像                

print('模糊化與銳利化：按 r 鍵重設滑桿數值, 按 esc 離開')
img = cv2.imread(path)
h, w, ch = img.shape
img = cv2.resize(img, (600, int(600*h/w))) #使影像寬度= 600 px
cv2.namedWindow('images')
cv2.imshow('images', img)
cv2.createTrackbar('sharpness', 'images', 17, 34, sharpening) #建立滑桿
sharpening(0) #初始化

while(1):
    k = cv2.waitKey(20) & 0xFF
    if k == 27: #如果是 Esc (ASCII 第27號)，脫離迴圈
        break
    elif k==ord('r'): #按 "r" 鍵重設滑桿數值
         cv2.setTrackbarPos('sharpness','images', 17)
         sharpening(0)      

# 關閉所有視窗
cv2.destroyAllWindows()
