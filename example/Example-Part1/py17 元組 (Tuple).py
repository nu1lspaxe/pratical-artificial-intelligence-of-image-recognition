## py17: 元組 (Tuple)
## 元組（Tuple）與表列（List）近似，但不得修改，用來存放常數

print('M是表列, N是元組')
M = [123, 'abc', True] #用表列方括弧
print(M)
print('len(M))=', len(M))
M[0] = 66
print(M)
#########################

N = (456, 'def', False) #元組用圓括弧
print(N)
print('len(N))=', len(N))
N[0] = 66
print(N)