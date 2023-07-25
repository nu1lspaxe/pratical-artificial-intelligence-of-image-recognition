## 1D 數列生成
import numpy as np #匯入numpy 套件

a=np.zeros(5)
print('np.zeros(5)=',a, a.dtype)

b=np.ones(5)
print('np.ones(5)=',b, b.dtype)

c=np.ones(5, dtype='int16')
print("np.ones(5, dtype='int16')=",c, c.dtype)

d= np.random.rand(5) #均勻分配的隨機數, 範圍[0 1]
d= np.around(d, 3) #小數點下三位
print('np.random.rand(5)=', d, d.dtype)

e= np.random.randn(5) #常態分配的隨機數, 平均值的期望值為0
e= np.around(e, 3) #小數點下三位
print('np.random.randn(5)=', e, e.dtype)

f= np.arange(5)
print('np.arange(5)=', f, f.dtype)

g= np.arange(2,7)
print('np.arange(2,7)=', g, g.dtype)

h= np.arange(3,12,2)
print('np.arange(3,12,2)=', h, h.dtype)

i= np.arange(12,3,-2)
print('np.arange(12,3,-2)=', i, i.dtype)