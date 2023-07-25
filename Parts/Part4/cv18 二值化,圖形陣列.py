## cv18: 影像門檻處理(thresholding)：各種處理方法
import cv2
import numpy as np
from matplotlib import pyplot as plt

option = int(input('影像: 1.灰階, 2.毛線, 3.校園 = ? '))
if option==1:
    img=np.zeros((256,256),dtype='uint8')
    for x in range (0,256):
        img[:, x] = x
elif option==2:
    img = cv2.imread('data/s.jpg', 0) #強制以灰階格式讀取影像
else:
    img = cv2.imread('data/ntust.jpg', 0) #強制以灰階格式讀取影像

#傳回值, 輸出影像 = cv2.threshold(輸入影像, 門檻值, 最大值, 門檻處理方法)
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, None, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret, thresh3 = cv2.threshold(img,127, 255, cv2.THRESH_BINARY_INV)
ret, thresh4 = cv2.threshold(img,127, 255, cv2.THRESH_TRUNC)
ret, thresh5 = cv2.threshold(img,127, 255, cv2.THRESH_TOZERO)
ret, thresh6 = cv2.threshold(img,127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','THRESH_OTSU','BINARY_INV','TRUNC','TOZERO','TOZERO_INV'] #圖標題 list
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5, thresh6] #影像 list

for i in range(0,7):  #0~6迴圈
    plt.subplot(2,4,i+1)
    plt.imshow(images[i],'gray') #以灰階模式(cmap='gray')顯示
    plt.title(titles[i])#標題
    plt.xticks([]) #不顯示橫軸座標
    plt.yticks([]) #不顯示縱軸座標

plt.show() #顯示圖形陣列

