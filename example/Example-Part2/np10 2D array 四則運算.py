## 2D array 四則運算
import numpy as np #匯入numpy 套件

a= np.array([[0,1,2],[3,4,5]])
b= np.array([[2,2,2],[4,4,4]])

print('a+b=\n',a+b)
print('a.*b=\n',a*b)
print('a>b:\n',a>b)
print('a<b:\n',a<b)
print('a==b:\n',a==b)
print('a!=b:\n',a!=b, '\n')

print('np.matmul(a,b.T)=\n',np.matmul(a,b.T), '\n') #矩陣乘法
print('a@b.T:\n',a@b.T, '\n') #矩陣乘法

print('np.ravel(a)= ', np.ravel(a)) #拉直(語法1)
print('a.ravel()= ', a.ravel(), '\n') #拉直(語法2)






