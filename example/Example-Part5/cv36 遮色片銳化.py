'''cv36: 遮色片銳利化調整(unsharp masking, USM)'''
import cv2  # 載入opencv模組
import numpy as np  # 載入numpy模組
path = "data/s.jpg"
font = cv2.FONT_HERSHEY_SIMPLEX

def unsharp_masking(pos): #自訂函式
    ksize =  2*cv2.getTrackbarPos('blur', 'images')+1  #讀取滑桿高斯模糊數值
    low_pass = cv2.GaussianBlur(img, (ksize, ksize), 0) #計算高斯低通濾波影像
    high_pass = img - low_pass # 計算高斯高通影像
    disp_high_pass = high_pass + 0.5 # 顯示用高通影像
    weight =  cv2.getTrackbarPos('weight', 'images')/100  #讀取滑桿銳化權重數值
    #dst = img + weight * high_pass # 產生銳化影像
    dst = cv2.addWeighted(img, 1, high_pass, weight, 0)

    #顯示文字
    str1 = 'Low Pass (' + str(ksize) + 'x' + str(ksize) + ')'
    str2 = 'High Pass (' + str(ksize) + 'x' + str(ksize) + ')'
    str3 = 'Unsharp Masking'
    cv2.putText(low_pass , str1, (23, 53), font, 0.8, 0, 2)      
    cv2.putText(low_pass , str1, (20, 50), font, 0.8, (0,1,1), 2)   #浮點格式下，色彩範圍[0 1]                 
    cv2.putText(disp_high_pass , str2, (23, 53), font, 0.8, 0, 2)      
    cv2.putText(disp_high_pass, str2, (20, 50), font, 0.8, (0,1,1), 2)
    cv2.putText(dst, str3, (23, 53), font, 0.8, 0, 2)
    cv2.putText(dst, str3, (20, 50), font, 0.8, (0,1,1), 2)
    
    img_upper = np.hstack([img, dst]) #水平排列 img 與 dst
    img_lower = np.hstack([low_pass, disp_high_pass]) #水平排列 low_pass 與 high_pass
    output = np.vstack([img_upper, img_lower])
    cv2.imshow('images', output)  #顯示處理後的影像                

print('遮色片銳利化調整(unsharp masking, USM)：按 r 鍵重設滑桿數值, 按 Esc 離開')
img = cv2.imread(path, 1).astype("float32")/255 #將影像以彩色格式讀取，並轉換至32位元浮點格式
h, w = img.shape[:2] #讀取影像的高,寬
img = cv2.resize(img, (500, int(500*h/w))) #使影像寬度= 500 px
cv2.namedWindow('images')
cv2.createTrackbar('blur', 'images', 5, 20, unsharp_masking) #建立滑桿
cv2.createTrackbar('weight', 'images', 100, 200, unsharp_masking) #建立滑桿
unsharp_masking(0) #初始化

while(1):
    k = cv2.waitKey(20) & 0xFF
    if k == 27: #如果是 Esc (ASCII 第27號)，脫離迴圈
        break
    elif k==ord('r'): #按 "r" 鍵重設滑桿數值
         cv2.setTrackbarPos('blur','images', 5)
         cv2.setTrackbarPos('weight', 'images', 100)
         unsharp_masking(0)      

# 關閉所有視窗
cv2.destroyAllWindows()
