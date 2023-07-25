import os
os.system("cls") #清空 terminal

M =[[1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]]

## 巢狀迴圈
for row in M:
    for column in row:
        print(column)