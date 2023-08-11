'''OpenCV基本應用'''
#載入相關套件模組
import cv2
import numpy as np

path = "data/ntust.jpg"	#圖片路徑
buttonDown= False #滑鼠左鍵是否按下(全域變數)

## 自定義滑鼠回應函式
def onMouse(event, x, y, flags, param):

	#如果滑鼠左鍵按下
	if event == cv2.EVENT_LBUTTONDOWN:
		global buttonDown
		#buttonDown設為 True
		buttonDown = True 
	#如果滑鼠移動
	if event == cv2.EVENT_MOUSEMOVE:
		#如果按鈕按下
		if buttonDown:
			#在(x,y)位置繪製半徑6px的圓形點
			cv2.circle(im1, (x,y), 6, (0, 255, 255), -1)	#BGR
            #顯示影像
			cv2.imshow("draw", im1)
	#如果滑鼠左鍵彈起
	if event == cv2.EVENT_LBUTTONUP:
		#buttonDown設為 False
		buttonDown = False
	#如果按下滑鼠右鍵
	if event == cv2.EVENT_RBUTTONUP:
		#將視窗刪除
		cv2.destroyAllWindows()

  
#    event: EVENT_LBUTTONDOWN,   EVENT_RBUTTONDOWN,   EVENT_MBUTTONDOWN,
#         EVENT_LBUTTONUP,     EVENT_RBUTTONUP,     EVENT_MBUTTONUP,
#         EVENT_LBUTTONDBLCLK, EVENT_RBUTTONDBLCLK, EVENT_MBUTTONDBLCLK,
#         EVENT_MOUSEMOVE: 

#    flags: EVENT_FLAG_CTRLKEY, EVENT_FLAG_SHIFTKEY, EVENT_FLAG_ALTKEY,
#         EVENT_FLAG_LBUTTON, EVENT_FLAG_RBUTTON,  EVENT_FLAG_MBUTTON

## 自定義滑桿回應函式
def onTrackbar(pos):
	#讀取sliders的資料
	slider1 = cv2.getTrackbarPos("weight", "fusion")
	slider2 = cv2.getTrackbarPos("size", "fusion")
	slider3 = cv2.getTrackbarPos("negative", "fusion")
    #注意slider2不得等於0
	if slider2 == 0: slider2 = 1
	#算出im2的寬高
	rows, columns = im2.shape[:2]
	#讓im1縮小成im2的寬高，縮小後稱為im3
	im3 = cv2.resize(im1, (columns, rows), interpolation=cv2.INTER_LINEAR)
	#建立跟im2一樣大的黑影像im4
	im4 = np.zeros((rows, columns, 3))
	#將im3按slider2(調整size)的比例縮小。縮小後的im3, 貼入im4的中央
	im3 = cv2.resize(im3, None, fx=slider2/100.0, fy=slider2/100.0, interpolation=cv2.INTER_LINEAR)
	im4[int(rows/2-im3.shape[0]/2):int(rows/2+im3.shape[0]/2), int(columns/2-im3.shape[1]/2):int(columns/2+im3.shape[1]/2), :] = im3

    #根據slider1的數值(調整wieght),用cv2.addWeighted對im2與im4加權混合
	mix = cv2.addWeighted(im2, (100-slider1)/100.0, im4.astype(im2.dtype), slider1/100.0, 0)	
	#根據slider3的數值,對im2負片效果
	mix[:,:int(columns*slider3/100.0),:] = 255 - mix[:,:int(columns*slider3/100.0),:]
    #顯示影像
	cv2.imshow("fusion", mix)
        
## 主程式起始處
#建立400x400的黑影像im1
im1 = np.zeros((400, 400, 3), np.uint8)
#顯示黑影像
cv2.imshow("draw", im1)
#用cv2.setMouseCallback建立滑鼠回應函式
cv2.setMouseCallback("draw", onMouse)
#等待
cv2.waitKey(0)

# 讀取背景影像im2
im2 = cv2.imread("data/ntust.jpg")
# 顯示背景影像
cv2.imshow("fusion", im2)
# 用cv2.createTrackbar建立weight滑桿
cv2.createTrackbar("weight", "fusion", 50, 100, onTrackbar)
# 用cv2.createTrackbar建立size滑桿
cv2.createTrackbar("size", "fusion", 50, 100, onTrackbar)
# 用cv2.createTrackbar建立negative滑桿
cv2.createTrackbar("negative", "fusion", 0, 100, onTrackbar)
# onTrackbar回應函式初始化
onTrackbar(0)
# 等待(按 Esc 離開，按'r'重置三條滑桿)
while (1):
	key = cv2.waitKey(1) & 0xFF #留下最後8位元，防止bug
	if key == 27:	# Esc鍵在ASCII表中為27
		break
	elif key == ord('r'):
		cv2.setTrackbarPos("weight", "fusion", 50)
		cv2.setTrackbarPos("size", "fusion", 50)
		cv2.setTrackbarPos("negative", "fusion", 0)
		onTrackbar(0)

