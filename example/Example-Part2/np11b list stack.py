## list stack

from time import sleep
import numpy as np #利用as可簡化載入所使用的名稱

## stack (堆疊)
arrays = [np.arange(12).reshape(3, 4) for x in range(6)] #生成3x4矩陣6次

print(np.stack(arrays).shape) #呈現6x3x4矩陣
print(np.stack(arrays, axis=0).shape) #6x3x4矩陣
print(np.stack(arrays, axis=1).shape) #轉換成3x6x4矩陣
sleep(2.0) #暫停兩秒
print(np.stack(arrays, axis=2).shape) #轉換成3x4x6矩陣
print(arrays)  #呈現3x4x6矩陣內容



