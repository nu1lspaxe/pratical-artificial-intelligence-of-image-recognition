## np17: flip (翻轉)
import numpy as np
a= np.array([[0,1,2,4],[5,6,7,8]])
print(a)

b= np.fliplr(a)
print('np.fliplr(a)=\n', b)

c= np.flipud(a)
print('np.flipud(a)=\n', c)

d= np.flip(a, axis= 0)
print('np.flip(a, axis=0)=\n', d)

e= np.flip(a, axis= 1)
print('np.flip(a, axis=1)=\n', e)

## https://numpy.org/doc/stable/reference/routines.html