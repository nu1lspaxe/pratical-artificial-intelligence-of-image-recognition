## 2D array format
import numpy as np #匯入numpy 套件

a=np.array([[11,22,33],[44,55,66]])
print('n-dimensions = ', a.ndim)
print('shape = ', a.shape)
print('size = ', a.size)
print('dtype = ', a.dtype) # 預設整數格式為 int32 (32bit)

b=np.array([[1.0,2.1,3.1],[4.2,5.3,6.8]])
print('dtype = ', b.dtype) # 預設浮點數格式為 float64 (64bit)

c=np.array([[1.0,2.1,3.1],[4.2,5.3,6.8]], dtype=np.float32) # 設浮點數格式為 float32
print('dtype = ', c.dtype)

d=np.array([[1,2,3],[4,5,6]], dtype=np.uint8)
print('dtype = ', d.dtype) # 預設整數格式為uint8 (8位元正整數, 8-bit unsigned integer)

