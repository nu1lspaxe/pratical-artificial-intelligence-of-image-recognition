'''
py09: if, elif, else 的用法
'''
print("成績等級")
score = input("請輸入分數: ")
sc = int(score)
if (sc >= 90):
    print(" A")
elif (sc >= 80):
    print(" B")
elif (sc >= 70):
    print(" C")
elif (sc >= 60):
    print(" D")
else:
    print(" F")

# Python 裡沒有 switch/cases..., 要用 if/elif....取代
    
