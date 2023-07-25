'''cv28: 直方圖均等化(Histogram Equilization)'''
import numpy as np
import cv2
from matplotlib import pyplot as plt
font = cv2.FONT_HERSHEY_DUPLEX #字體
img = cv2.imread('data/indoor.jpg', cv2.IMREAD_GRAYSCALE) #以灰階模式開啟影像，相當於參數 0
#刻意降低輸入影像的對比
alpha = 0.5 #contrast
beta = 100 #brightness
new_img = img.copy()
cv2.convertScaleAbs(img, new_img, alpha, beta) #調整影像的對比與亮度
##for y in range(img.shape[0]):
##    for x in range(img.shape[1]):
##            new_img[y,x] = np.clip(alpha*img[y,x] + beta, 0, 255)
img_he = cv2.equalizeHist(new_img) #直方圖均等化

clahe = cv2.createCLAHE(clipLimit=10.0, tileGridSize=(4,4))  #建立對比限制自適應直方圖均等化物件
img_clahe = clahe.apply(new_img) #使用該物件處理影像
img_all = np.hstack([new_img, img_he, img_clahe])
img_all_color = cv2.cvtColor(img_all, cv2.COLOR_GRAY2BGR) #轉換成三通道的彩色影像
#img_all_color = np.stack([img_all, img_all, img_all], axis=2) #可替代上式

hight, width = img.shape
cv2.putText(img_all_color , 'Input', (14, 64), font, 1.6, 0, 2)
cv2.putText(img_all_color , 'Input', (10, 60), font, 1.6,(255,255,0), 2)
cv2.putText(img_all_color , 'Histogram Equalization (HE)', (14+width, 64), font, 1.2, 0, 2)
cv2.putText(img_all_color , 'Histogram Equalization (HE)', (10+width, 60), font, 1.2, (255,255,0), 2)
cv2.putText(img_all_color , 'Contrast-Limited Adaptive HE', (14+2*width, 64), font, 1.2, 0, 2)
cv2.putText(img_all_color , 'Contrast-Limited Adaptive HE', (10+2*width, 60), font, 1.2, (255,255,0), 2)
cv2.putText(img_all_color , 'limit=10, grid=4x4', (14+2*width, 114), font, 1,0, 2)
cv2.putText(img_all_color , 'limit=10, grid=4x4', (10+2*width, 110), font, 1, (255,255,0), 2)
plt.imshow(img_all_color) #注意: plt的色彩通道順序是RGB
plt.title("Histogram equalization (HE): A comparison")
plt.xticks([]), plt.yticks([])
if 1: #全螢幕顯示
    figManager = plt.get_current_fig_manager() 
    figManager.window.showMaximized()
plt.show() #顯示影像陣列

# 用 matplotlab 繪製灰階直方圖
fig = plt.figure() #繪製圖形陣列
fig.add_subplot(2,3,1)
plt.hist(new_img.flatten(), bins=64) #顯示以 64 個 bars 呈現灰階影像直方圖
plt.xlim([0,255]); plt.title("Input")
fig.add_subplot(2,3,2)
plt.hist(img_he.flatten(), bins=64)
plt.xlim([0,255]); plt.title("HE")
fig.add_subplot(233)
plt.hist(img_clahe.flatten(), bins=64)
plt.xlim([0,255]); plt.title("CLAHE")
fig.add_subplot(2,3,4)
plt.imshow(new_img, cmap= "gray", vmin=0, vmax=255) #要設定vmin, vmax, 否則自動根據影像內容調整範圍
plt.xticks([]), plt.yticks([])
fig.add_subplot(2,3,5)
plt.imshow(img_he, cmap= "gray", vmin=0, vmax=255)
plt.xticks([]), plt.yticks([])
fig.add_subplot(2,3,6)
plt.imshow(img_clahe, cmap= "gray", vmin=0, vmax=255)
plt.xticks([]), plt.yticks([])
if 1: #全螢幕顯示
    figManager = plt.get_current_fig_manager() 
    figManager.window.showMaximized()
plt.show()

## 比較CLAHE不同參數的效果
clahe1= cv2.createCLAHE(clipLimit=5.0, tileGridSize=(1,1))  #建立CLAHE物件
img_clahe1 = clahe1.apply(new_img) #使用該物件處理影像
clahe2= cv2.createCLAHE(clipLimit=5.0, tileGridSize=(2,2))  #建立CLAHE物件
img_clahe2 = clahe2.apply(new_img) #使用該物件處理影像
clahe3= cv2.createCLAHE(clipLimit=5.0, tileGridSize=(4,4))  #建立CLAHE物件
img_clahe3 = clahe3.apply(new_img) #使用該物件處理影像
img_row1 = np.hstack([img_clahe1, img_clahe2, img_clahe3])
clahe4= cv2.createCLAHE(clipLimit=15.0, tileGridSize=(1,1))  #建立CLAHE物件
img_clahe4 = clahe4.apply(new_img) #使用該物件處理影像
clahe5= cv2.createCLAHE(clipLimit=15.0, tileGridSize=(2,2))  #建立CLAHE物件
img_clahe5 = clahe5.apply(new_img) #使用該物件處理影像
clahe6= cv2.createCLAHE(clipLimit=15.0, tileGridSize=(4,4))  #建立CLAHE物件
img_clahe6 = clahe6.apply(new_img) #使用該物件處理影像
img_row2 = np.hstack([img_clahe4, img_clahe5, img_clahe6])
clahe7= cv2.createCLAHE(clipLimit=30.0, tileGridSize=(1,1))  #建立CLAHE物件
img_clahe7 = clahe7.apply(new_img) #使用該物件處理影像
clahe8= cv2.createCLAHE(clipLimit=30.0, tileGridSize=(2,2))  #建立CLAHE物件
img_clahe8 = clahe8.apply(new_img) #使用該物件處理影像
clahe9= cv2.createCLAHE(clipLimit=30.0, tileGridSize=(4,4))  #建立CLAHE物件
img_clahe9 = clahe9.apply(new_img) #使用該物件處理影像
img_row3 = np.hstack([img_clahe7, img_clahe8, img_clahe9])
img_all2 = np.vstack([img_row1, img_row2, img_row3])
h, w = img_all2.shape
img_all2_color = cv2.cvtColor(img_all2, cv2.COLOR_GRAY2BGR)  #轉換成三通道的彩色影像
#img_all2_color = np.stack([img_all2, img_all2, img_all2], axis=2) #可替代上式

cv2.putText(img_all2_color , 'limit=5, grid=1x1', (80, 60), font, 1.6, (255,255,0), 2)
cv2.putText(img_all2_color , 'limit=5, grid=2x2', (80+round(w/3), 60), font, 1.6,(255,255,0), 2)
cv2.putText(img_all2_color , 'limit=5, grid=4x4', (80+round(w*2/3), 60), font, 1.6, (255,255,0), 2)
cv2.putText(img_all2_color , 'limit=15, grid=1x1', (80, 60+round(h/3)), font, 1.6, (255,255,0), 2)
cv2.putText(img_all2_color , 'limit=15, grid=2x2', (80+round(w/3), 60+round(h/3)), font, 1.6,(255,255,0), 2)
cv2.putText(img_all2_color , 'limit=15, grid=4x4', (80+round(w*2/3), 60+round(h/3)), font, 1.6, (255,255,0), 2)
cv2.putText(img_all2_color , 'limit=30, grid=1x1', (80, 60+round(h*2/3)), font, 1.6, (255,255,0), 2)
cv2.putText(img_all2_color , 'limit=30, grid=2x2', (80+round(w/3), 60+round(h*2/3)), font, 1.6,(255,255,0), 2)
cv2.putText(img_all2_color , 'limit=30, grid=4x4', (80+round(w*2/3), 60+round(h*2/3)), font, 1.6, (255,255,0), 2)
plt.imshow(img_all2_color)
plt.title("Contrast-Limited Adaptive HE (CLAHE) parametric effects")
plt.xticks([]), plt.yticks([])
if 1: #全螢幕顯示
    figManager = plt.get_current_fig_manager() 
    figManager.window.showMaximized()
plt.show()
