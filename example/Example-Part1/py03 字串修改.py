## py02: 字串修改
str1 = "ABCdefGHIjkABBC"
print("str1:"+ str1)
print(len(str1)) #字串長度
print(str1[0]) #第0個字元
print(str1[2]) #第2個字元
print(str1.replace('B','b')) #把str1裡所有的'B'都改成'b'

list1 = list(str1)
list1[0:5]='aaaa'
print(list1) #這是一個由多個字元構成的 list
str2 = ''.join(list1) #合併成一個字串
print(str2)