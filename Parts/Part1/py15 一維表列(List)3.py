M=[11,22,33,44,33,99,44,33]
print(M)
M.append(66) #將66添加在表列的末端
print("M.append(66)=", M)
print("M.index(33)=", M.index(33)) #秀出第一個33的索引號
print("M.count(33)=", M.count(33)) #計算33出現的次數
#N = M #連結M表列 (之後若修改M, N也會變)
N = M.copy() #複製M表列  (之後若修改M, N不受影響)
M[0] = 0
print("N=M.copy()", N)