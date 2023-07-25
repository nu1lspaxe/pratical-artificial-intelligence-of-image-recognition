## py29: 存文字檔

print("開啟新檔, 存入字串")
file_obj1 = open("out.txt", mode='w')
print("Python testing\n1 2 3 4\n", file=file_obj1)
file_obj1.close()

print("在既有的檔案中，添加字串")
file_obj2 = open("out.txt", mode='a')
print("New python testing\n5\t6\t7\t8\n", file=file_obj2)
file_obj2.close()

print("添加單迴圈數值資料")
file_obj3 = open("out.txt", mode='a')
for x in range(0,100,10):
    print(x, file=file_obj3)
file_obj3.close()

print("添加雙迴圈數值資料")
file_obj4 = open("out.txt", mode='a')
for x in range(0,2):
    for y in range(0,4):
        print([x, y], file = file_obj4)
file_obj4.close()

print("使用write函式，添加字串")
file_obj5 = open("out.txt", mode='a')
file_obj5.write("writing")
file_obj5.close()

