import cv2  # 載入opencv模組
import numpy as np  # 載入numpy模組
path = "data/s.jpg"

kernel = np.array([[-1, -1, -1],[-1, 8, -1],[-1, -1, -1]]).astype("float32") #八方向 Laplacian 濾鏡

def processing(pos):
    weight = cv2.getTrackbarPos('weight', 'images') #讀取影像高斯模糊濾鏡尺寸
    thresh = cv2.getTrackbarPos('thresh', 'images') #讀取影像二值化的門檻值
    img_32F = img.astype("float32")/255   

    # 空間濾波
    Laplacian = cv2.filter2D(img_32F, -1, kernel) #使用自訂濾鏡(Laplacian 高頻(點)偵測)
    disp_Laplacian = np.clip(255*(Laplacian+0.5), 0, 255).astype("uint8") #處理範圍出界問題，轉換至8位元格式
    img_sharp = img_32F + (weight/100) * Laplacian #影像銳化
    img_sharp = np.clip(255*img_sharp, 0, 255).astype("uint8") #處理範圍出界問題，轉換至8位元格式
    Laplacian = np.clip(255*Laplacian, 0, 255).astype("uint8") #處理範圍出界問題，轉換至8位元格式
    ret, point_detection = cv2.threshold(Laplacian, thresh, 255, cv2.THRESH_BINARY) #紋理影像二值化
    dilation_points  = cv2.dilate(point_detection, np.array([[0,0,1,0,0],[0,1,1,1,0],[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0],]).astype("uint8")) #5x5點膨脹
    img_upper = np.hstack([img, img_sharp]) #左右拼圖
    img_lower = np.hstack([disp_Laplacian, dilation_points]) #左右拼圖
    output = np.vstack([img_upper, img_lower]) #上下拼圖
    output = cv2.cvtColor(output, cv2.COLOR_GRAY2BGR) #為了能上彩色的字，轉換成彩色格式

    font = cv2.FONT_HERSHEY_SIMPLEX #字體
    cv2.putText(output , "Input", (23, 33), font, 0.8, 0, 2)
    cv2.putText(output , "Input", (20, 30), font, 0.8, (0,255,255), 2)
    cv2.putText(output , "Sharpening (" + str(weight) +"%)", (523, 33), font, 0.8, 0, 2)
    cv2.putText(output , "Sharpening (" + str(weight) +"%)", (520, 30), font, 0.8, (0,255,255), 2)
    cv2.putText(output , "Laplacian", (23, 33+round(500*h/w)), font, 0.8, 0, 2)
    cv2.putText(output , "Laplacian", (20, 30+round(500*h/w)), font, 0.8, (0,255,255), 2)
    cv2.putText(output , "Point detection", (523, 33+round(500*h/w)), font, 0.8, 0, 2)
    cv2.putText(output , "Point detection", (520, 30+round(500*h/w)), font, 0.8, (0,255,255), 2)
    cv2.imshow('images', output) #顯示成果影像

print('Laplacian 高通濾波與影像銳化(自訂濾鏡)')
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) #強制以灰階格式讀取，等同參數 0
h, w = img.shape #讀取原影像尺寸
img = cv2.resize(img, (500, int(500*h/w))) #使影像寬度= 500 px
cv2.namedWindow('images')
cv2.createTrackbar('weight', 'images', 50, 100, processing) #建立模糊化滑桿
cv2.createTrackbar('thresh', 'images', 160, 255, processing) #建立二值化滑桿
processing(0) #初始化

while(1):
    k = cv2.waitKey(10) & 0xFF
    if k == 27: #如果是 Esc (ASCII 第27號)，脫離迴圈
        break
    elif k==ord('r'): #按 "r" 鍵重設滑桿數值
         cv2.setTrackbarPos('weight','images', 50)
         cv2.setTrackbarPos('thresh','images', 160)
         processing(0)     

# 關閉所有視窗
cv2.destroyAllWindows()
