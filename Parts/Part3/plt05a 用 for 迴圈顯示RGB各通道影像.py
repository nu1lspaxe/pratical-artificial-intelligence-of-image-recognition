## plt05a: 用 for 迴圈顯示RGB各通道影像
import matplotlib.pyplot as plt #匯入 matplotlib.pyplot
import numpy as np

plt.close('all') #關閉所有視窗
im1= plt.imread('data/s.jpg') #讀取影像
n = im1.shape #影像陣列的形狀
print('im1.shape=', n) #顯示影像陣列的形狀
print('im1.ndim=', im1.ndim) #顯示影像的維度
str1 = ['Red','Green','Blue','RGB'] #標題表列

#plt.imshow(im) #注意: plt的色彩通道順序是RGB
print('關閉圖像(點擊右上角X), 再顯示下一個圖像')

for i in range(4):
    plt.figure(i)  #建立第i個 figure
    
    if (i==3): #顯示 RGB 影像
        im2= im1.copy()
    else: #顯示 R,G,B 個別通道的子影像
        im2= np.zeros(n, dtype='uint8') #建立 uint8 格式的0矩陣
        im2[:,:,i]= im1[:,:,i] #將 im1 的第i通道複製到 im2
        
    plt.imshow(im2) #顯示影像
    plt.title(str1[i], fontsize= 20) #使用第i個標題
    plt.axis('off') #不顯示 x,y 軸數值
    plt.savefig('data/'+str1[i]+'.jpg') #儲存figure截圖(含標題)
    plt.imsave('data/'+str1[i]+'_imsave.jpg',im2) #儲存影像(原寸)
    plt.show() #顯示(容易被忽略)

## https://matplotlib.org/stable/api/pyplot_summary.html