import numpy as np

a= np.array([0,2,4,8])
b= a[::-1] #反序
print(a)
print(b)

## 以下6行錯誤: python 的 range() 只能用整數
# counter= 0
# c=np.zeros((1,10),'float32')
# for x in range(0,1,0.1):
#     c[0,counter]=x
#     counter+=1
# print(c)

print('\n產生float序列:')
counter= 0
d=np.zeros((1,10),'float32')
for x in np.arange(0,1,0.1):
    d[0,counter]= x
    counter+=1
print(d)

  