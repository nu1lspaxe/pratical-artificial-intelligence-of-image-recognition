import cv2
import numpy as np

#注水填充法(Flood Fill)
def fill_image(image, x, y, t):
    copyImage = image.copy()#複製影像
    h, w = image.shape[:2] #讀取影像高寬
    mask = np.zeros([h+2, w+2], np.uint8)#新建影像  +2是函數要求
    mask[40:190, 40:180]=255
    mask = 255 - mask
    cv2.floodFill(copyImage, mask, (y,x), (0,255,255), (t,t,t), (t,t,t), cv2.FLOODFILL_FIXED_RANGE)
    #1.彩色影像, 2.注水填充僅在遮罩的黑色區域執行，3.種子點座標, 4.注水區BGR色彩, 
    #5.種子點BGR值與低門檻的BGR差異, 6.種子點BGR值與低門檻的BGR差異, 7.使用固定門檻
    return copyImage, mask

src = cv2.imread('data/s.jpg')
h, w = src.shape[:2] 
x= int(input('seed x (<' + str(h) +') = ? '))
y= int(input('seed y (<' + str(w) +') = ? '))  
t= int(input('tolerance = ? '))
dst, mask = fill_image(src, x, y, t)
dst = np.hstack((src, dst))
cv2.namedWindow('Input/FloodFill')
cv2.imshow('Input/FloodFill',dst)
cv2.namedWindow('mask')
cv2.imshow('mask',mask)
cv2.waitKey()
cv2.destroyAllWindows()