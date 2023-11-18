## v/h split 拆分

import numpy as np #利用as可簡化載入所使用的名稱

## split (均分)
a = np.arange(12).reshape(3,4)
print('a=\n',a,'\n')
[b, c]=np.hsplit(a, 2); #水平方向平均分二分
print('[b, c]= np.hsplit(a,2)\n')
print('b=',b,'\n')
print('c=',c,'\n')

[d, e, f]=np.vsplit(a, 3); #垂直方向平均分二分
print('[d, e, f]= np.vsplit(a,3)\n')
print('d=',d,'\n')
print('e=',e,'\n')
print('f=',f,'\n')