## 2D array 取值
import numpy as np #匯入numpy 套件

a=np.arange(12).reshape(3,4)
print('a=',a,'\n')
print('a[0,:]=',a[0,:])
print('a[2,:]=',a[2,:])
print('a[:,0]=',a[:,0])
print('a[:,2]=',a[:,2],'\n')

a[0:2,1:3] = -9
print('a[0:2,1:3]=-9')
print('a=',a,'\n')
