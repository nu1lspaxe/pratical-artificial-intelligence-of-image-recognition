'''cv27: 直方圖伸展(histogram stretching)'''
import cv2
import numpy as np

##建立影像灰階直方圖 (輸入圖片，直方圖影像的大小，直方圖區間數)
def create_hist(img, size, histSize):
    hist_img = np.ones(size, dtype=np.uint8)*255 #建立直方圖背景影像
    hist = cv2.calcHist([img], [0], None, [histSize], [0,256]) #統計直方圖
    cv2.normalize(hist, hist, 0, size[0], cv2.NORM_MINMAX, cv2.CV_32F) #調整直方圖的數值範圍
    binW = round(size[1]/histSize) #計算直方圖每個bar(直方矩形)的寬度
    for i in range(histSize):  # 繪製直方矩形
        cv2.rectangle(hist_img, (i*binW, size[0]),
                   ((i+1)*binW, size[0] - round(hist[i][0])),
                   (0,0,0),-1)
    return hist_img

#更新影像灰階直方圖
def update_hist(pos):
    lower = cv2.getTrackbarPos("lower", "histogram")
    upper = cv2.getTrackbarPos("upper", "histogram")
    if lower>upper: #防止 lower > upper
        lower = upper
        cv2.setTrackbarPos("lower", "histogram", lower)
    histSize = int(np.maximum(np.ceil(abs(upper - lower) / 4), 1))

    dst = img.astype("float32")
    dst = np.round((dst - lower) * 255 / (upper-lower+1e-4)) #根據[lower, upper]調整影像對比
    dst = np.clip(dst, 0, 255).astype("uint8")   
    cv2.imshow(filename, dst)
    
    binW = histImgSize[1] / 255 #直方圖區間寬度
    start = int(lower*binW) 
    end = int(upper*binW)
    # 先畫 lower 的線條(青色)
    draw_H = cv2.line(hist_image.copy(), (start,0), (start,histImgSize[0]), (255,255,0), 4)
    # 後畫 upper 的線條(紅色)
    draw_H = cv2.line(draw_H, (end,0), (end,histImgSize[0]), (0,0,255), 4)
    
    rescale_H = create_hist(dst, histImgSize, histSize) #建立新影像的灰階直方圖
    output = np.vstack((draw_H, rescale_H)) #直方圖影像上下堆疊
    cv2.imshow("histogram", output) #顯示直方圖影像

## 主程式起始處
print("直方圖伸展：按 Space 換圖，按 Esc 離開")
filelist = list(["ntust_bright","ntust_dark","ntust_low_contrast"]) #影像表列
filename =  filelist[np.random.randint(3)] #隨機選取其中一個檔名
img1 = cv2.imread("data/"+filename+".jpg", cv2.IMREAD_GRAYSCALE) #以灰階模式開啟影像
height, width = img1.shape
img = cv2.resize(img1, [round(640), round(640*height/width)]) #調整影像大小, 轉換至浮點格式
histImgSize = (200, 500, 3) #直方圖影像的原始尺寸
histSize = 64 # 灰階直方圖統計的區間數(bin)
hist_image = create_hist(img, histImgSize, histSize) #產生直方圖

cv2.imshow(filename, img)
cv2.imshow("histogram",hist_image)
cv2.createTrackbar("lower", "histogram", 0, 255, update_hist) #建立滑桿: 下邊界
cv2.createTrackbar("upper", "histogram", 255, 255, update_hist) #建立滑桿: 上邊界

while (1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27: #如果是 Esc (ASCII 第27號)，脫離迴圈
        break
    elif k==32: #按"Space"隨機讀取另一幅影像
        cv2.destroyWindow(filename)
        filename =  filelist[np.random.randint(3)] #隨機選取其中一個檔名
        img1 = cv2.imread("data/"+filename+".jpg", 0) #以灰階模式開啟檔案
        rows, cols = img1.shape
        img = cv2.resize(img1, [round(640), round(640*rows/cols)]) #調整影像大小, 轉換至浮點格式
        hist_image = create_hist(img, histImgSize, histSize) #產生直方圖
        cv2.imshow(filename, img)
        cv2.imshow("histogram",hist_image)
        cv2.setTrackbarPos("lower", "histogram", 0) #重設滑桿: 下邊界
        cv2.setTrackbarPos("upper", "histogram", 255) #重設滑桿: 上邊界
        
cv2.destroyAllWindows()
