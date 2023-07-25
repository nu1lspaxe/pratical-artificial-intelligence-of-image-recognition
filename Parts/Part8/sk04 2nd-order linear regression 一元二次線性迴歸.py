# sk04: 2nd-order linear regression 一元二次線性迴歸
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

#建立x,y數據: y = -0.2*x + 0.5*x**2 + 0.3 + 隨機雜訊
x= np.arange(0,1,0.02).reshape(-1,1) #x是[0 1]之間以0.02為間隔的50筆數列，用reshape轉換成(50,1)尺寸
y= -0.2*x + 0.5*x**2  + 0.3 #產生 y
y= y+ 0.05*(np.random.rand(x.shape[0],1)-0.5) #對y加入[-0.025 0.025]之間的隨機數
print('x.shape = ', x.shape)

## 用簡單線性迴歸(一元一次) ##
model_1 = LinearRegression().fit(x, y) #建立線性迴歸模型
plt.subplot(1,2,1) #以下繪圖放在子圖1
plt.scatter(x, y, c='red') # 繪製的xy散布圖
y_pred = model_1.predict(x) # y的估計值
plt.plot(x, y_pred, color='blue', linewidth= 3) #繪製一階迴歸曲線
model_1_r2 = model_1.score(x, y) # 決定係數(r2)。數值1代表0誤差，誤差越大，r2數值越接近0
plt.title('y=ax+b (1st-order)',fontsize=16)
plt.xlabel('x',fontsize=16), plt.ylabel('y',fontsize=16)
plt.text(0,0.55,'r2= '+str(np.round(model_1_r2,4)), fontsize=14) #決定係數
plt.text(0,0.52,'a= '+str(np.round(model_1.coef_[0,0],3)), fontsize=14) #x項迴歸係數
plt.text(0,0.49,'b= '+str(np.round(model_1.intercept_[0],3)), fontsize=14) #截距

## 用二次線性迴歸(一元二次) ##
x_poly_2 = PolynomialFeatures(degree = 2).fit_transform(x) #產生二次迴歸的x與x平方項資料[x, x**2]
model_2 = LinearRegression().fit(x_poly_2, y) #建立線性迴歸模型
plt.subplot(1,2,2) #以下繪圖放在子圖2
plt.scatter(x, y, color = 'red')  # 繪製的xy散布圖
y2_pred= model_2.predict(x_poly_2) # 二階迴歸的預測結果
plt.plot(x, y2_pred, color = 'blue', linewidth= 3)  # 繪製二階迴歸曲線
model_2_r2 = model_2.score(x_poly_2, y) # 計算訓練組的決定係數(r2)。數值1代表0誤差，誤差越大，r2數值越接近0
plt.title('y=a[1]*(x)+a[2]*(x2)+b (2nd-order)',fontsize=16)
plt.xlabel('x',fontsize=16), plt.ylabel('y',fontsize=16)
plt.text(0,0.55,'r2= '+str(np.round(model_2_r2,4)), fontsize=14) #決定係數
plt.text(0,0.52,'a[1]= '+str(np.round(model_2.coef_[0][1],3)), fontsize=14) #x項迴歸係數
plt.text(0,0.49,'a[2]= '+str(np.round(model_2.coef_[0][2],3)), fontsize=14) #x平方項迴歸係數
plt.text(0,0.46,'b= '+str(np.round(model_2.intercept_[0],3)), fontsize=14) #截距
plt.show() #顯示

## https://realpython.com/linear-regression-in-python/#simple-linear-regression