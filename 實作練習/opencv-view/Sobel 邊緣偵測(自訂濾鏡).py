import cv2  # 載入opencv模組
import numpy as np  # 載入numpy模組
path = "data/ntust.jpg"

# Sobel 濾鏡
kernel_h = np.array([[-1, -2, -1],[0, 0, 0],[1, 2, 1]]).astype("float32") #Sobel 橫向邊緣偵測
kernel_v = kernel_h.T #矩陣轉置 (#Sobel 縱向邊緣偵測)

def processing(pos):
    ksize = 2*cv2.getTrackbarPos('blur', 'images')-1 #讀取影像高斯模糊濾鏡尺寸
    thresh = cv2.getTrackbarPos('thresh', 'images') #讀取影像二值化的門檻值
    if ksize > 0:
        img_blur = cv2.GaussianBlur(img, (ksize, ksize), 0) #影像前處裡: 高斯模糊
    else:
        img_blur = img
    img_32F = img_blur.astype("float32")/255   

    # 空間濾波
    Sobel_h = cv2.filter2D(img_32F, -1, kernel_h) #使用自訂濾鏡(Sobel 橫向邊緣偵測)
    Sobel_v = cv2.filter2D(img_32F, -1, kernel_v) #使用自訂濾鏡(Sobel 縱向邊緣偵測)
    
    abs_Sobel_h = np.abs(255*Sobel_h).astype("uint8") #開絕對值，轉換至8位元格式
    abs_Sobel_v = np.abs(255*Sobel_v).astype("uint8") #開絕對值，轉換至8位元格式
    img_lower = np.hstack([Sobel_h+0.5, Sobel_v+0.5]) #水平合併顯示用 Sobel 濾波影像(浮雕效果)
    img_lower = np.clip(255*img_lower, 0, 255).astype("uint8") #處理範圍出界問題，轉換至8位元格式
    dst = cv2.bitwise_or(abs_Sobel_h, abs_Sobel_v) #取水平與垂直紋理的聯集
    ret, dst = cv2.threshold(dst, thresh, 255, cv2.THRESH_BINARY) #紋理影像二值化  
    img_upper = np.hstack([img_blur, dst])
    output = np.vstack([img_upper, img_lower])
    output = cv2.cvtColor(output, cv2.COLOR_GRAY2BGR) #為了能上彩色的字，轉換成彩色格式

    font = cv2.FONT_HERSHEY_SIMPLEX #字體
    if ksize >0:
        cv2.putText(output , "GaussianBlur ("+ str(ksize)+"x" + str(ksize)+ ")", (23, 33), font, 0.8, 0, 2)
        cv2.putText(output , "GaussianBlur ("+ str(ksize)+"x" + str(ksize)+ ")", (20, 30), font, 0.8, (0,255,255), 2)
    else:
        cv2.putText(output , "No image blur", (23, 33), font, 0.8, 0, 2)
        cv2.putText(output , "No image blur", (20, 30), font, 0.8, (0,255,255), 2)
    cv2.putText(output , "Sobel (edge detection)", (523, 33), font, 0.8, 0, 2)
    cv2.putText(output , "Sobel (edge detection)", (520, 30), font, 0.8, (0,255,255), 2)
    cv2.putText(output , "Sobel (horizontal)", (23, 33+round(500*h/w)), font, 0.8, 0, 2)
    cv2.putText(output , "Sobel (horizontal)", (20, 30+round(500*h/w)), font, 0.8, (0,255,255), 2)
    cv2.putText(output , "Sobel (vertical)", (523, 33+round(500*h/w)), font, 0.8, 0, 2)
    cv2.putText(output , "Sobel (vertical)", (520, 30+round(500*h/w)), font, 0.8, (0,255,255), 2)
    cv2.imshow('images', output) #顯示成果影像

print('Sobel邊緣偵測(自訂濾鏡)')
print('Sobel 橫向邊緣偵測濾鏡\n' +str(kernel_h))
print('Sobel 縱向邊緣偵測濾鏡\n' +str(kernel_v))
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) #強制以灰階格式讀取，等同參數 0
h, w = img.shape #讀取原影像尺寸
img = cv2.resize(img, (500, int(500*h/w))) #使影像寬度= 500 px
cv2.namedWindow('images')
cv2.createTrackbar('blur', 'images', 1, 9, processing) #建立模糊化滑桿
cv2.createTrackbar('thresh', 'images', 160, 255, processing) #建立二值化滑桿
processing(0) #初始化

while(1):
    k = cv2.waitKey(10) & 0xFF
    if k == 27: #如果是 Esc (ASCII 第27號)，脫離迴圈
        break
    elif k==ord('r'): #按 "r" 鍵重設滑桿數值
         cv2.setTrackbarPos('blur','images', 1)
         cv2.setTrackbarPos('thresh','images', 160)
         processing(0)     

# 關閉所有視窗
cv2.destroyAllWindows()
