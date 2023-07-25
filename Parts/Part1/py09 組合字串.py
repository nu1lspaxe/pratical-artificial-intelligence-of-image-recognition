'''
py04: 組合字串
'''
str1 = 'ABC' #字串可用'  ' 或" "
str2 = 'DEFG'
str3 = str1 + ' '+ str2 #' '是空格
print('一般字串相加')
print(str3)

a=100
b=55
str4 = str(a)+str(b)
print('數值變為字串後相加')
print(a,'+',b,'=',str4)

str5 = "ABC\tDEF\nGHI\tJKL\nMNO\tPQR\n" #\t跳段, \n換行
print(str5)


str6 = "NTUST"
d = 44
e = 3.1415926
formatstr = "%s xxxx %d xxxxxx %f"
print("%s %d %f" % (str6, d, e))
print(formatstr % (str6, d, e))





