print('三元二次多項式線性迴歸，做RGB-to-LAB色彩轉換')
print('獲得3x10係數矩陣,3x1截距(常數項)')
import numpy as np
import cv2
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

## 將nx3的RGB資料前處理，成為nx10，帶有二次項與交互項的RGB資料
def high_order(RGB):
    RGB_high_order= np.ones((len(RGB),10),dtype='float32')
    RGB_high_order[:,:3]= RGB #前3項分別是R,G,B
    for i in range(len(RGB)):
        RGB_high_order[i][3]=R**2 #第4項是R平方
        RGB_high_order[i][4]=G**2 #第5項是G平方
        RGB_high_order[i][5]=B**2 #第6項是B平方
        RGB_high_order[i][6]=R*G #第7項是R*G
        RGB_high_order[i][7]=G*B #第8項是G*B
        RGB_high_order[i][8]=R*B #第9項是R*B
        RGB_high_order[i][9]=R*G*B #第10項是R*G*B
    return RGB_high_order

##生成RGB迴歸訓練輸入資料
i=0
RGB_train= np.ones((11**3,3),dtype='float32')
for R in np.arange(0,1,0.1):
    for G in np.arange(0,1,0.1):
        for B in np.arange(0,1,0.1):
            i+=1
            RGB_train[i][0]=R
            RGB_train[i][1]=G
            RGB_train[i][2]=B

#輸入資料的前處理：將nx3的RGB資料延伸成nx10的三元二次多項式資料
RGB_train_high = high_order(RGB_train)
RGB_train_3D = RGB_train.reshape(RGB_train.shape[0],1,3) #變成三維格式，以符合cvtColor()的輸入格式
LAB_train_3D = cv2.cvtColor(RGB_train_3D, cv2.COLOR_RGB2LAB) #算出LAB目標值
LAB_train = np.squeeze(LAB_train_3D) #轉回二維格式，以符合線性迴歸的格式要求

#線性迴歸
model = LinearRegression().fit(RGB_train_high, LAB_train)
r_sq = model.score(RGB_train_high, LAB_train) #算出決定係數r**2, 數值越接近1越準確
print(f"決定係數(coefficient of determination): {r_sq}")
print(f"係數矩陣(coefficients): {model.coef_}")
print(f"常數項(intercept): {model.intercept_}")

#評估L*,a*,b*個別的估計誤差
LAB_train_pred = model.predict(RGB_train_high)
plt.subplot(1,3,1)
plt.plot(LAB_train[:,0],LAB_train_pred[:,0],'.',c='r')
plt.title('L* comparison'), plt.xlabel('L*'), plt.ylabel('L* (prediction)')

plt.subplot(1,3,2)
plt.plot(LAB_train[:,1],LAB_train_pred[:,1],'.',c='g')
plt.title('a* comparison'), plt.xlabel('a*'), plt.ylabel('a* (prediction)')

plt.subplot(1,3,3)
plt.plot(LAB_train[:,2],LAB_train_pred[:,2],'.',c='b')
plt.title('b* comparison'), plt.xlabel('b*'), plt.ylabel('b* (prediction)')
plt.show()


#套用迴歸矩陣
print('輸入[0 1]之間的RGB值')
R = float(input('R=? '))
G = float(input('G=? '))
B = float(input('B=? '))
RGB_test_high = high_order(np.array([R,G,B]).reshape(1,3)) # 將數入RGB轉成多項式的輸入變數(1,10)
LAB_test_pred = model.predict(RGB_test_high) #用迴歸模型估計LAB值
print(f"CIELAB (L*,a*,b*) predict: {LAB_test_pred}") #顯示LAB估計值
