## plt09a: colormap 比較
import matplotlib.pyplot as plt #匯入 matplotlib.pyplot

## 自定義影像彩色轉灰階函式
def rgb2gray(rgb):
    gray = 0.2126*rgb[:,:,0] + 0.7152*rgb[:,:,1] + 0.0722*rgb[:,:,2]
    return gray

plt.close('all') #關閉所有視窗
colormaps = ['gray','jet','rainbow',
             'summer','autumn','winter','copper',
             'coolwarm','cool','hot',
             'twilight','hsv']
im1 = plt.imread('data/6.jpg')
im2 = rgb2gray(im1) #使用自定義影像彩色轉灰階函式

fig = plt.figure() #建立一個 figure
#fig.tight_layout() #自動排版

for i in range(0,12): #讀取0~11號 colormap
    fig.add_subplot(3,4,i+1)  #添加3x4圖形陣列的第i+1個子圖
    ax= plt.imshow(im2, cmap= colormaps[i]) #用第i的colormap套色
    plt.title(colormaps[i]) #用colormap的名稱做標題
    plt.axis('off')
    plt.colorbar(ax) #標示 colorbar

#全螢幕顯示
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
plt.show() #顯示圖形陣列

## colormaps:
## https://matplotlib.org/stable/tutorials/colors/colormaps.html