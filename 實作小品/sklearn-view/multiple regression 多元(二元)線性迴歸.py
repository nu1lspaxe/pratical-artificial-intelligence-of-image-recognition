import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#讀取csv檔的資料，用','分欄，忽略第一列(row)
data = np.genfromtxt("data/HeightAgeWeight_data.csv",
                    delimiter=",", skip_header=1) 

x = data[:,[1,2]] #將第1,2欄「身高」與「年齡」資料當作x
y = data[:,3].reshape(-1, 1) #將第3欄「體重」當作y
print('x.shape = ', x.shape)

## model_1: 僅用「身高」預測「體重」##
plt.subplot(1,3,1)
model_1 = LinearRegression().fit(x[:,0].reshape(-1,1), y) #建立一元線性迴歸模型
y1_pred = model_1.predict(x[:,0].reshape(-1,1)) # x套用迴歸模型獲得的y的估計值
plt.scatter(x[:,0], y, c='blue') # 繪製的xy散布圖
r2 = model_1.score(x[:,0].reshape(-1,1), y) # 決定係數(r2)。數值1代表0誤差，誤差越大，r2數值越接近0
plt.title('y=a(x[0])+b',fontsize=16)
plt.xlabel('x[0] (Height)',fontsize=16)
plt.ylabel('y (Weight)',fontsize=16)
plt.text(90,71,'r2= '+str(np.round(r2,4)), fontsize=14)
plt.text(90,69,'a= '+str(np.round(model_1.coef_[0,0],3))+' (Height)', fontsize=14)
plt.text(90,67,'b= '+str(np.round(model_1.intercept_[0],3)), fontsize=14)

## model_2: 僅用「年齡」預測「體重」##
plt.subplot(1,3,2)
model_2 = LinearRegression().fit(x[:,1].reshape(-1,1), y) #建立一元線性迴歸模型
y2_pred = model_2.predict(x[:,1].reshape(-1,1)) # x套用迴歸模型獲得的y的估計值
plt.scatter(x[:,1], y, c='blue') # 繪製的xy散布圖
r2 = model_2.score(x[:,1].reshape(-1,1), y) # 決定係數(r2)。數值1代表0誤差，誤差越大，r2數值越接近0
plt.title('y=a(x[1])+b',fontsize=16)
plt.xlabel('x[1] (Age)',fontsize=16)
plt.ylabel('y (Weight)',fontsize=16)
plt.text(11,70,'r2= '+str(np.round(r2,4)), fontsize=14)
plt.text(11,68,'a= '+str(np.round(model_2.coef_[0,0],3))+' (Age)', fontsize=14)
plt.text(11,66,'b= '+str(np.round(model_2.intercept_[0],3)), fontsize=14)

## model_3: 用「身高」與「年齡」預測「體重」##
plt.subplot(1,3,3)
model_3 = LinearRegression().fit(x, y) #建立多元(二元)線性迴歸模型
y_pred = model_3.predict(x) # x套用迴歸模型獲得的y的估計值
plt.plot([45, 75], [45, 75], color='blue') #45度直線
plt.scatter(y, y_pred, c='green') # 繪製預測準確度的散布圖
r2 = model_3.score(x, y) # 決定係數(r2)。數值1代表0誤差，誤差越大，r2數值越接近0

print('y=a(x[0])+b(x[1])+c')
print('coefficient of determination 決定係數 (r2)= %f' %(r2))
print('coefficient 係數 (a) = %f' %(model_3.coef_[0,0]))
print('coefficient 係數 (b) = %f' %(model_3.coef_[0,1]))
print('intercept 截距 (b)= %f' %(model_3.intercept_))

plt.title('y=a(x[0])+b(x[1])+c',fontsize=16)
plt.xlabel('y (Weight)',fontsize=16)
plt.ylabel('y_pred (Weight)',fontsize=16)
plt.text(45,72,'r2= '+str(np.round(r2,4)), fontsize=14)
plt.text(45,69,'a= '+str(np.round(model_3.coef_[0,0],3))+' (Height)', fontsize=14)
plt.text(45,66,'b= '+str(np.round(model_3.coef_[0,1],3))+' (Age)', fontsize=14)
plt.text(45,63,'c= '+str(np.round(model_3.intercept_[0],3)), fontsize=14)
plt.show()


## https://realpython.com/linear-regression-in-python/#simple-linear-regression