## np18: tile (拼貼)
import numpy as np
a= np.array([[1,5],[2,6]])
print('a=\n', a)
b= np.tile(a, [1,2])
print('np.tile(a, [1,2])=\n', b)
c= np.tile(a, [2,3])
print('np.tile(a, [2,3])=\n', c)

## https://numpy.org/doc/stable/reference/routines.html