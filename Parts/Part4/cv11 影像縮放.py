## cv11: 影像放大內插法的差異
import cv2
import numpy as np

img = cv2.imread('data/s.jpg')
height, width = img.shape[:-1]

#影像放大八倍
res1 = cv2.resize(img[250:300, 200:250, :], None, fx=8, fy=8, interpolation = cv2.INTER_NEAREST)
res2 = cv2.resize(img[250:300, 200:250, :], None, fx=8, fy=8,  interpolation = cv2.INTER_LINEAR)
res3 = cv2.resize(img[250:300, 200:250, :], None, fx=8, fy=8,  interpolation = cv2.INTER_CUBIC)
res=np.hstack((res1, res2, res3))
cv2.imshow('Nearest->Linear->Cubic interpolations', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
