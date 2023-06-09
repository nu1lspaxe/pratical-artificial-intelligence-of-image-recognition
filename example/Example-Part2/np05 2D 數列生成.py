## 2D 數列生成
import numpy as np #匯入numpy 套件

a=np.zeros((2,4))
print('np.zeros((2,4))=\n',a, a.dtype)

b=np.ones((3,3))
print('np.ones(3,3)=\n',b, b.dtype)

c= np.arange(9).reshape(3,3)
print('np.arange(9).reshape(3,3)=\n', c, c.dtype)

d=np.diagonal(c)
print('np.diagonal(c)=\n',d, d.dtype)
