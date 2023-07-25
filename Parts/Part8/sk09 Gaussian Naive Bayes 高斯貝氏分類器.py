# sk09: Gaussian Naive Bayes 高斯貝氏分類器
import numpy as np
import matplotlib.pyplot as plt

#讀取csv檔的資料，用','分欄，忽略第一列(row)
data = np.genfromtxt("data/Social_Network_Ads.csv",
                    delimiter=",", skip_header=1) 
x = data[:,[2,3]] #將第2,3欄「年齡」與「收入」資料當作x
y = data[:,4] #將第4欄「購買」當作y

#資料的75%當作訓練組，25%當作測試組，以均勻挑選方式拆分(random_state=0)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)

# Feature Scaling (資料清理)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()  #資料標準化（減去平均值，再除以標準差）
x_train = sc.fit_transform(x_train) #根據這筆資料的平均值與標準差
x_test = sc.transform(x_test) #套用fit_transform()裡用的平均值與標準差

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB() # 建立高斯貝氏分類器
classifier.fit(x_train, y_train) # 對訓練組資料作分類

##### 以下撰寫方式與sk07 邏輯迴歸分類器範例相同 ########

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
x1, x2 = np.meshgrid(np.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step = 0.01), np.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))
plt.contourf(x1, x2, classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape), alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(x1.min(), x1.max())
plt.ylim(x2.min(), x2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1], c = ListedColormap(('orange', 'blue'))(i), label = j)
plt.title('Gaussian Naive Bayes Classifier (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()

# 顯示測試結果
plt.subplot(1,2,2)
x_set, y_set = x_test, y_test
x1, x2 = np.meshgrid(np.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step = 0.01), np.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))
plt.contourf(x1, x2, classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape), alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(x1.min(), x1.max())
plt.ylim(x2.min(), x2.max())

for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1], c = ListedColormap(('orange', 'blue'))(i), label = j)
plt.title('Gaussian Naive Bayes Classifier (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()
