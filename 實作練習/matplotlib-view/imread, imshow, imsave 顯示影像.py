import matplotlib.pyplot as plt #匯入 matplotlib.pyplot
import numpy as np

plt.close('all') #關閉所有視窗
fig= plt.figure(1)
str1 = 'data/s.jpg' #"路徑/檔名"
im1= plt.imread(str1) #讀取影像
print(im1.dtype, im1.shape) #陣列型別與形狀
plt.title(str1) #以"路徑/檔名"作為標題
plt.axis('off') #不顯示x,y軸數值
plt.imshow(im1) #顯示影像
im2 = 255 - im1 #影像反白
im= plt.imsave('data/imshave.jpg', im2) #儲存新影像
plt.show()
