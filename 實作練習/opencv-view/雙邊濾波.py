import cv2  # 載入opencv模組
import numpy as np  # 載入numpy模組
path = "data/s.jpg"

def addGaussianNoise(image, sigma): ##產生高斯雜訊
    noise = np.random.normal(0, sigma, (h,w,3)) #產生標準差為sigma，平均值為0的高斯分配隨機數
    noisy_img = np.clip(image + noise, 0, 255).astype("uint8") #將雜訊加入影像，並轉換至8位元格式
    return noisy_img #傳回含雜訊的影像

def denoising(pos): ##調整雜訊濃度與濾鏡大小
    ## 加雜訊
    noise_level = cv2.getTrackbarPos("sigmaNoise","images") #讀取高斯雜訊滑桿數值
    noisy_img = addGaussianNoise(img, noise_level) #加入高斯雜訊

    ## 除雜訊
    sigmaColor = max(cv2.getTrackbarPos("sigmaColor","images"), 1) #讀取高斯色差係數滑桿數值
    sigmaSpace = max(cv2.getTrackbarPos("sigmaSpace","images"), 1) #讀取高斯空間係數滑桿數值
    GaussianBlur_img = cv2.GaussianBlur(noisy_img, (7, 7), sigmaSpace/4)
    BilateralFilter_img = cv2.bilateralFilter(noisy_img, 7, sigmaColor, sigmaSpace)

    font = cv2.FONT_HERSHEY_SIMPLEX #字體
    str1 = "GaussianNoise  (sigmaSpace= " + str(noise_level) + ")"
    str2 = "GaussianBlur (sigmaSpace=" + str(round(sigmaSpace/4, 2)) + ")"
    str3 = "BilateralFilter (Color=" + str(sigmaColor) + ", Space=" + str(sigmaSpace) + ")"
    cv2.putText(noisy_img , str1, (13,33), font, 0.8, 0, 2)
    cv2.putText(noisy_img , str1, (10,30), font, 0.8, (0,255,255), 2)
    cv2.putText(GaussianBlur_img , str2, (13,33), font, 0.8, 0, 2)
    cv2.putText(GaussianBlur_img , str2, (10,30), font, 0.8, (0,255,255), 2)
    cv2.putText(BilateralFilter_img , str3, (13,33), font, 0.8, 0, 2)
    cv2.putText(BilateralFilter_img , str3, (10,30), font, 0.8, (0,255,255), 2)
    
    output = np.hstack([noisy_img, GaussianBlur_img, BilateralFilter_img])    
    cv2.imshow("images", output)

## 主程式起始處
print("雙邊濾波(bilateral filtering)：按 r 鍵重置, 按 Esc 離開")
img = cv2.imread(path, cv2.IMREAD_COLOR) #強制以彩色模式開啟影像，相當於參數1
h, w = img.shape[:2] #讀取原影像尺寸
img = cv2.resize(img, (500, int(500*h/w))) #使影像寬度= 500 px
h, w = img.shape[:2] #讀取原影像尺寸
cv2.namedWindow("images")
cv2.createTrackbar("sigmaNoise", "images", 20, 30, denoising) #建立高斯雜訊係數滑桿
cv2.createTrackbar("sigmaColor", "images", 20, 100, denoising) #建立高斯色差係數滑桿
cv2.createTrackbar("sigmaSpace", "images", 20, 100, denoising) #建立高斯空間係數滑桿
denoising(0) #初始化

while (1):
    k = cv2.waitKey(10) & 0xFF
    if k == 27: #如果是 Esc (ASCII 第27號)，脫離迴圈
        break
    elif k==ord('r'): #按 "r" 鍵重設滑桿數值
         cv2.setTrackbarPos("sigmaNoise","images", 20)
         cv2.setTrackbarPos("sigmaColor","images", 20)
         cv2.setTrackbarPos("sigmaSpace","images", 20)
         denoising(0)
         
# 關閉所有視窗
cv2.destroyAllWindows()

