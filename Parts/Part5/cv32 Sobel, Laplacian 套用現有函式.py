'''cv32: Sobel 與 Laplacian 套用現有函式'''
import cv2  # 載入opencv模組
import numpy as np  # 載入numpy模組
path = "data/s.jpg"

def processing(pos):
    ksize = 2*cv2.getTrackbarPos('size', 'images')+1 #讀取影像高斯模糊濾鏡尺寸
    img_32F = img.astype("float32")/255   
    # 空間濾波
    Sobel_h = cv2.Sobel(img_32F, -1, 0, 1, None, ksize+2) #Sobel 橫向邊緣偵測
    Sobel_v = cv2.Sobel(img_32F, -1, 1, 0, None, ksize+2) #Sobel 縱向邊緣偵測
    Laplacian = cv2.Laplacian(img_32F, -1, None, ksize) #Laplacian 高頻(點)偵測
    
    Laplacian = np.clip(255*(Laplacian+0.5), 0, 255).astype("uint8") #轉換至8位元格式
    img_lower = np.hstack([Sobel_h/ksize**3+0.5, Sobel_v/ksize**3+0.5]) #水平合併顯示用 Sobel 濾波影像(浮雕效果)
    img_lower = np.clip(255*img_lower, 0, 255).astype("uint8") #處理範圍出界問題，轉換至8位元格式  
    img_upper = np.hstack([img, Laplacian])
    output = np.vstack([img_upper, img_lower])
    if img.ndim == 2:
        output = cv2.cvtColor(output, cv2.COLOR_GRAY2BGR) #為了能上彩色的字，轉換成彩色格式

    font = cv2.FONT_HERSHEY_SIMPLEX #字體
    cv2.putText(output , "Input", (23, 33), font, 0.8, 0, 2)
    cv2.putText(output , "Input", (20, 30), font, 0.8, (0,255,255), 2)
    cv2.putText(output , "Laplacian ("+ str(ksize+2)+"x" + str(ksize+2)+ ")", (523, 33), font, 0.8, 0, 2)
    cv2.putText(output , "Laplacian ("+ str(ksize+2)+"x" + str(ksize+2)+ ")", (520, 30), font, 0.8, (0,255,255), 2)
    cv2.putText(output , "Sobel (horizontal " + str(ksize+2)+"x" + str(ksize+2)+ ")", (23, 33+round(500*height/width)), font, 0.8, 0, 2)
    cv2.putText(output , "Sobel (horizontal " + str(ksize+2)+"x" + str(ksize+2)+ ")", (20, 30+round(500*height/width)), font, 0.8, (0,255,255), 2)
    cv2.putText(output , "Sobel (vertical " + str(ksize+2)+"x" + str(ksize+2)+ ")", (523, 33+round(500*height/width)), font, 0.8, 0, 2)    
    cv2.putText(output , "Sobel (vertical " + str(ksize+2)+"x" + str(ksize+2)+ ")", (520, 30+round(500*height/width)), font, 0.8, (0,255,255), 2)
    cv2.imshow('images', output) #顯示成果影像

print('Sobel 與 Laplacian 套用現有函式：按 r 鍵重置，按 Esc 離開')
img = cv2.imread(path) #以影像原格式讀取(彩色或灰階)
[height, width] = img.shape[:2] #讀取原影像尺寸
        
img = cv2.resize(img, (500, int(500*height/width))) #使影像寬度= 500 px
cv2.namedWindow('images')
cv2.createTrackbar('size', 'images', 1, 3, processing) #建立模糊化滑桿
processing(0) #初始化

while(1):
    k = cv2.waitKey(10) & 0xFF
    if k == 27: #如果是 Esc (ASCII 第27號)，脫離迴圈
        break
    elif k==ord('r'): #按 "r" 鍵重設滑桿數值
         cv2.setTrackbarPos('size','images', 1)
         processing(0)     

# 關閉所有視窗
cv2.destroyAllWindows()
