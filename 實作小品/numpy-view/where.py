## np20: where (查詢)
import numpy as np
print('用法一：符合條件的元素，以第二引數處理，其餘以第三引數處理')
a= np.array([0,1,2,3,4,5,6,7,8,9])
print('a=',a)
b= np.where(a>6, 999, 10*a) #滿足a>6的元素,輸出999,否則輸出10*a
print('np.where(a>6, 999, 10*a)=\n', b, '\n')

print('用法二：查詢符合條件的索引值與數值(一維)')
c= np.array([0,1,2,3,4,5,6,7,8,9])*10
print('c=',c)
d= np.where((c<20)|(c>60))
print('符合條件的索引值(一維座標) d=np.where((c<20)|(c>60))=\n', d)
print('符合條件的資料 c[d]=', c[d], '\n')

print('用法二：查詢符合條件的索引值與數值(二維)')
e= np.array([[0,11,22,33],[44,55,66,77]])
print('e=',e)
f= np.where((e<20)|(e>60))
print('符合條件的索引值(二維座標) f=np.where((c<20)|(c>60))=\n', f)
print('符合條件的資料 e[f]=', e[f])
