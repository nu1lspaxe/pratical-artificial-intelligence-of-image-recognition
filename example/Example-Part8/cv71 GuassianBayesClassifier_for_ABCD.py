## 利用高斯貝氏分類器 (Bayesian Classifier) 辨識ABCD四種字符
import cv2
import matplotlib.pyplot as plt
import numpy as np

#顯示12字體4字元影像
img_all= cv2.imread('data/ABCD.png', 1)
plt.subplot(2,4,(1,6)) #圖框跨越((1,2),(5,6))區域，以(左上/右下)=(1,6)標示
plt.imshow(img_all)
plt.title('12 fontfaces'), plt.axis('off')

#以紅、綠、藍三色，顯示統計明度區域
for c in range(4): #ABCD四個例圖，取第一種字體
    img = img_all[0:30,c*30:(c+1)*30,:]
    img[13:19,13:19,1:3]= 0 #中央區域(紅色)
    img[20:26,13:18,[0,2]]= 0 #底部區域(綠色)
    img[10:20,21:26,0:2]= 0 #右方區域(藍色)
    if c<2:
        plt.subplot(2,4,c+3)
    else:
        plt.subplot(2,4,c+5)
    plt.imshow(img), plt.title('3 RIOs (p)')

plt.show()

# 載入所有子影像並計算每一類的統計特徵值 p
p = np.zeros((12,4,3),'float32')
img_all_gray= cv2.cvtColor(img_all, cv2.COLOR_BGR2GRAY) #轉換成灰階影像

for k in range(12):
    for c in range(4):
        img = img_all[k*30:(k+1)*30,c*30:(c+1)*30] #取子影像
        p[k,c,0] = img[13:19,13:19].mean() #中央區域(紅色)平均明度
        p[k,c,1] = img[20:26,13:18].mean() #底部區域(綠色)平均明度
        p[k,c,2] = img[10:20,21:24].mean() #右方區域(藍色)平均明度

pA= np.squeeze(p[:,0,:]) #將字母A的特徵值壓成2維(12x3)
pB= np.squeeze(p[:,1,:]) #將字母B的特徵值壓成2維(12x3)
pC= np.squeeze(p[:,2,:]) #將字母C的特徵值壓成2維(12x3)
pD= np.squeeze(p[:,3,:]) #將字母D的特徵值壓成2維(12x3)

p_list= np.vstack((pA,pB,pC,pD)) #將ABCD四個字母的特徵排成(48x3)
dA= np.zeros(len(p_list),'float32') #字母A的分類結果
dB= np.zeros(len(p_list),'float32') #字母B的分類結果
dC= np.zeros(len(p_list),'float32') #字母C的分類結果
dD= np.zeros(len(p_list),'float32') #字母D的分類結果

##高斯貝氏分類
for i in range(len(p_list)):
    t = p_list[i,:] #依序讀取第i個子圖的3個特徵值
    #第i個子的特徵，若使dA[i],dB[i],dC[i],dD[i]中，dB[i]的數值最高，則分類結果為字母'B'
    #det()行列式，cov()共變異數矩陣，mean()平均值，@矩陣乘法，inv()反矩陣，T矩陣轉置
    dA[i] = (-1./2)*np.log(np.linalg.det(np.cov(pA.T)))-(1./2)*(t - np.mean(pA, axis=0)).T @ np.linalg.inv(np.cov(pA.T)) @ (t - np.mean(pA,axis=0)).T
    dB[i] = (-1./2)*np.log(np.linalg.det(np.cov(pB.T)))-(1./2)*(t - np.mean(pB, axis=0)).T @ np.linalg.inv(np.cov(pB.T)) @ (t - np.mean(pB,axis=0)).T
    dC[i] = (-1./2)*np.log(np.linalg.det(np.cov(pC.T)))-(1./2)*(t - np.mean(pC, axis=0)).T @ np.linalg.inv(np.cov(pC.T)) @ (t - np.mean(pC,axis=0)).T
    dD[i] = (-1./2)*np.log(np.linalg.det(np.cov(pD.T)))-(1./2)*(t - np.mean(pD, axis=0)).T @ np.linalg.inv(np.cov(pD.T)) @ (t - np.mean(pD,axis=0)).T

##評估結果
d_list= np.vstack((dA,dB,dC,dD)) #將ABCD四個字母的分類指標排成48x4陣列
prediction= np.chararray((12,4), unicode= True) #存放評估結果的文字陣列

idx= np.argmax(d_list, axis=0).reshape(4,12).T #取每一欄最大值的位置，再轉置成4x12
#print(idx)

str1="ABCD"
counter= 0 #用於計算辨識正確的個數
for k in range(12):
    for c in range(4):
        if idx[k,c] == c: #如果辨識正確
            counter += 1 #counter 加 1
        prediction[k,c]= str1[idx[k,c]] #將辨識的字母存入陣列相應的位置

print('prediction:')
print(prediction) #顯示辨識結果(應該0,1,2,3欄分別是A,B,C,D)

print('\n%.1f%% match!\n' % (100*counter/(4*12))) #顯示辨識正確率
