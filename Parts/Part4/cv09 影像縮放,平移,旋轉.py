## cv09: 影像縮放,平移,旋轉
import cv2
import numpy as np

img = cv2.imread('data/s.jpg')
height, width = img.shape[:-1]

#影像放大兩倍
res = cv2.resize(img, None, fx=1.5, fy=1.5)
#OR
#res = cv2.resize(img,(2*width, 2*height))

cv2.imshow('res', res)

#建立幾何變形轉換矩陣(平移)
M1 = np.float32([[1, 0, 100], [0, 1, 50]])
shift_img = cv2.warpAffine(img, M1, (width, height)) #影像幾何變形轉換
cv2.imshow('shift_img ', shift_img)

#建立幾何變形轉換矩陣(旋轉)
theta = -45.0*(np.pi/180)
M2 = np.float32([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 100]])
rotate_img  = cv2.warpAffine(img, M2, (width, height)) #影像幾何變形轉換
cv2.imshow('rotate_img', rotate_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
