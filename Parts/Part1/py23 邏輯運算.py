''' 
py10: 邏輯運算
== 等於
!= 不等於 
> 大於
< 小於
>= 大於等於
<= 小於等於
'''

print("成績等級(滿分100分)")
score = input("請輸入分數: ")
s1 = int(score)
if (s1 >= 90) or (s1 <60):
    print("極端")
else:
    print("一般")


score = input("請輸入分數: ")
s2 = int(score)
if (s2 < 90) and (s2 >=60):
    print("一般")
else:
    print("極端")

score = input("請輸入 0 或 1: ")
s3 = int(score)
if (s3 == 1):   # "==" 等於
    print("輸入1")
elif(s3 != 1):  # "!=" 不等於
    print("輸入不是1")
