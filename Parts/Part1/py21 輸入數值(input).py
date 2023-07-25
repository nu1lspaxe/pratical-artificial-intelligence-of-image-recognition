'''
py08: 輸入數值 (input)
'''
a = input("a=? ")
b = input("b=? ")
c = a+b
print(c)
d = int(a)+int(b)
print('直接加(成為字串): ', c, type(c))
print('轉成數值再相加(成為數值): ', d, type(d))
