## cv02: 數值處理2
import cv2  # 載入opencv套件
import numpy as np

a = np.array([10, 20, 30])
print(a)
b = np.array([1, 2, 3])
print(b)

print("\nadd")
print( cv2.add(a, b) )

print("\nsubtract")
print( cv2.subtract(a, b) )

print("\nmultiply")
print(cv2.multiply(a, b))

print("\ndivide")
print(cv2.divide(a, b))



