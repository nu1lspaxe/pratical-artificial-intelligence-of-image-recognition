## cv04: 指定影像RGB值
import cv2  # 載入opencv套件
import numpy as np

Red = int(input('uint8 Red=? '))
Green = int(input('uint8 Green=? '))
Blue = int(input('uint8 Blue=? '))

## uint8(ndim=3)
im = np.ones((200,400,3),'uint8')
#以下三行當給定的RGB值超過[0 255]範圍會出錯
# im[:,:,0]= Blue
# im[:,:,1]= Green
# im[:,:,2]= Red
#clip的目的是避免數值超過範圍，變成輸入值除以255的餘數
im[:,:,0]= np.clip(Blue,0,255) 
im[:,:,1]= np.clip(Green,0,255)
im[:,:,2]= np.clip(Red,0,255)
cv2.imshow('uint8(color)', im) # 用imshow("視窗名稱",圖片)來顯示圖片

print('im[:2,:5,:]=\n', im[:2,:5,:])

# 用waitKey等待視窗，當按下任意鍵時繼續下一步，括弧內是等待的微秒數(1秒=1000)
cv2.waitKey()

# 關閉所有視窗
cv2.destroyAllWindows()


