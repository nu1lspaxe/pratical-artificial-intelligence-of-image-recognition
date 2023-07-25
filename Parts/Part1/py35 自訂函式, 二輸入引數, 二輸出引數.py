'''
py20: 自訂函式, 二輸入引數, 二輸出引數
'''
def f1(x1,x2):
   y1 = x1+x2
   y2 = x1*x2
   return y1, y2

a1 = 3
a2 = 4
z1, z2 = f1(a1, a2)
print(z1)
print(z2)

