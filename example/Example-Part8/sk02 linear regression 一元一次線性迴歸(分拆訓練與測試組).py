# sk02: simple linear regression 一元一次線性迴歸(分拆訓練與測試組)
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#建立x,y數據: y = 0.5*x + 9 + random noise
x= np.arange(0,100,2).reshape(-1,1)
y= 0.5*x + 9
y= y+ 6*(np.random.rand(x.shape[0],1)-0.5) #對y加入[-3 3]之間的隨機數(random noise)

#將50筆x,y資料，67%分為訓練組，33%分為測試組，以均勻挑選方式拆分(random_state=0)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.33, random_state = 0)
print('x_train.shape = ', x_train.shape)
print('x_test.shape = ', x_test.shape)
model = LinearRegression().fit(x_train, y_train) #用訓練集建立線性迴歸模型
plt.subplot(1,2,1) # 以下繪圖放在子圖1
plt.scatter(x_train, y_train, c='green') # 繪製訓練集的xy散布圖
y_train_pred = model.predict(x_train) # 訓練組y的估計值
plt.plot(x_train, y_train_pred, color='blue') #繪製迴歸曲線
r2_train = model.score(x_train, y_train) # 計算訓練組的決定係數(r2)。數值1代表0誤差，誤差越大，r2數值越接近0

print('y = a*x + b')
print('coefficient of determination 決定係數 (r2)= %f' %(r2_train))
print('coefficient 係數 (a)= %f\nintercept 截距 (b)= %f' %(model.coef_, model.intercept_))

plt.title('y=ax+b (training data)',fontsize=16)
plt.xlabel('x',fontsize=16), plt.ylabel('y',fontsize=16)
plt.text(0.5,0.9*y[-1],'r2= '+str(np.round(r2_train,4)), fontsize=14) # 決定係數(r2)
plt.text(0.5,0.85*y[-1],'a= '+str(np.round(model.coef_[0,0],3)), fontsize=14) # 變數x的迴歸係數
plt.text(0.5,0.8*y[-1],'b= '+str(np.round(model.intercept_[0],3)), fontsize=14) # 截距

plt.subplot(1,2,2) # 以下繪圖放在子圖2
plt.plot(x_train, model.predict(x_train), color='blue') #繪製迴歸曲線
plt.scatter(x_test, y_test, c='red') # 繪製測試集的xy散布圖
r2_test = model.score(x_test, y_test) # 計算測試組的決定係數(r2)。數值1代表0誤差，誤差越大，R^2數值越接近0
plt.title('y=ax+b (test data)',fontsize=16)
plt.xlabel('x',fontsize=16), plt.ylabel('y',fontsize=16)
plt.text(0.5,0.9*y[-1],'r2= '+str(np.round(r2_test,4)), fontsize=14) # 決定係數(r2)
plt.show() #顯示所有繪圖

## https://realpython.com/linear-regression-in-python/#simple-linear-regression