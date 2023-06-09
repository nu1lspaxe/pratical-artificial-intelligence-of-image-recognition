## py14: 一維列表(List)2

x = [10, 30, -20, 6, 55, 0]
y = ["abc", "def"]
print('x=', x)
print('x[0:5:2]=', x[0:5:2]) #從第0個到第5個(不含第5個)，以2為間隔

print('len(x)=', len(x)) #矩陣長度
print('min(x)=', min(x)) #最小值
print('max(x)=', max(x)) #最大值
print('sum(x)=', sum(x)) #總和
print('mean(x)=', sum(x)/float(len(x))) #平均值

x.extend(y)
print('x.extend(y)=', x) #增添y列表
x.insert(2,999)
print('x.insert(2,999)=', x) #在位置2插入999
x.remove(6)
print('x.remove(6)=', x) #刪除數值6
x.remove('def')
print('x.remove("def")=', x) #刪除數值"def"
x.pop()
print('x.pop()=', x) #移除最後一位
x.sort()
print('x.sort()=', x) #遞增排序
x.reverse()
print('x.reverse()=', x) #列表反轉