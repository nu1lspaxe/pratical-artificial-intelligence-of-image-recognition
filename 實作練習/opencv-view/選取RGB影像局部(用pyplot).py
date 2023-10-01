import cv2 # 載入opencv套件
import matplotlib.pyplot as plt

# 用imread函式來讀取圖片
img= cv2.imread("data/s.jpg")
img= img[:,:,::-1] #將第三維的元素順序顛倒
height, width, channel = img.shape
print(height, width, channel)

px = img[100, 100] #讀取一點的BGR數值
print('img[100, 100]=', px) #顯示該數值
img[240, 100, :] = [255, 255, 0] #中心點設成黃色(一小點)
img[280:360, 260:300, :] = [255, 0, 0] #矩形設成紅色

fig= plt.figure()
fig.add_subplot(2,3,1)
plt.imshow(img) #顯示處理過的影像
plt.title('plt.imshow')

fig.add_subplot(2,3,2)
plt.imshow(img[:, :, 0],'gray') #顯示紅色通道
plt.title('Red channel'), plt.axis('off')

fig.add_subplot(2,3,3)
plt.imshow(img[:, :, 1],'gray') #顯示綠色通道
plt.title('Green channel'), plt.axis('off')

fig.add_subplot(2,3,4)
plt.imshow(img[:, :, 2],'gray') #顯示藍色通道
plt.title('Blue channel'), plt.axis('off')

fig.add_subplot(2,3,5)
roi = img[0:int(height/2), 0:int(width/2) ] #擷取左上角高寬1/2之區域
plt.imshow(roi)
plt.title('take top-left region')

plt.show() #注意: 容易被忽略

plt.imsave("data/roi.jpg", roi) #用plt.imsave存檔,注意它的色通道順序必須是 RGB

