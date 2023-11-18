## reshape
import numpy as np #匯入numpy 套件

a= np.arange(24).reshape(2,3,4)
print('np.zeros((2,3,4))=\n',a, a.shape)

b= a.reshape(6,4)
print('\nnp.zeros((6,4))=\n',b, b.shape)

c= a.reshape(4,3,2)
print('\nnp.zeros((4,3,2))=\n',c, c.shape)

d= a.reshape(24)
print('\nnp.zeros((4,3,2))=\n',d, d.shape)





