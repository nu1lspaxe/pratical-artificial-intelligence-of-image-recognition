import numpy as np
import cv2
img = cv2.imread('data/s.jpg')
img = cv2.blur(img,(5,5)) #平滑化
Z = img.reshape((-1,3)) #將影像降成2維資料
Z = np.float32(Z) #轉換成浮點數格式

# 定義 k-means 的收斂條件：誤差<=1.0，疊代次數<=10，只要滿足其中一個條件就結束
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

K=int(input('K (3~10)= ? ')) #輸入色彩分群數K

# k-means 分群(分K群,做10次,起始群心隨機)
ret,label,center = cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

center = np.uint8(center) #將群組中心轉回uint8
res = center[label.flatten()] #忽略維度，將每個像素的BGR值，替換成所屬群組的中心BGR值
res2 = res.reshape((img.shape)) #將影像轉回三維
cv2.imshow('res2',res2) #顯示色彩分群結果
cv2.waitKey(0)
cv2.destroyAllWindows()