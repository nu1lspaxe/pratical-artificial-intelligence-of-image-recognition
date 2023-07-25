## cv01: 數值處理1
import cv2  # 載入opencv套件
import numpy as np

print("uint8(260)")
a = np.uint8([250])
b = np.uint8([10])
print( cv2.add(a, b) )   # cv2.add 高於最大範圍，等於最大值
print(a + b)      # 一般的 python 以 250+10 = 260 % 256 =餘數 4 輸出

print("\nuint8(-5)")
c = np.uint8([5])
d = np.uint8([10])
print( cv2.subtract(c, d) )   # cv2.subtract 低於最小範圍，等於最小值
print(c - d)      # 一般的 python 以 5-10 = -5 % 256 = 餘數 251 輸出

print("\n5*10")
print(cv2.multiply(c, d))

print("\n5/10")
print(cv2.divide(c, d))  # 由於 c 與 d 的 dtype 是 uint8, 5除以10 的結果是 0

print("\n10/5")
print(cv2.divide(d, c)) 


