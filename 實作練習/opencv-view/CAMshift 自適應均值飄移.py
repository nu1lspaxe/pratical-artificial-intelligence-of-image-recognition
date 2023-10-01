import numpy as np
import cv2 as cv

cap = cv.VideoCapture('https://www.bogotobogo.com/python/OpenCV_Python/images/mean_shift_tracking/slow_traffic_small.mp4')

# take first frame of the video
ret,frame = cap.read()
# setup initial location of window 用於統計初始色相直方圖的影像範圍(ROI)
x, y, w, h = 300, 200, 100, 50 # simply hardcoded the values
track_window = (x, y, w, h)
# set up the ROI for tracking 讀出第0幀的影像ROI
roi = frame[y:y+h, x:x+w]
hsv_roi =  cv.cvtColor(roi, cv.COLOR_BGR2HSV) #轉換至HSV空間
mask = cv.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.))) #忽略低飽和與低亮度色彩
roi_hist = cv.calcHist([hsv_roi],[0],mask,[180],[0,180]) #建立ROI的色相直方圖
cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX) #將色相直方圖資料調整至[0 255]範圍，以便顯示
# plt.hist(roi_hist)
# plt.show()
# Setup the termination criteria, either 10 iteration or move by at least 1 pt
# 設定CamShift 收斂的終止條件，10次迭代或誤差小於1，看哪先到，就終止運算
term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1 )
while(1): #視訊讀取迴圈
    ret, frame = cap.read() #讀取下一幀
    if ret == True: #如果有讀到畫面
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) #轉換至HSV空間
        #根據ROI的色相直方圖，獲得新畫面的色相近似度（機率）反投影圖
        dst = cv.calcBackProject([hsv],[0],roi_hist,[0,180],1) 
        # apply camshift to get the new location
        # 根據反投影圖(色相近似度)與上一幀的跟蹤框，獲得新的跟蹤框與端點
        ret, track_window = cv.CamShift(dst, track_window, term_crit)
        # Draw it on image
        pts = cv.boxPoints(ret)
        pts = np.int0(pts)
        #在frame上，根據系列端點，繪製(白色=255)封閉路徑的多邊形
        img2 = cv.polylines(frame,[pts],True, 255,2) 
        cv.imshow('img2',img2) #顯示影像
        k = cv.waitKey(30) & 0xff
        if k == 27: #按Esc鍵脫離迴圈
            break
    else: #如果讀不到視訊畫面，脫離迴圈
        break