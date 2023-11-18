import cv2 # 載入opencv套件
import numpy as np

# 解析 FourCC 視訊編解碼器四字元識別碼
def decode_fourcc(v):
  v = int(v)
  codec = "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])
  return codec #將32位元的 v, 分四段分別轉換為ASCII字元

def processing(pos):
    frameNo = cv2.getTrackbarPos('frame','Video') 
    cap.set(1,frameNo) # 指向指定畫格
    #ret, frame = cap.retrieve(frameNo) #讀取指定編號的畫格(cv2.CAP_PROP_POS_MSEC會錯誤)
    ret, frame = cap.read() # 讀取影片中的下一個畫格
    if ret== True:
        cv2.imshow("Video", frame) #顯示該畫格
        print('當前播放位置(毫秒):',int(cap.get(0))) #cv2.CAP_PROP_POS_MSEC
        print('當前播放位置(畫格編號):',int(cap.get(1))) #cv2.CAP_PROP_POS_FRAMES
        #print('當前播放位置(比率,0:頭,1:尾)只支援avi檔:',round(cap.get(2),4)) #cv2.CAP_PROP_POS_AVI_RATIO

    else:
        cv2.imshow("Video", np.zeros((height,width),'uint8')) #顯示黑畫面


# 建立視訊或相機物件
cap = cv2.VideoCapture("data/example.mp4")

# 讀取視訊參數
#https://docs.opencv.org/4.x/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
width= int(cap.get(3)) #cv2.CAP_PROP_FRAME_WIDTH
print('畫格寬:',width)
height= int(cap.get(4)) #cv2.CAP_PROP_FRAME_HEIGHT
print('畫格高:',height) 
print('畫格速率(fps):',cap.get(5)) #cv2.CAP_PROP_FPS
print('視訊編解碼器四字元識別碼:',decode_fourcc(cap.get(6))) #cv2.CAP_PROP_FOURCC
frameTotal= int(cap.get(7))
print('畫格總數:', frameTotal) #cv2.CAP_PROP_FRAME_COUNT
print('畫格格式(編號):',cap.get(8)) #cv2.CAP_PROP_FORMAT

# 取得 Codec 名稱
fourcc = cap.get(cv2.CAP_PROP_FOURCC)

cv2.namedWindow('Video')
cv2.createTrackbar('frame', 'Video', 0, frameTotal, processing) #建立滑桿
processing(0)


while True:
   key = cv2.waitKey(25) & 0xFF
   if key == 27: #當按鍵為ESC(ASCII碼為27)時跳出迴圈
        break   

cap.release()  # 釋放記憶體
cv2.destroyAllWindows()
