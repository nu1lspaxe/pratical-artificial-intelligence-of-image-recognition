
## 二維表列(List)
print("二維表列(List)")
y=[[10,20,30],
   [11,22,33],
   [3,3,3],
   [4,4,4]]
print('y', y)
print('y[0][0]=', y[0][0])
print('y[1][2]=',y[1][2])
print('len(y)=', len(y)) #矩陣第一維長度
print('min(y)=', min(y)) #最小值
print('max(y)=', max(y)) #最大值
print('')

## 三維表列(List)
print("三維表列(List)")
z=[[[10,20,30],[11,22,33],[3,3,3],[4,4,4]]]
print('z', z)
print('z[0][0][0]=', z[0][0][0])
print('z[0][1][2]=',z[0][1][2])
print('len(z)=', len(z)) #矩陣第一維長度
z[0][3][2] = 999
print("z[0][3][2]=999 ->",z)
