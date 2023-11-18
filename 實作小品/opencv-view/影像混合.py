import cv2
import numpy as np

#讀入兩幅影像
img1 = cv2.imread('data/s.jpg')
img2 = cv2.imread('data/ntust.jpg')

#顯示BGR三通道的平均值與標準差
print('BGR三通道的平均值與標準差=')
print(np.around(cv2.meanStdDev(img2),1))


size = img1.shape #影像1的尺寸
img2 = cv2.resize(img2, (size[1], size[0])) #將影像2的大小調成跟影像1相同

#mix = img1 + img2 #不行，超過255會從0開始
#mix = cv2.add(img1, img2) #直接疊加，超過255即為255
mix = cv2.addWeighted(img1, 0.5, img2, 0.5, 0) #加權疊加

dst = np.hstack((img1, img2, mix)) # 水平拼貼
# dst = np.vstack((img1, img2, mix)) # 垂直拼貼
cv2.imshow('img1-> img2 -> mix', dst) # 顯示加權混合後的影像
cv2.waitKey(0) # 等待任意鍵離開
cv2.destroyAllWindows()
