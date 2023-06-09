## 2D array
import numpy as np #匯入numpy 套件

a = np.array([[0,1,2],[3,4,5]])
print(a)
print('a.dtype=', a.dtype)
print('a.size=', a.size)
print('a.ndim=', a.ndim)
print('a.shape=', a.shape)
print('len(a)=', len(a),'\n')

print('a.clip(2,4)=', a.clip(2,4))
print('a.repeat(2)=', a.repeat(2),'\n')

print('a.mean()=', a.mean())
print('a.mean(axis = 0)=', a.mean(axis = 0))
print('a.mean(axis = 1)=', a.mean(axis = 1),'\n')

print('a.min()=', a.min())
print('a.min(axis = 0)=', a.min(axis = 0))
print('a.min(axis = 1)=', a.min(axis = 1),'\n')

print('a.max()=', a.max())
print('a.max(axis = 0)=', a.max(axis = 0))
print('a.max(axis = 1)=', a.max(axis = 1),'\n')

print('a.sum()=', a.sum())
print('a.sum(axis = 0)=', a.sum(axis = 0))
print('a.sum(axis = 1)=', a.sum(axis = 1))
