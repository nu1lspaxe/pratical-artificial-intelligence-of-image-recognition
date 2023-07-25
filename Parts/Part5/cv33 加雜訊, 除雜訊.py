'''cv33: 加雜訊(高斯/胡椒鹽), 除雜訊(均值/中值濾波)'''
import random # 載入random模組
import cv2  # 載入opencv模組
import numpy as np  # 載入numpy模組
path = "data/s.jpg"

def addGaussianNoise(image, sigma): ##將影像加上高斯雜訊
    noise = np.random.normal(0, sigma, (h,w,3)) #產生標準差為sigma，平均值為0的高斯分配隨機數
    noisy_img = np.clip(image + noise, 0, 255).astype("uint8") #將雜訊加入影像，並轉換至8位元格式
    return noisy_img #傳回含雜訊的影像

def addSaltPepperNoise(image, noise_rate): ##將影像加上胡椒鹽雜訊
    noisy_img = image.copy()
    for x in range(0, h):
        for y in range(0, w):
            for ch in range(0,3):
                if random.random() < noise_rate: # noise_ratio 的有效範圍是[0 1]
                    if random.random() < 0.5: #被隨機調選的像素，隨機給定極端值(0或255)
                        noisy_img[x,y,ch] = 0 #加入胡椒雜訊
                    else:
                        noisy_img[x,y,ch] = 255 #加入鹽雜訊
    return noisy_img #傳回含雜訊的影像

def denoising(pos): ##調整雜訊濃度與濾鏡大小
    ## 加雜訊
    noise_level = cv2.getTrackbarPos("noise","images") #讀取雜訊滑桿數值
    if (option == 1): ##加入高斯雜訊
        noisy_img = addGaussianNoise(img, noise_level)
    else:  ##加入胡椒鹽雜訊
        noisy_img = addSaltPepperNoise(img, noise_level/100)

    ## 除雜訊
    ksize = 2*cv2.getTrackbarPos("ksize","images")+1 #讀取雜訊滑桿數值
    meanBlur_img = cv2.blur(noisy_img, (ksize, ksize)) #均值濾波
    medianBlur_img = cv2.medianBlur(noisy_img, ksize) #中值濾波
    
    font = cv2.FONT_HERSHEY_SIMPLEX #字體
    if option==1:
        cv2.putText(noisy_img , "Gaussian noise  (sigma = " + str(noise_level) + ")", (23,33), font, 0.8, 0, 2)
        cv2.putText(noisy_img , "Gaussian noise  (sigma = " + str(noise_level) + ")", (20,30), font, 0.8, (0,255,255), 2)
    else:
        cv2.putText(noisy_img , "Salt and pepper noise  (" + str(noise_level) + "%)", (23,33), font, 0.8, 0, 2)
        cv2.putText(noisy_img , "Salt and pepper noise  (" + str(noise_level) + "%)", (20,30), font, 0.8, (0,255,255), 2)
    cv2.putText(meanBlur_img , "meanBlur (" + str(ksize) +"x" + str(ksize) + ")", (23,33), font, 0.8, 0, 2)
    cv2.putText(meanBlur_img , "meanBlur (" + str(ksize) +"x" + str(ksize) + ")", (20,30), font, 0.8, (0,255,255), 2)
    cv2.putText(medianBlur_img , "medianBlur (" + str(ksize) +"x" + str(ksize) + ")", (23,33), font, 0.8, 0, 2)
    cv2.putText(medianBlur_img , "medianBlur (" + str(ksize) +"x" + str(ksize) + ")", (20,30), font, 0.8, (0,255,255), 2)
    output = np.hstack([noisy_img, meanBlur_img, medianBlur_img])    
    cv2.imshow("images", output)

## 主程式起始處
print("影像加雜訊, 除雜訊(均值/中值濾波)：按 Esc 離開")
option = int(input("加雜訊: 1.高斯, 2.胡椒鹽 =? "))
img = cv2.imread(path,cv2.IMREAD_COLOR) #強制以彩色格式讀取，等同參數 1
h, w = img.shape[:2] #讀取原影像尺寸
img = cv2.resize(img, (500, int(500*h/w))) #使影像寬度= 500 px
h, w = img.shape[:2] #讀取原影像尺寸
cv2.namedWindow("images")
cv2.createTrackbar("noise", "images", 10, 20, denoising) #建立雜訊滑桿
cv2.createTrackbar("ksize", "images", 1, 5, denoising) #建立空間濾鏡大小滑桿
denoising(0) #初始化

while (1):
    k = cv2.waitKey(10) & 0xFF
    if k == 27: #如果是 Esc (ASCII 第27號)，脫離迴圈
        break

# 關閉所有視窗
cv2.destroyAllWindows()
