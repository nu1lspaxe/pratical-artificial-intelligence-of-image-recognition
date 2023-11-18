from matplotlib import pyplot as plt
#import matplotlib.plot as plt #同上一行

## 自定義影像彩色轉灰階函式
def rgb2gray(rgb):
    gray = 0.2126*rgb[:,:,0] + 0.7152*rgb[:,:,1] + 0.0722*rgb[:,:,2]
    return gray
    
plt.close('all') #關閉所有視窗
fig = plt.figure() #建立一個 figure

fig.add_subplot(131) #添加1x3圖形陣列的第1個子圖
im1 = plt.imread('data/6.jpg') #讀取彩色影像
plt.imshow(im1, aspect='equal'), plt.title('RGB'), plt.axis('off')
#aspect 是圖像高寬比, 可以給數值，或'equal'(default)按原圖比例, 'auto'空間縮放

fig.add_subplot(132) #添加1x3圖形陣列的第2個子圖
im2 = rgb2gray(im1) #使用自定義影像彩色轉灰階函式
plt.imshow(im2, cmap='gray',aspect='auto'), plt.title('Gray'), plt.axis('off')
#cmap 是灰階顏色對映表(colormap), 'gray'為灰階色

fig.add_subplot(133) #添加1x3圖形陣列的第3個子圖
plt.hist(im2.flatten(), bins=64) #顯示64階灰階直方圖
plt.title('1D histogram'), plt.yticks([])
plt.xlabel('graylevel')

plt.show() #顯示圖形陣列
