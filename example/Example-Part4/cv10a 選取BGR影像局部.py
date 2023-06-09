## cv10a: 選取BGR影像局部
import cv2 # 載入opencv套件

# 用imread函式來讀取圖片
img= cv2.imread("data/s.jpg")
height, width, channel = img.shape
print(height, width, channel)

px = img[100, 100] #讀取一點的BGR數值
print('img[100, 100]=', px) #顯示該數值
img[240, 100, :] = [0, 255, 255] #中心點設成黃色(一小點)
img[280:360, 260:300, :] = [0, 0, 255] #矩形設成紅色

cv2.imshow("Image",img) #顯示處理過的影像

cv2.imshow("Blue", img[:, :, 0]) #顯示藍色通道
cv2.imshow("Green", img[:, :, 1]) #顯示綠色通道
cv2.imshow("Red", img[:, :, 2]) #顯示紅色通道

roi = img[0:int(height/2), 0:int(width/2) ] #擷取左上角高寬1/2之區域
cv2.imshow("roi", roi)
cv2.imwrite("data/roi.jpg", roi)

# 用waitKey等待視窗，當按下任意鍵時繼續下一步
cv2.waitKey(0)

# 關閉所有視窗
cv2.destroyAllWindows()
