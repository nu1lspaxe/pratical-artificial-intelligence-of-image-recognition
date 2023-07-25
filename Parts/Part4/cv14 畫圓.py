## cv14: 畫圓
import numpy as np
import cv2

# 建立黑影像
img = np.zeros((512,512,3), np.uint8)

# 畫圓形: circle(影像矩陣,圓心xy座標, 半徑, 顏色(B,G,R),粗細(-1填滿))
cv2.circle(img, (200,100), 63, (0,255,255), -1)
cv2.circle(img, (350,100), 63, (0,255,255), -1, cv2.LINE_AA)

# 畫橢圓形: ellipse(影像矩陣,圓心xy座標, 長短軸直徑, 旋轉角度,/
# 起始角度,結束角度,顏色(B,G,R),粗細(-1填滿))
cv2.ellipse(img, (256,256), (100,50), 30, 0, 180, (255,255,0), -1)
cv2.ellipse(img, (256,256), (100,50), 30, 0, 360, (0,255,255), 7)

#顯示圖形
cv2.imshow('img', img)

# 用waitKey等待視窗，當按下任意鍵時繼續下一步
cv2.waitKey(0)

# 關閉所有視窗
cv2.destroyAllWindows()
