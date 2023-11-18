## 1D array 取值
import numpy as np #匯入numpy 套件

a=np.arange(12)*10 #np.arrange(x) 產生從0開始以1為間隔，小於x的正整數數列
print('a=', a,'\n') #'\n'：換行
print('a[0:4]=', a[0:4],'\n')
print('a[0:8:2]=', a[0:8:2],'\n')
print('a[[1,3,5]]=', a[[1,3,5]],'\n')

b= a.copy()
b[5:7]=-99
print('b[5:7]=-99')
print(b,'\n')

c= a.copy()
c[[1,3,5]]=44
print('c[[1,3,5]]=44')
print(c,'\n')

d= a.copy()
d[[1,3,5]]= [111,222,333]
print('d[[1,3,5]]= [111,222,333]')
print(d,'\n')