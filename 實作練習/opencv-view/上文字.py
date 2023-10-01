import cv2
import numpy as np
img = cv2.imread('data/s.jpg')
today = np.datetime64('today', 'D') #今日
print("Today: ", str(today))

font = cv2.FONT_HERSHEY_SIMPLEX #字體
#上文字 putText(影像矩陣,字串,字串左下座標,字體,放大倍率, 顏色, 粗細, 平滑化)
cv2.putText(img,str(today),(12,202), font, 1,(0,0,0), 2) #背景黑字
cv2.putText(img,str(today),(10,200), font, 1, (255,255,255), 2) #前景白字

#顯示圖形
cv2.imshow('img', img)

# 用waitKey等待視窗，當按下任意鍵時繼續下一步
cv2.waitKey(0)

# 關閉所有視窗
cv2.destroyAllWindows()
