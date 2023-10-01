import cv2  # 載入opencv套件

# 用imread函式來讀取圖片
src=cv2.imread('data/s.jpg')

# 用imshow("視窗名稱",圖片)來顯示圖片
cv2.imshow('src',src), cv2.moveWindow('src',300,50)

# 影像反白
dst = 255 - src
cv2.imshow('dst', dst), cv2.moveWindow('dst',650,50)
cv2.imwrite('data/dst.jpg', dst) # 存檔
#cv2.imwrite('data/dst.jpg', dst, [cv2.IMWRITE_JPEG_QUALITY, 98])

# 用waitKey等待視窗，當按下任意鍵時繼續下一步
cv2.waitKey(0)

# 關閉所有視窗
cv2.destroyAllWindows()
