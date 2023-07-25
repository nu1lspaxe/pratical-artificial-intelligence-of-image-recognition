'''cv55: Lucas-Kanade Optical Flow LK光流追蹤'''
import numpy as np
import cv2 as cv

cap = cv.VideoCapture(1) #開啟相機視訊物件
# ShiTomasi 角點偵測的參數
feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )
# Lucas-Kanade optical flow 的參數
lk_params = dict( winSize  = (15, 15), #觀察範圍
                  maxLevel = 2, #金字塔層數
                  criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

color = np.random.randint(0, 255, (100, 3)) # 產生0~255隨機整數構成的100x3 BGR色彩值
ret, old_frame = cap.read() # 讀取初始視訊影像
old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY) #影像轉換至灰階格式
p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params) #找出初始特徵點位置

# 繪製光流追蹤圖
mask = np.zeros_like(old_frame) #建立遮罩影像初始化(黑畫面)
while(1): #視訊迴圈
    ret, frame = cap.read() # 讀取視訊影像
    if not ret:
        print('沒有讀到影像!')
        break
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  #影像轉換至灰階格式
    # 計算光流：獲得特徵移動後的位置p1,是否有追蹤到st,誤差err 
    p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    #  選擇特徵點
    if p1 is not None: #如果p1的組數大於0
        good_new = p1[st==1] #將有追蹤到的從p1匯入good_new
        good_old = p0[st==1] #將有追蹤到的從p0匯入good_old
    # 繪製光流軌跡
    # enumerate 將數組整理成(0,seq[0]), (1,seq[1]),.....(i,(new,old))
    for i, (new, old) in enumerate(zip(good_new, good_old)):  #處理第i個特徵點光流追蹤的結果
        a, b = new.ravel() #good_new中第i筆資料的(x,y)座標
        c, d = old.ravel() #good_old中第i筆資料的(x,y)座標
        #在mask上繪製第i個特徵點新增的光流路徑(彩色線段)
        mask = cv.line(mask, (int(a), int(b)), (int(c), int(d)), color[i].tolist(), 2) 
        #在frame上以彩色圓圈繪製第i個特徵點
        frame = cv.circle(frame, (int(a), int(b)), 5, color[i].tolist(), -1) 

    img = cv.add(frame, mask) #將mask疊加到frame上
    cv.imshow('frame', img) #顯示疊上光流路徑(遮罩)的
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
    # 更新上一幀和之前的點
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2) #-1代表第一維數量照舊

cv.destroyAllWindows()