import cv2  # 載入opencv套件

# 用imread函式來讀取圖片
src = cv2.imread('data/s.jpg')

#顯示影像讀取後的格式
print(src.dtype, src.shape)

# 用7x7大小的均值濾鏡對原圖模糊化
dst = cv2.blur(src, (7,7))

# 用imshow("視窗名稱",圖片)來顯示圖片
cv2.imshow('src',src), cv2.moveWindow('src', 200, 50)
cv2.imshow('dst',dst), cv2.moveWindow('dst', 850, 50)

# 用waitKey等待視窗，當按下任意鍵時繼續下一步，括弧內是等待的微秒數(1秒=1000)
cv2.waitKey(3000)

# 關閉所有視窗
cv2.destroyAllWindows()
