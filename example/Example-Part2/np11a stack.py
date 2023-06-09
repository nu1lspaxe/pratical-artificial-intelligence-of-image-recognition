## h/v/d stacks (堆疊)
import numpy as np #匯入numpy 套件

a= np.array([[0,1,2],[3,4,5]])
b= np.array([[2,2,2],[4,4,4]])

c= np.hstack((a,b)) #水平堆疊
print('np.hstack(a,b)=\n',c, c.shape, '\n')

c2= np.hstack((a,b,a)) #水平堆疊
print('np.hstack(a,b,a)=\n',c2, c2.shape, '\n')

d= np.vstack((a,b)) #垂直堆疊
print('np.vstack(a,b)=\n',d, d.shape, '\n')

e= np.dstack((a,b)) #層厚(3D)堆疊
print('np.dstack(a,b)=\n',e, e.shape, '\n')







