## np16: rotation (旋轉)
import numpy as np
a= np.array([[0,1,2],[3,4,5],[6,7,8]],'int16')
#一般寫 dtype = 'int16'或 dtype = np.int16 是為了閱讀上更容易了解
print(a)

b= a.T 
print('a.T=\n', b)

c= np.rot90(a, -1)
print('np.rot90(a,-1)=\n', c)

d= np.rot90(a, 1)
print('np.rot90(a, 1)=\n', d)

## https://numpy.org/doc/stable/reference/routines.html