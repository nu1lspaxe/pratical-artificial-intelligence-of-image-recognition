import matplotlib.pyplot as plt #匯入 matplotlib.pyplot
import numpy as np

plt.close('all') #關閉所有視窗

fig = plt.figure() #建立一個 figure
for i in range(1,7): #讀取1~6號影像
    fig.add_subplot(2,3,i)  #添加2x3圖形陣列的第i個子圖
    im= plt.imread('data/'+str(i)+'.jpg') #讀取影像的'路徑/檔名'
    plt.imshow(im) #顯示影像
    plt.title(str(i), fontsize= 20) #使用i做標題,字級放大
    plt.axis('off') #不顯示 x,y 軸數值

# figure 全螢幕顯示
if 1: #1:全螢幕顯示, 0:忽略
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()

plt.show() #顯示(容易被忽略)
