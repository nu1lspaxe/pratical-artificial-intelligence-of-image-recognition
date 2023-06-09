'''cv44: 顯示相機視訊'''
import cv2 # 載入opencv套件

# 解析 FourCC 視訊編解碼器四字元識別碼
def decode_fourcc(v):
  v = int(v)
  codec = "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])
  return codec #將32位元的 v, 分四段分別轉換為ASCII字元

# 建立視訊或相機物件
cap = cv2.VideoCapture(1) # 參數0：使用系統預設相機。指定相機為1,2,3...

if cap.isOpened() is False: # 若沒讀到相機，跳出程式
    print("找不到相機")
    exit()

print(0,cap.get(0))	#CAP_PROP_POS_MSEC =0 視訊開啟至今時間(微秒)
print(1,cap.get(1))	#CAP_PROP_POS_FRAMES =1 視訊開啟至今時間(畫格數)
print(3,cap.get(3))	#CAP_PROP_FRAME_WIDTH =3 畫格寬
print(4,cap.get(4))	#CAP_PROP_FRAME_HEIGHT =4 畫格高
print(5,cap.get(5))	#CAP_PROP_FPS =5 畫格速率(frame per second)
print(6,decode_fourcc(cap.get(6)))	#CAP_PROP_FOURCC =6 視訊編解碼器四字元識別碼
print(7,cap.get(7))	#CAP_PROP_FRAME_COUNT =7 畫格總數
print(8,cap.get(8))	#CAP_PROP_FRAME_COUNT =8 畫格格式(編號)
print(10,cap.get(10))  #CAP_PROP_BRIGHTNESS =10 亮度
print(11,cap.get(11))	#CAP_PROP_CONTRAST =11 對比度
print(12,cap.get(12))	#CAP_PROP_SATURATION =12 飽和度
print(13,cap.get(13))	#CAP_PROP_HUE =13 色相
print(14,cap.get(14))	#CAP_PROP_GAIN =14 亮度增益
print(15,cap.get(15))   #CAP_PROP_EXPOSURE =15 曝光
print(17,cap.get(17))  #CAP_PROP_WHITE_BALANCE_BLUE_U =17 白平衡(藍)
print(20,cap.get(20))  #CAP_PROP_SHARPNESS =20 銳利度
print(21,cap.get(21))  #CAP_PROP_AUTO_EXPOSURE =21 自動曝光
print(22,cap.get(22))  #CAP_PROP_GAMMA =22 伽馬值
print(28,cap.get(28))  #CAP_PROP_FOCUS =28 焦距
print(30,cap.get(30))  #ISO speed =30 感度
print(39,cap.get(39))  #CAP_PROP_AUTOFOCUS =39 自動對焦
print(44,cap.get(44))  #CAP_PROP_AUTO_WB =44 自動白平衡
print(45,cap.get(45))  #CAP_PROP_WB_TEMPERATURE =45 色溫
print(46,cap.get(46))  #CAP_PROP_CODEC_PIXEL_FORMAT =46 像素格式
print(47,cap.get(47))  #CAP_PROP_BITRATE =47 位元深度
#https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html

cap.set(12,64) 
print('修改飽和度',cap.get(12))
cap.set(13,0) 
print('修改色相',cap.get(13))

while (1):  # 用無窮迴圈讀取影片中每個畫格(幀)   
    ret, frame = cap.read() # 讀取影片中的畫格
    if ret == True: # 若有讀取到影片中的畫格
        cv2.imshow("Video", frame) #顯示該畫格
        # 停每25毫秒讀取鍵盤的按鍵
        key = cv2.waitKey(25) & 0xFF
        if key == 27: #當按鍵為ESC(ASCII碼為27)時跳出迴圈
            break   
    else: # 當沒讀到影片中的Frame時，跳出迴圈
        break

cap.release() # 釋放記憶體
cv2.destroyAllWindows()
