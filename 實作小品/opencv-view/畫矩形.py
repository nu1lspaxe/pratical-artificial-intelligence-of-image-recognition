import numpy as np
import cv2

# 建立黑影像
img = np.zeros((512,512,3), np.uint8)

# 畫矩形rectangle(影像矩陣,左上xy座標,右下xy座標,顏色(B,G,R),粗細)
cv2.rectangle(img, (100,200), (400,300), (0,255,255), 3)

# 畫矩形rectangle(影像矩陣,左上xy座標,右下xy座標,顏色(B,G,R),填滿)
cv2.rectangle(img, (100,350), (400,450), (0,0,255), -1)

#顯示圖形
cv2.imshow('img', img)

# 用waitKey等待視窗，當按下任意鍵時繼續下一步
cv2.waitKey(0)

# 關閉所有視窗
cv2.destroyAllWindows()
