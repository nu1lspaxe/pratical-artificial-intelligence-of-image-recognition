## cv06: 影像檔案格式
import cv2  # 載入opencv套件

#檔案格式選擇
im_option= int(input('1.logical(BW), 2.uint8(gray), 3.uint8(color), 4.uint16(gray), 5.uint16(color)= ? '))
if im_option==1:
    filename= 's_bw'
elif im_option==2:
    filename= 's_uint8_gray'
elif im_option==3:
    filename= 's_uint8_color'
elif im_option==4:
    filename= 's_uint16_gray'
elif im_option==5:
    filename= 's_uint16_color'
else:
    print('filename error')

str1= 'data/'+ filename + '.tif'

#讀檔方式選擇
open_option= int(input('1.default, 2.Unchanged(=-1), 3.Grayscale(=0), 4.Color(=1)= ? '))
if open_option==1:
    src = cv2.imread(str1)
elif open_option==2:
    src = cv2.imread(str1, cv2.IMREAD_UNCHANGED) #(參數可用-1替代)
elif open_option==3:
    src = cv2.imread(str1, cv2.IMREAD_GRAYSCALE) #(參數可用0替代)
elif open_option==4:
    src = cv2.imread(str1, cv2.IMREAD_COLOR)  #(參數可用1替代)
else:
    print('opening error')

print(src.dtype, src.shape) #顯示影像讀取後的格式

# 用imshow("視窗名稱",圖片)來顯示圖片
cv2.imshow('src', src)

# 用waitKey等待視窗，當按下任意鍵時繼續下一步，括弧內是等待的微秒數(1秒=1000)
cv2.waitKey()

# 關閉所有視窗
cv2.destroyAllWindows()
