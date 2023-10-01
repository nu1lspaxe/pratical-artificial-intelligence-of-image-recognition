import numpy as np
import cv2

# 建立黑影像
img = np.zeros((512,512,3), np.uint8)

# 繪製5像素寬的黃色斜線
cv2.line(img, (0,0), (511,100), (0,255,255), 5)

# 繪製5像素寬的黃色斜線(反鋸齒處理(高斯模糊))
d = 100
cv2.line(img, (0,0+d), (511,100+d), (0,255,255), 5, cv2.LINE_AA)

#顯示圖形
cv2.imshow('img', img)

# 用waitKey等待視窗，當按下任意鍵時繼續下一步
cv2.waitKey(0)

# 關閉所有視窗
cv2.destroyAllWindows()
