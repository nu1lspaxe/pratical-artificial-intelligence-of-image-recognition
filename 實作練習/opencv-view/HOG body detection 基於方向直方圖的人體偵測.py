import cv2
import numpy as np
filename = 'data/people3.jpg'
src = cv2.imread(filename)
cv2.namedWindow('people')
cv2.imshow('people',src)

# HOG 特徵描述子
hog = cv2.HOGDescriptor()
# 創建 SVM 檢測器
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# 檢測行人
(rects, weights) = hog.detectMultiScale(src,
                                        winStride=(4, 4),
                                        padding=(8, 8),
                                        scale=1.25,
                                        useMeanshiftGrouping=False)

cv2.namedWindow('results')
for (x,y,w,h) in rects:
    cv2.rectangle(src, (x,y), (x+w,y+h), (0,255,0),2)

cv2.imshow('results',src)
cv2.waitKey()
cv2.destroyAllWindows()