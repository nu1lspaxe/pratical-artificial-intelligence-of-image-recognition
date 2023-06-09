## 型態轉換
import numpy as np #匯入numpy 套件

a= np.pi
print('np.pi=',a)

b=np.around(a)
print('np.around(pi)=',b, b.dtype)

c=np.ceil(a)
print('np.ceil(pi)=',c, c.dtype)

d=np.floor(a)
print('np.floor(pi)=',d, d.dtype)

e = d.astype('int8')
print("d.astype('int8')=",e, e.dtype)

print('np.abs(-9)=', np.abs(-9))
print('np.sqrt(4)=', np.sqrt(4))
print('np.log(e)=', np.log(np.e))
print('np.log2(16)=', np.log2(16))
print('np.log10(100)=', np.log10(100))

f1 = np.array([1.1, 2.2, 3.3, 0, -1])
f2 = np.array(f1, dtype='?') #布林值
f3 = np.array(f1, dtype='U') #正整數
f4 = np.array(f1, dtype='i') #16位元整數
print(f1)   # [ 1.1  2.2  3.3  0.  -1. ]
print(f2)   # [ True  True  True False  True]
print(f3)   # ['1.1' '2.2' '3.3' '0.0' '-1.0']
print(f4)   # [ 1  2  3  0 -1]

