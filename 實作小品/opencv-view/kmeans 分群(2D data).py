import numpy as np
import cv2
from matplotlib import pyplot as plt

X = np.random.randint(25,50,(25,2)) #產生25~50之間的25x2數值陣列
Y = np.random.randint(60,85,(25,2)) #產生60～～85之間的25x2數值陣列
Z = np.vstack((X,Y)) #將兩者垂直合併
Z = np.float32(Z) #轉換成浮點數格式

# 定義 k-means 的收斂條件：誤差<=1.0，疊代次數<=10，只要滿足其中一個條件就結束
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# k-means 分群(分兩群,做10次,起始群心隨機)
ret,label,center=cv2.kmeans(Z,2,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

A = Z[label.ravel()==0] #A群的(x,y)座標
B = Z[label.ravel()==1] #B群的(x,y)座標

# 繪製散佈圖
plt.scatter(A[:,0],A[:,1]) # A群預設為藍色(c='b')
plt.scatter(B[:,0],B[:,1],c = 'r') # B群設定為紅色
plt.scatter(center[:,0],center[:,1],s = 80, c = 'y', marker = 's') #標記群組中心，大小80
plt.xlabel('Height'),plt.ylabel('Weight')
plt.show()