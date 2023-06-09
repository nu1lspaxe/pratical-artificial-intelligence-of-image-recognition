## 1D array
import numpy as np #匯入numpy 套件

a = np.array([0,1,2,3,4,5])
print(a)
print('a.dtype=', a.dtype)
print('a.size=', a.size)
print('a.ndim=', a.ndim)
print('a.shape=', a.shape)
print('len(a)=', len(a),'\n')

print('a.clip(2,4)=', a.clip(2,4))
print('a.repeat(2)=', a.repeat(2),'\n')

print('a.mean()=', a.mean())
print('a.min()=', a.min())
print('a.max()=', a.max())
print('a.sum()=', a.sum())
print('a.std()=', a.std())