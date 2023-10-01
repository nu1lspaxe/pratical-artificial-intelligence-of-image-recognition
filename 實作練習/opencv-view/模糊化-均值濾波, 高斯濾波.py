import cv2  # 載入opencv模組
import numpy as np  # 載入numpy模組
path = "data/s.jpg"

def processing(pos):
    #讀取調整值
    ksize1 = cv2.getTrackbarPos('ksize','images')

    # 均值濾鏡對原圖模糊化
    img_blur = cv2.blur(img, (ksize1+1, ksize1+1))
    cv2.putText(img_blur, "mean filter (" + str(ksize1+1)+"x"+str(ksize1+1)+")", (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv2.LINE_AA)
    
    # 高斯濾鏡對原圖模糊化
    ksize2 = 2*ksize1+1
    img_GaussianBlur = cv2.GaussianBlur(img, (ksize2, ksize2), 0)  #參數0: 自動決定 sigma
    cv2.putText(img_GaussianBlur, "Gaussian filter (" + str(ksize2)+"x"+str(ksize2)+")", (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv2.LINE_AA)

    #合併三個子圖
    img_all = np.hstack([img, img_blur, img_GaussianBlur])
    cv2.putText(img_all, "Input", (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv2.LINE_AA)
    
    cv2.imshow('images', img_all)


print('模糊化: 均值濾波, 高斯濾波。按任意鍵離開')
# 用imread函式來讀取圖片
img = cv2.imread(path)
cv2.namedWindow("images")

# 用imshow("視窗名稱",圖片)來顯示圖片
cv2.createTrackbar('ksize','images', 5, 21, processing)
processing(0) #初始化

# 用waitKey等待視窗，當按下任意鍵時繼續下一步，括弧內是等待的微秒數(1秒=1000)
cv2.waitKey(0)

# 關閉所有視窗
cv2.destroyAllWindows()
