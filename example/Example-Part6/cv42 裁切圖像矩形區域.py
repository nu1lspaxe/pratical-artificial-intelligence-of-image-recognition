'''cv42: 裁切圖像矩形區塊'''
#import numpy as np
import cv2 as cv
drawing = False # true if mouse is pressed
ix,iy = -1,-1

# mouse callback function 滑鼠反應函式
def draw_crop(event, x, y, flags, param):
    global ix, iy, drawing # 全域變數
    if event == cv.EVENT_LBUTTONDOWN: # 按下滑鼠左鍵
        drawing = True # 繪畫狀態
        ix, iy = x, y
        cv.destroyWindow('roi')  # 刪除 roi 視窗
    elif event == cv.EVENT_MOUSEMOVE: # 滑鼠移動中
        if drawing == True: # 繪畫狀態
            img2 = img.copy() # 複製原影像
            cv.rectangle(img2, (ix,iy), (x,y), (0,255,255), 2) #繪製黃色矩形框
            cv.imshow('image', img2) # 顯示影像
    elif event == cv.EVENT_LBUTTONUP: # 滑鼠左鍵彈起
        drawing = False # 非繪畫狀態
        roi = img[iy:y, ix:x, :] # 複製矩形區域
        cv.imshow('roi', roi) # 顯示矩形區域


img = cv.imread('data/s.jpg') # 讀圖
cv.namedWindow('image') # 建議 image 視窗
cv.setMouseCallback('image', draw_crop) # 設置滑鼠反應函式
while(1): # 永久迴圈
    cv.imshow('image', img) # 顯示影像
    k = cv.waitKey(1) & 0xFF
    if k == 27: # 按 Esc 離開
        break
cv.destroyAllWindows() # 關閉視窗
