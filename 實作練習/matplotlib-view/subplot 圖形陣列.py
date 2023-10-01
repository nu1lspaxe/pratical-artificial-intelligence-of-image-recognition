import matplotlib.pyplot as plt #匯入 matplotlib.pyplot
import numpy as np

plt.close('all') #關閉所有視窗
fig = plt.figure() #建立一個 figure

fig.add_subplot(221) #添加2x2圖形陣列的第1個子圖
im1 = plt.imread('data/1.jpg')
plt.imshow(im1), plt.title(1), plt.axis('off')

fig.add_subplot(222) #添加2x2圖形陣列的第2個子圖
im2 = plt.imread('data/2.jpg')
plt.imshow(im2), plt.title(2), plt.axis('off')

fig.add_subplot(223) #添加2x2圖形陣列的第3個子圖
im3 = plt.imread('data/3.jpg')
plt.imshow(im3), plt.title(3), plt.axis('off')

fig.add_subplot(224) #添加2x2圖形陣列的第4個子圖
im4 = plt.imread('data/4.jpg')
plt.imshow(im4), plt.title(4), plt.axis('off')

# figure 全螢幕顯示
if 0: #1:全螢幕顯示, 0:忽略 
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()

plt.show() #顯示圖形陣列

