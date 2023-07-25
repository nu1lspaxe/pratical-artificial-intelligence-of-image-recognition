str1="ABCdefGHIjk"
str2="abcdefghijk"
str3="ABCDEFGHIJK"
#1str="ABCdefGHIjk" #錯誤:變數的第一個字不能是數值
print("str1:"+ str1)
print("str2:"+ str2)
print("str3:"+ str3)
print(len(str1)) #字串長度
print(str1[0]) #第0個字元
print(str1[2]) #第2個字元
print("str1是否全為小寫?", str1.islower())
print("str1是否全為大寫?", str1.isupper())
print("str2是否全為小寫?", str2.islower())
print("str2是否全為大寫?", str2.isupper())
print("str3是否全為小寫?", str3.islower())
print("str3是否全為大寫?", str3.isupper())
print("str1是否為數值?", str1.isnumeric())
print("str1是否為字串?", str1.isalpha())

a=5
print("a=" + str(a))
print("a是否為數值?", str1.isnumeric())
print("a是否為字串?", str1.isalpha())