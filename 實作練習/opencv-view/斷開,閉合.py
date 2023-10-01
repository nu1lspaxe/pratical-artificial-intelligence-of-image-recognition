import cv2
import numpy as np

src = cv2.imread('data/taipei.jpg')

#建立一個 3x3 的結構元素（核心）
kernel = np.ones((5,5), np.uint8)
#開運算_語法：morphologyEx(輸入圖, 操作種類(開運算的話為MORPH_OPEN), 結構元素)
#先侵蝕後膨脹：先將雜訊或窄小的細線消除，再補回邊界，可以區分開物體、平滑輪廓
opening = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel)
#閉運算_語法：morphologyEx(輸入圖, 操作種類(閉運算的話為MORPH_CLOSE), 結構元素)
#閉運算=先膨脹後侵蝕：先將一些小洞或斷線補起來，再去除雜訊，可以使物體完整、平滑輪廓
closing = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel)
dst = np.hstack((src, opening, closing))
cv2.imshow('src -> opening -> closing', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

