## concatenate (連接)
import numpy as np #匯入numpy 套件

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

print('a,b在第1維連接=\n', np.concatenate((a, b), axis=0),'\n')
print('b轉置後，在第2維連接=\n',np.concatenate((a, b.T), axis=1),'\n')
print('ab忽略維度，直接相接=\n', np.concatenate((a, b), axis=None),'\n')






