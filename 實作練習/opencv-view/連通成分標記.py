import cv2
import numpy as np
  
# 輸入影像
img = cv2.imread('data/coins.png')
  
# 轉換成灰階格式
gray_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
  
# 7x7 高斯模糊
blurred = cv2.GaussianBlur(gray_img, (7, 7), 0)
print(blurred.shape, blurred.dtype)
  
# 大津(Otsu)二值化
#ret, threshold = cv2.threshold(blurred, None, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
threshold = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
cv2.imshow("threshold", threshold) #顯示二值化影像

# 二值影像連通成分分析
analysis = cv2.connectedComponentsWithStats(threshold, #二值影像
                                            connectivity=8, #連通方式: 4或8鄰接連
                                            ltype=cv2.CV_32S) #輸出資料格式
#分析結果:(區域數量,編號,邊界框座標,中心點)
(totalLabels, label_ids, values, centroid) = analysis
  
# 輸出影像初始化
output = np.zeros(gray_img.shape, dtype="uint8")
  
# 繪製每個區域的圖框，並將區域以不同明度疊加至輸出圖
for i in range(1, totalLabels):
    
    area = values[i, cv2.CC_STAT_AREA] #第i個區域的面積
      
    if (area > 40) and (area < 5000): #過濾面積適中的區域
        new_img = img.copy()
          
        # 讀取第i個區域邊界框的左上角(x,y)座標，以及(高,寬)
        x1 = values[i, cv2.CC_STAT_LEFT]
        y1 = values[i, cv2.CC_STAT_TOP]
        w = values[i, cv2.CC_STAT_WIDTH]
        h = values[i, cv2.CC_STAT_HEIGHT]
          
        pt1 = (x1, y1) #邊界框的左上角(x,y)座標
        pt2 = (x1+ w, y1+ h) #邊界框的右下角(x,y)座標
        (X, Y) = centroid[i]  #邊界框的中心點(x,y)座標
          
        # 繪製綠色矩形框
        cv2.rectangle(new_img, pt1, pt2, (0, 255, 0), 3)
        # 繪製紅色中心點(實心圓，半徑4px)
        cv2.circle(new_img, (int(X), int(Y)), 4, (0, 0, 255), -1)
  
        # 建立第i區域的圖像遮罩，根據i的大小決定明度
        componentMask = (label_ids == i).astype("uint8") * int(i*255./totalLabels)
  
        # 用 bitwise_or，將遮罩疊加至輸出影像
        output = cv2.bitwise_or(output , componentMask)
          
        # 顯示結果
        cv2.imshow("Image", new_img)
        cv2.imshow("Filtered Components", output)
        cv2.waitKey(0) # 等待任意鍵
        cv2.destroyWindow("Image") # 關閉視窗
        cv2.destroyWindow("Filtered Components") # 關閉視窗

cv2.destroyWindow("threshold") # 關閉視窗