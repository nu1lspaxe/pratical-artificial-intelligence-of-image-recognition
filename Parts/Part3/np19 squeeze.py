## np19: squeeze (降維:壓縮長度1的維度)
import numpy as np
a= np.ones((1,3,4)) #三維陣列
print('a= np.ones((1,3,4))\na.shape=', a.shape)
a= np.squeeze(a, axis=0) #壓縮第一維
print('np.squeeze(a, axis=0)=\n', a, a.shape, '\n')

b= np.ones((2,1,4)) #三維陣列
print('b=np.ones((2,1,4))\nb.shape=', b.shape)
b = np.squeeze(b, axis=1) #壓縮第二維
print('np.squeeze(b, axis=1)=\n', b, b.shape, '\n')

c= np.ones((2,3,1)) #三維陣列
print('c=np.ones((2,3,1))\nc.shape=', c.shape)
c = np.squeeze(c, axis=2) #壓縮第三維
print('np.squeeze(c, axis=2)=\n', c, c.shape)

##以下的範例，自動把只有一個元素的維度壓縮
d0= np.zeros((1,2,3))
d1= np.ones((1,2,3))
d2= np.ones((1,2,3))*2
d3= np.ones((1,2,3))*3
e= np.concatenate([d0,d1,d2,d3])
print('e.shape= ', e.shape)
while 1:
    p= int(input('p = ? '))
    if (p<4) & (p>-1):
        f= np.squeeze(e[p,:,:]) #第一維作為選項，因此只有一個元素
        print('f=\n', f) #第一維被壓縮
    else:
        print('out of range')

## https://numpy.org/doc/stable/reference/routines.html