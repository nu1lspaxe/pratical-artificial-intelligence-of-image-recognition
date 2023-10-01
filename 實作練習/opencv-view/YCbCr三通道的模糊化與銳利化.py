'''
人眼對CbCr通道的解析度較低
只有對Y(通道0)清晰度，對影像品質有影響
'''
import cv2  # 載入opencv模組
import numpy as np  # 載入numpy模組
path = "data/ntust.jpg" #影像路徑
font = cv2.FONT_HERSHEY_SIMPLEX #字體

def showYCrCb(YCrCb_image): ## 產生單通道模糊化結果，與各通道影像
    h2, w2 = YCrCb_image.shape[:2]
    YCrCb_channels = np.zeros((h2,w2*3,3)).astype("uint8") #建立空白影像
    list1 = np.array([[1,2],[0,2],[0,1]]).astype("int16") #通道選擇表
    for ch in range(0, 3):
        YCrCb_image2 = YCrCb_image.copy() #處理後的影像必須獨立
        YCrCb_image2[:,:,list1[ch]] = 128 #將ch之外的通道設為灰畫面，與下列六行作用相同
##        if ch==0:
##            YCrCb_image2[:,:,[1,2]] = 128
##        elif ch==1:
##            YCrCb_image2[:,:,[0,2]] = 128
##        elif ch==2:
##            YCrCb_image2[:,:,[0,1]] = 128
        YCrCb_channels[:,(0+ch*w):(ch+1)*w2,:] = YCrCb_image2 #水平平接Y,Cr,Cb三個子圖

    #調高Cr與Cb通道的色彩對比，超出[0 255]範圍必須以邊界值取代
    YCrCb_channels[:,:,[1,2]] = np.clip(2*(YCrCb_channels[:,:,[1,2]]-128.) + 128, 0, 255) 
    YCrCb_channels = cv2.cvtColor(YCrCb_channels, cv2.COLOR_YCrCb2BGR) #轉換回BGR空間
    cv2.putText(YCrCb_channels, 'Y channel' , (23, 53), font, 1, 0, 2)
    cv2.putText(YCrCb_channels, 'Y channel' , (20, 50), font, 1, (0, 255, 255), 2)
    cv2.putText(YCrCb_channels, 'Cr channel' , (23+w2, 53), font, 1, 0, 2)
    cv2.putText(YCrCb_channels, 'Cr channel' , (20+w2, 50), font, 1, (0, 255, 255), 2)
    cv2.putText(YCrCb_channels, 'Cb channel' , (23+w2*2, 53), font, 1, 0, 2)
    cv2.putText(YCrCb_channels, 'Cb channel' , (20+w2*2, 50), font, 1, (0, 255, 255), 2)
    BGR_image = cv2.cvtColor(YCrCb_image, cv2.COLOR_YCrCb2BGR)  #轉換回BGR空間
    return BGR_image, YCrCb_channels

def sharpening(pos): #自定義影像模糊化/銳化函式
    ch = cv2.getTrackbarPos('channel', 'images')  #讀取通道值 ch
    t = cv2.getTrackbarPos('sharpness', 'images')  #讀取銳化程度數值 t
    channel_name = ["Y","Cr","Cb"]
    YCrCb_img2 = YCrCb_img1.copy() #處理後的影像必須獨立

    if (t<20):
        ## 用 ksize x ksize 大小的範圍用高斯模糊模糊原圖
        ksize = 2*(20 - t)+1 #必須是奇數
        temp = cv2.GaussianBlur(YCrCb_img1[:,:,ch], (ksize, ksize), 0) # 影像高斯模糊
        YCrCb_img2[:,:,ch] = temp # ch 通道的銳化影像
        dst, YCrCb_channels = showYCrCb(YCrCb_img2) #產生單通道模糊化結果，與各通道影像
        str1 = channel_name[ch] +' channel blurring (' + str(ksize) + 'x' + str(ksize) + ')'         

    elif (t>=20): ## 用遮色片銳利化(USM)
        n = t - 20
        temp = cv2.GaussianBlur(YCrCb_img1[:,:,ch], (7, 7), 0) # 建立模糊遮色片
        temp = cv2.addWeighted(YCrCb_img1[:,:,ch], 1+n/3.0, temp, -n/3.0, 0); # 加權運算
        YCrCb_img2[:,:,ch] = temp # ch 通道的銳化影像
        dst, YCrCb_channels = showYCrCb(YCrCb_img2) #產生單通道模糊化結果，與各通道影像       
        str1 = channel_name[ch] + ' channel sharping (' + str(round(n/3, 2)) + ')'

    cv2.rectangle(dst, (10, 20), (380, 70), 0, -1) #文字黑背景框
    cv2.putText(dst,  str1, (20, 50), font, 0.8, (255 - t*(255/40), 255, t*(255/40)), 2)  #變色文字
    upper_img = np.hstack([BGR_img, dst]) #水平排列 BGR_img 與 dst
    lower_img = cv2.resize(YCrCb_channels, (w*2, round(h*2/3))) #調整Y,Cr,Cb子圖的大小
    output = np.vstack([upper_img, lower_img]) #上下合併兩圖
    
    cv2.imshow('images', output)  #顯示處理後的影像                

print('YCbCr三通道的模糊化/銳利化：按 r 鍵重設滑桿數值, 按 Esc 離開')
BGR_img = cv2.imread(path, 1) #以彩色模式開啟影像檔
h, w = BGR_img.shape[:2] #讀取影像高,寬
BGR_img = cv2.resize(BGR_img, (600, int(600*h/w))) #使影像寬度= 600 px
h, w = BGR_img.shape[:2]
YCrCb_img1 = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2YCrCb) #轉換至YCrCb空間
cv2.namedWindow('images')
cv2.createTrackbar('channel', 'images', 0, 2, sharpening) #建立滑桿
cv2.createTrackbar('sharpness', 'images', 20, 40, sharpening) #建立滑桿
sharpening(0) #初始化

while(1):
    k = cv2.waitKey(20) & 0xFF
    if k == 27: #如果是 Esc (ASCII 第27號)，脫離迴圈
        break
    elif k==ord('r'): #按 "r" 鍵重設滑桿數值
        cv2.setTrackbarPos('channel','images', 0)
        cv2.setTrackbarPos('sharpness','images', 20)
        sharpening(0)      

# 關閉所有視窗
cv2.destroyAllWindows()
