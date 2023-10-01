## 2D array transpose
import numpy as np #匯入numpy 套件

a=np.arange(12).reshape(3,4) # 二維陣列
print('a=',a,'\n')
print('np.max(a)=',np.max(a)) #整個array的最大值
print('np.max(a, axis = 0)=',np.max(a, axis = 0)) #對array的第一維分別取最大值
print('np.max(a, axis = 1)=',np.max(a, axis = 1)) #對array的第二維分別取最大值

print('np.min(a)=',np.min(a)) #整個array的最小值
print('np.mean(a)=',np.mean(a)) #整個array的平均值
print('np.sum(a)=',np.sum(a)) #整個array的總和

b = np.transpose(a)
print('b= np.transpose(a)\n',b,'\n')

c = a.T
print('c= a.T\n',c,'\n')

