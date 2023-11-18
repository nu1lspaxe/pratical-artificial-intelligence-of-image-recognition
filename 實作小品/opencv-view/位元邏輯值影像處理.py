import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('data/s.jpg', 0)
height, width = img1.shape

# 建立與img1大小相同的黑白二值遮罩
img2 = np.zeros((height, width), np.uint8)
img2[100:200, 100:300] =255 # 局部填入白色
img3 = np.hstack((img1, img2)) # 兩圖並排
plt.imshow(img3, cmap = 'gray'), plt.title('img1/img2')
plt.xticks([]), plt.yticks([])
plt.show()

# 邏輯運算
img4 = cv2.bitwise_and(img1, img2) # AND
img5 = cv2.bitwise_or(img1, img2) # OR
img6 = cv2.bitwise_not(img1) # NOT
img7 = np.hstack((img4, img5, img6)) # 三圖並排
plt.imshow(img7, cmap = 'gray'), plt.title('AND/OR/NOT (gray)')
plt.xticks([]), plt.yticks([])
plt.show()