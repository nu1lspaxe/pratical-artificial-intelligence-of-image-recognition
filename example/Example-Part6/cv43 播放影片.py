'''cv43: 播放影片'''
import cv2 # 載入opencv套件

# 解析 FourCC 視訊編解碼器四字元識別碼
def decode_fourcc(v):
  v = int(v)
  codec = "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])
  return codec #將32位元的 v, 分四段分別轉換為ASCII字元

# 建立視訊或相機物件
cap = cv2.VideoCapture("data/example.mp4")

# 讀取視訊參數
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) #視訊畫面高
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) #視訊畫面寬
fps = cap.get(cv2.CAP_PROP_FPS) #視訊幀率
total_count = cap.get(cv2.CAP_PROP_FRAME_COUNT) #視訊總幀數
print("影像高,寬: %d x %d" % (height, width))
print("視訊幀率(FPS, Frame Per Second): %.2f" % fps)
print("視訊總幀數: %d" % total_count)

# 取得 Codec 名稱
fourcc = cap.get(cv2.CAP_PROP_FOURCC)
codec = decode_fourcc(fourcc)
print("視訊編解碼器四字元識別碼 (FourCC Codec): " + codec)

while True:  # 用無窮迴圈讀取影片中每個畫格(幀)   
    ret, frame = cap.read() # 讀取影片中的畫格
    if ret == True: # 若有讀取到影片中的畫格
        cv2.imshow("Video", frame) #顯示該畫格
        # 停每800/fps毫秒讀取鍵盤的按鍵
        key = cv2.waitKey(round(800/fps)) & 0xFF
        if key == 27: #當按鍵為ESC(ASCII碼為27)時跳出迴圈
            break   
    else: # 當沒讀到影片中的Frame時，跳出迴圈
        break

cap.release()  # 釋放記憶體
cv2.destroyAllWindows()
