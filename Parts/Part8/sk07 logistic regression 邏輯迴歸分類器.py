# sk07: 邏輯迴歸(Logistic Regression)作為分類器(classifier)
import numpy as np
import matplotlib.pyplot as plt

#讀取csv檔的資料，用','分欄，忽略第一列(row)
data = np.genfromtxt("data/Social_Network_Ads.csv",
                    delimiter=",", skip_header=1) 
x = data[:,[2,3]] #將第2,3欄「年齡」與「收入」資料當作x
y = data[:,4] #將第4欄「購買」當作y

# Feature Scaling (資料清理)
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler() #資料標準化（減去平均值，再除以標準差）
x = sc_x.fit_transform(x)

#資料的75%當作訓練組，25%當作測試組，以均勻挑選方式拆分(random_state=0)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0) #建立邏輯迴歸分類器
classifier.fit(x_train, y_train) # 對訓練組資料作邏輯迴歸分類

# 測試資料的分類預測
y_pred = classifier.predict(x_test)

# 建立混淆矩陣 (Confusion Matrix)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print('confusion_matrix (混淆矩陣)')
print(cm)

# 顯示訓練結果
plt.subplot(1,2,1)
from matplotlib.colors import ListedColormap
x_set, y_set = x_train, y_train
# 建立特徵圖二維座標資料，x1與x2分別是第一維(第一特徵)與第二維(第二特徵)的座標資料，範圍根據每維度x_set特徵數據的最小與最大值，間距0.01
x1, x2 = np.meshgrid(np.arange(start = x_set[:, 0].min()-1, stop = x_set[:, 0].max()+1, step = 0.01),np.arange(start = x_set[:, 1].min()-1, stop = x_set[:, 1].max()+1, step = 0.01))
# 分別帶入特徵圖的x1與x2二維座標。如果分類器辨識為第0類，該座標位置顯示紅色；如果分類器辨識為第1類，該座標位置顯示綠色。
plt.contourf(x1, x2, classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape), alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(x1.min(), x1.max()) #根據x1的數值範圍，限制特徵圖水平方向的範圍
plt.ylim(x2.min(), x2.max()) #根據x2的數值範圍，限制特徵圖垂直方向的範圍
#依序對每個訓練樣本繪製一個點，如果該樣本被分為第0類，顯示橘圓，如果是第1類，則顯示藍色。標記以分類數值[0,1]呈現
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1], c = ListedColormap(('orange', 'blue'))(i), label = j)
plt.title('LR Classifier (Training Set)')
plt.xlabel('Angle')
plt.ylabel('Estimated Salary')
plt.legend()
                     
# 顯示測試結果
plt.subplot(1,2,2)
from matplotlib.colors import ListedColormap
x_set, y_set = x_test, y_test
# 建立特徵圖二維座標資料，x1與x2分別是第一維與第二維的座標資料，範圍根據每維度x_set特徵數據的最小與最大值，間距0.01
x1, x2 = np.meshgrid(np.arange(start = x_set[:, 0].min()-1, stop = x_set[:, 0].max()+1, step = 0.01), np.arange(start = x_set[:, 1].min()-1, stop = x_set[:, 1].max()+1, step = 0.01))
# 分別帶入特徵圖的x1與x2二維座標。如果分類器辨識為第0類，該座標位置顯示紅色；如果分類器辨識為第1類，該座標位置顯示綠色。
plt.contourf(x1, x2, classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape), alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(x1.min(), x1.max()) #根據x1的數值範圍，限制特徵圖水平方向的範圍
plt.ylim(x2.min(), x2.max()) #根據x2的數值範圍，限制特徵圖垂直方向的範圍
#依序對每個訓練樣本繪製一個點，如果該樣本被分為第0類，顯示橘圓，如果是第1類，則顯示藍色。標記以分類數值[0,1]呈現
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1], c = ListedColormap(('orange', 'blue'))(i), label = j)
plt.title('LR Classifier (Test Set)')
plt.xlabel('Angle')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()
