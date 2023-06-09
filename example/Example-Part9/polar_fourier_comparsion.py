## 兩影像4x4區塊傅立葉極座標頻譜的比較
## Texture Dissimilarity of a pair of images
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

## 計算傅立葉極座標頻譜的子程式
def log_polar_fourier_spectrum(im):
    vector=im.ndim
    if vector==3:#
        fxy=cv.cvtColor(im,cv.COLOR_RGB2GRAY)#RGB 3維轉成2維灰階影像
    elif vector==2:
        fxy = im#
        
    else:
        print('the image is not a 2D or 3D array (非2維和3維矩陣)')#

    if fxy.dtype=='uint8':
        fxy = fxy/255.

    #Fuv = np.fft.fftshift(dft)#頻率0分量移動到頻譜中心
    Fuv= np.fft.fft2(fxy) #默認結果中心在左上角
    fshift = np.fft.fftshift(Fuv)  #調用fftshift()函数轉移至頻譜中心 
    P = np.log(np.abs(fshift)+1)#fft结果是複數, 其絕對值是振幅(P)，log中不可為0(+1)

    [Y,X]=np.mgrid[(-ksize/2)+1:ksize/2+1:1,(-ksize/2)+1:ksize/2+1:1]#
    X1=np.float32(X)
    Y1=np.float32(-Y) #注意:影像原始的垂直座標是越往下數值越高，但在極座標的對映是越往上座標值越高
    rho, theta= cv.cartToPolar(X1, Y1) #2D Fourier transform into polar coordinates
    deg = (180/np.pi*theta) #convert to [0 360] degree
    
    hist2d = np.zeros((18,8),'float32') ##
    for di in range(0,18):
        for ri in range(0,8):
            idx = np.where((deg>=(di*20)) & (deg<((di+1)*20)) & (rho>=ri*(71./8.)) & (rho<(ri+1)*(71./8.)))
            meanPi = np.mean(P[idx]) #可能是空的，無法計算，得到 nan
            if np.isnan(meanPi):
                hist2d[di,ri] = 0
            else:
                hist2d[di,ri] = meanPi

    return P, hist2d

# input image names
#filename1 = 'data/1.jpg'
filename1 = 'data/2.jpg'
filename2 = 'data/3.jpg'

# step1: read image 1
img1= cv.imread(filename1)
ksize= 100 #先resize成400x400
img1= cv.resize(img1,(4*ksize,4*ksize))
img1= cv.cvtColor(img1, cv.COLOR_BGR2RGB)#show原圖
plt.subplot(241), plt.imshow(img1), plt.title('image 1', fontsize=14)
plt.axis('off')

# step2: create P1, hist2d1 and show P1 (Log Fourier Spectrum)
P1 = np.zeros(ksize,'float32')
hist2d1 = np.zeros((18,8),'float32')
for x in range(4):
    for y in range(4):
        [P1x, hist2d1x] = log_polar_fourier_spectrum(img1[ksize*x:ksize*(x+1),ksize*y:ksize*(y+1),:])
        P1= P1+P1x
        hist2d1= hist2d1+hist2d1x
P1= P1/16
hist2d1= hist2d1/16
P1_im= np.clip(P1/4,0,1).astype('float32')
P1_im= cv.cvtColor(P1_im, cv.COLOR_GRAY2RGB)
cv.line(P1_im,[ksize//2, 0],[ksize//2, ksize],(1,.5,0),1)
cv.line(P1_im,[0, ksize//2],[ksize, ksize//2],(1,.5,0),1)
plt.subplot(242),plt.imshow(P1_im)
plt.title('Fourier Spectrum 1 (4x4 blocks)', fontsize=14), plt.axis('off')

# step5: show Log-Polar Fourier Spectrum 1
im_hist2d1= hist2d1[0:9,0:7]
im_hist2d1= cv.resize(np.flipud(im_hist2d1.T),(180,160), interpolation=3)
im_hist2d1_mb= cv.copyMakeBorder(im_hist2d1,2,2,2,2,cv.BORDER_CONSTANT) #加黑邊寬
plt.subplot(243), plt.imshow(im_hist2d1_mb, cmap='gray', vmin=0, vmax=4)
plt.title('Polar Fourier Spectrum 1', fontsize=16), plt.axis('off')

# step4: read image 2
img2= cv.imread(filename2)
img2= cv.resize(img2,(4*ksize,4*ksize))
img2= img2[:,:,::-1] #將BGR順序改成RGB 
plt.subplot(245), plt.imshow(img2), plt.title('image 2', fontsize= 14)
plt.axis('off')

# step5: create P2, hist2d2 and show P2 (Log Fourier Spectrum)
P2 = np.zeros(ksize,'float32')
hist2d2 = np.zeros((18,8),'float32')
for x in range(4):
    for y in range(4):
        [P2x, hist2d2x] = log_polar_fourier_spectrum(img2[ksize*x:ksize*(x+1),ksize*y:ksize*(y+1),:])
        P2=P2+P2x
        hist2d2=hist2d2+hist2d2x
P2= P2/16
hist2d2= hist2d2/16
P2_im= np.clip(P2/4,0,1).astype('float32')
P2_im= cv.cvtColor(P2_im, cv.COLOR_GRAY2RGB)
cv.line(P2_im,[ksize//2, 0],[ksize//2, ksize],(1,.5,0),1)
cv.line(P2_im,[0, ksize//2],[ksize, ksize//2],(1,.5,0),1)
plt.subplot(246),plt.imshow(P2_im)
plt.title('Fourier Spectrum 2 (4x4 blocks)', fontsize=14), plt.axis('off')

# step6: show Log-Polar Fourier Spectrum 2
im_hist2d2= hist2d2[0:9,0:7]
#print(im_hist2d2.shape)
im_hist2d2= cv.resize(np.flipud(im_hist2d2.T),(180,160), interpolation=3)
im_hist2d2_mb= cv.copyMakeBorder(im_hist2d2,2,2,2,2,cv.BORDER_CONSTANT) #加黑邊寬
plt.subplot(247), plt.imshow(im_hist2d2_mb, cmap='gray', vmin=0, vmax=4)
plt.title('Polar Fourier Spectrum 2', fontsize=16), plt.axis('off')

# step7: show Polar Fourier Spectrum comparison
FFT_diff=2*(im_hist2d2-im_hist2d1)/np.max(im_hist2d2[:])
print(np.min(FFT_diff[:]),np.max(FFT_diff[:]))
idx1= np.where(FFT_diff<0)
idx2= np.where(FFT_diff>=0)
R= FFT_diff.copy() #注意，必須用 copy()，否則 R=G=B=FFT_diff 互相參考
R[idx1]= 0
G= -1.0*FFT_diff.copy()
G[idx2]= 0
B= -1.0*FFT_diff.copy()
B[idx2]= 0
FFT_diff_img = np.dstack((R,G,B))+0.5
FFT_diff_img_mb= cv.copyMakeBorder(FFT_diff_img,2,2,2,2,cv.BORDER_CONSTANT) #加黑邊寬
plt.subplot(248), plt.imshow(FFT_diff_img_mb)

# calcuate L2 dissimilarity (L2相異度計算)
diff  = hist2d2 - hist2d1
L2_dissimilarity = np.sqrt(np.mean(diff[:]**2))
print('L2 dissimilarity= ', np.round(L2_dissimilarity,3))
plt.title('L2 dissimilarity= '+ str(np.round(L2_dissimilarity,3)), fontsize=16), plt.axis('off')

#全螢幕顯示
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
plt.show()

