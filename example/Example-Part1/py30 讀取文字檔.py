## py15: 讀取文字檔

file_obj1 = open("out.txt", mode='w')
for x in range(0, 5):
    print("abc " + str(x), file=file_obj1)
file_obj1.close()

print("讀整批資料")
file_obj2 = open("out.txt")
data = file_obj2.read()
file_obj2.close()
print(data)

print("逐行讀取資料")
file_obj3 = open("out.txt")
for line in file_obj3:
    print(line.rstrip()) #刪去末端的'\n'
file_obj3.close()

print("將資料存入list")
file_obj4 = open("out.txt")
obj_list = file_obj4.readlines()
print(obj_list[2]) #讀取第3筆資料
file_obj4.close()



