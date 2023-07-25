'''cv26: 調整影像對比並顯示灰階直方圖'''
import cv2
import numpy as np
    
def processing(pos): ## 調整影像對比並顯示灰階直方圖
    histSize = 64 # 灰階直方圖統計的區間數(bin)
    brightness = 0.7*(cv2.getTrackbarPos("brightness", filename) - 100)
    contrast = cv2.getTrackbarPos("contrast", filename)/100

    #調整影像對比
    rows, cols, ch = hist_img.shape
    m = np.mean(img1[:]) # 計算影像灰階平均值
    img2 = contrast*(img1 - m)+ m + brightness #調整影像
    img2 = np.clip(img2, 0, 255).astype("uint8")  #將超出範圍的數值以邊界值取代
    cv2.imshow(filename, img2) #顯示經對比調整的影像

    #繪製灰階直方圖
    hist = cv2.calcHist(img2, [0], None, [histSize], [0, 256]) #統計影像灰階直方圖
    #calcHist(影像,指定通道,遮罩,直方圖尺寸,範圍)
    cv2.normalize(hist, hist, 0, rows, cv2.NORM_MINMAX, cv2.CV_8U) #將數值調整到[0 rows]範圍
    binW = round(cols/histSize) #計算直方圖每個bar(直方矩形)的寬度
    hist_img[:]=0 # 黑背景
    for i in range(histSize): # 繪製直方矩形
        cv2.rectangle(hist_img, (i*binW, rows),
                   ((i+1)*binW, rows - round(hist[i][0])), #注意影像座標的原點在左上角，與一般plot不同
                   (255,255,0),-1)        
    cv2.imshow("histogram", hist_img) #顯示直方圖
    cv2.moveWindow("histogram", 100+640, 110)

## 主程式起始處
print("調整影像對比，並顯示灰階直方圖：按 r 鍵重置，按 Esc 離開")
filelist = list(["s","ntust","ntust_normal","ntust_bright","ntust_dark","ntust_low_contrast"]) #影像表列
filename =  filelist[np.random.randint(6)] #隨機選取其中一個檔名
str1 = "data/"+filename+".jpg" #構成路徑+影像檔名的字串
img1 = cv2.imread(str1, cv2.IMREAD_UNCHANGED) #按原格式匯入圖片,可不加參數
h, w = img1.shape[:2]
img1 = cv2.resize(img1, [round(640), round(640*h/w)]) #調整影像大小
hist_img = np.zeros((200, 320, 3), dtype=np.uint8)*255 #建立直方圖背景影像
cv2.namedWindow(filename)
cv2.moveWindow(filename, 100, 20)
cv2.createTrackbar("brightness", filename, 100, 200, processing) # 建立亮度滑桿
cv2.createTrackbar("contrast", filename, 100, 200, processing) # 建立對比滑桿
processing(0) #初始化

while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27: #如果是 Esc (ASCII 第27號)，脫離迴圈
        break
    elif k==ord('r'): #按"r"重置 brightness, contrast 數值
         cv2.setTrackbarPos("brightness", filename, 100)
         cv2.setTrackbarPos("contrast", filename, 100)
         processing(0)
         
cv2.destroyAllWindows()
