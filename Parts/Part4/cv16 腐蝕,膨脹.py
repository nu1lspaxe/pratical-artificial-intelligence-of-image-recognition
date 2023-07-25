## cv16: 影像型態學處理：腐蝕與膨脹
import cv2
import numpy as np

src = cv2.imread('data/taipei.jpg')
shape = int(input('shape: 1. squre, 2. cross, 3. round = ? '))
ksize = int(input('kernel size = ? '))
#建立一個 kxk 的結構元素（核心）
if (shape==1):
                kernel =cv2.getStructuringElement(cv2.MORPH_RECT,(ksize,ksize))
                # kernel = np.ones((15,15), np.uint8)
elif (shape==2):
                kernel =cv2.getStructuringElement(cv2.MORPH_CROSS,(ksize,ksize))
elif (shape==3):
                kernel =cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(ksize,ksize))
else:
                print('Error')
#
#侵蝕_語法：erode(輸入圖, 結構元素, 執行次數)
#消融物體的邊界；如果物體比結構元素小，則物體會消失；可用來消除雜訊
erosion = cv2.erode(src, kernel)
#膨脹_語法：dilate(輸入圖, 結構元素, 執行次數)
#擴大物體的邊界；如果兩物體間有小於結構元素的間隙，則兩物體會連接起來；可用來填補間隙
dilation = cv2.dilate(src, kernel)

dst = np.hstack((src, erosion, dilation))
cv2.imshow('src -> erosion -> dilation', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

