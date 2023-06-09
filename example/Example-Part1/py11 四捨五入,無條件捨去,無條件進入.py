# 四捨五入,無條件捨去,無條件進入
from math import *
x = 1.55
y = -1.55
print(abs(y))         #絕對值
print(round(x))       #四捨五入
print(round(y))       #四捨五入
print(round(x, 1))   #針對小數點第一位 四捨五入
print(round(y, 1))    #針對小數點第一位 四捨五入
print(floor(x))  #低於x中的最大整數,無條件捨去
print(floor(y))  #低於y中的最大整數,無條件捨去
print(ceil(x))   #高於x中的最小整數,無條件進入
print(ceil(y))   #高於y中的最小整數,無條件進入