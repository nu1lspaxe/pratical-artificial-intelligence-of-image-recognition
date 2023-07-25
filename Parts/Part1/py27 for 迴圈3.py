## for 迴圈3

import os
os.system("cls") #清空 terminal

start = -2
end = 9
step = 2
print("當start值是%2d, end值是%2d, step值是%2d時的range( )串列元素:" % (start, end, step))
for x in range(start, end, step):
    print(x)
