## split 拆分

import numpy as np #利用as可簡化載入所使用的名稱

## split (均分)
a = np.arange(9) #生成[0 ....8]
print(a)
[b, c, d]=np.split(a, 3); #平均分三分
print(b)
print(c)
print(d)

## split (指定數量拆分)
[e, f, g]=np.split(a, [4, 7]); #按指定數量分三分
print(e) #第一個數量(4)
print(f) #第二個減去第一個的數量(7-4=3)
print(g) #剩下的數量(9-7=2)





