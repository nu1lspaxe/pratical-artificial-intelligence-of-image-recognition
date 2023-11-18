import cv2  # 載入opencv模組
import numpy as np  # 載入numpy模組

print('自訂空間濾鏡(模糊)：按任意鍵離開')
img = cv2.resize(cv2.imread('data/ntust.jpg'), None, fx=0.5, fy=0.5) #與影像原格式開啟，彩色或灰階格式皆適用

# 生成濾鏡
name_list = ['5x5 meanBlur','25x25 meanBlur','Horizontal moving','Vertical moving','Diagonal moving']
option = int(input("1. 5x5 均值濾波, 2. 25x25 均值濾波, 3. 橫向運動, 4. 綜向運動, 5 斜向運動 = ? "))
if (option ==1):
    a = np.ones([5,5]).astype("float32"); kernel = a/a.size
elif (option ==2):
    a = np.ones([25,25]).astype("float32"); kernel = a/a.size
elif (option ==3):
    a = np.ones([1,50]).astype("float32"); kernel = a/a.size
elif (option ==4):
    a = np.ones([50,1]).astype("float32"); kernel = a/a.size
elif (option ==5):
    a = np.ones(50).astype("float32")
    kernel = np.diag(a); kernel = kernel/a.size #diag()將一維數值陣列 a 填入對角線矩陣
else:
    print("error")
print('濾鏡\n' +str(kernel)) #列出濾鏡權重

# 影像空間濾波
dst = cv2.filter2D(img, -1, kernel) #使用自訂濾鏡
if dst.ndim==2:
    dst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.putText(dst , name_list[option-1] , (23, 53), cv2.FONT_HERSHEY_SIMPLEX, 1, 0, 2)
cv2.putText(dst , name_list[option-1] , (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
output = np.hstack([img, dst])
cv2.imshow('images', output)

# 用waitKey等待視窗，當按下任意鍵時繼續下一步，括弧內是等待的微秒數(1秒=1000)
cv2.waitKey()

# 關閉所有視窗
cv2.destroyAllWindows()
