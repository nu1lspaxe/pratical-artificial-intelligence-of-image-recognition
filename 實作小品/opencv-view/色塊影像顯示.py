import cv2  # 載入opencv套件
import numpy as np

## float32(ndim=2)
a1 = np.ones((200,200),'float32')
a2 = np.ones((200,200),'float32')*0.5
a3 = np.zeros((200,200),'float32')
b = np.hstack((a1,a2,a3))
cv2.imshow('float32',b) # 用imshow("視窗名稱",圖片)來顯示圖片
print(b.dtype, b.shape, b.ndim) #顯示影像讀取後的格式

## uint8(ndim=2)
c1 = np.ones((200,200),'uint8')*255
c2 = np.ones((200,200),'uint8')*128
c3 = np.zeros((200,200),'uint8')
d = np.hstack((c1,c2,c3))
cv2.imshow('uint8(gray)',d) # 用imshow("視窗名稱",圖片)來顯示圖片
print(d.dtype, d.shape, d.ndim) #顯示影像讀取後的格式

## uint8(ndim=3)
e1 = np.ones((200,200,3),'uint8')*255
e2 = np.ones((200,200,3),'uint8')*128
e3 = np.zeros((200,200,3),'uint8')
f = np.hstack((e1,e2,e3))
f[:50,:,[1,2]]=0 #保留第0通道(Blue)
f[50:100,:,[0,2]]=0 #保留第1通道(Green)
f[100:150,:,[0,1]]=0  #保留第2通道(Red)
cv2.imshow('uint8(color)',f) # 用imshow("視窗名稱",圖片)來顯示圖片
print(f.dtype, f.shape, f.ndim) #顯示影像讀取後的格式

# 用waitKey等待視窗，當按下任意鍵時繼續下一步，括弧內是等待的微秒數(1秒=1000)
cv2.waitKey()

# 關閉所有視窗
cv2.destroyAllWindows()


