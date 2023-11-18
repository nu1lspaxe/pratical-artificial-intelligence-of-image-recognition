import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x= np.array([0,1,2,3,4,5,6,7,8,9]).reshape(-1,1) # x原本是一維資料，reshape把數值轉成(10,1)尺寸
print(x.shape)

y= np.array([0,2,4,6,8,10,12,14,16,18]).reshape(-1,1) # y原本是一維資料，reshape把數值轉成(10,1)尺寸
# y= 2*x＋noise
y= y+ 2*(np.random.rand(10,1)-0.5) #對y加入[-1 1]之間的隨機數(noise)
plt.scatter(x, y, c='red') # 繪製xy散布圖
model = LinearRegression().fit(x, y) #簡單線性迴歸
r2 = model.score(x, y) # 決定係數(r2)：數值1代表0誤差，誤差越大，r2數值越接近0
y_pred = model.predict(x) # y的估計值

print('y = a*x + b')
print('coefficient of determination 決定係數 (r2)= %f' %(r2))
print('coefficient 變數x的係數 (a)= %f' %(model.coef_))
print('intercept 截距 (b)= %f' %(model.intercept_))

plt.plot(x, y_pred, color='blue')
plt.title('y=ax+b',fontsize=16)
plt.xlabel('x',fontsize=16), plt.ylabel('y',fontsize=16)
plt.text(0.5,0.9*y[-1],'r2= '+str(np.round(r2,3)), fontsize=14) # 決定係數
plt.text(0.5,0.83*y[-1],'a= '+str(np.round(model.coef_[0,0],3)), fontsize=14) # x的係數
plt.text(0.5,0.76*y[-1],'b= '+str(np.round(model.intercept_[0],3)), fontsize=14) # 截距

plt.show()



## https://realpython.com/linear-regression-in-python/#simple-linear-regression