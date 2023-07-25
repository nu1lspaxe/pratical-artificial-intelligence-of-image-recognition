'''cv53: SIFT特徵點匹配'''
import cv2
from matplotlib import pyplot as plt

trainingImage = cv2.imread('data/s.jpg',0)
height, width = trainingImage.shape
rotation_angle_degrees = 30
M = cv2.getRotationMatrix2D((width/2, height/2), rotation_angle_degrees, 1)
queryImage = cv2.warpAffine(trainingImage, M, (width, height), borderValue=255)

# create SIFT and detect/compute
sift = cv2.xfeatures2d.SIFT_create(nfeatures=200, nOctaveLayers=3, contrastThreshold=0.04, edgeThreshold=10, sigma=1.6)
kp1, des1 = sift.detectAndCompute(queryImage,None) #kp: keypoint, des: sift descriptor
kp2, des2 = sift.detectAndCompute(trainingImage,None)
print('len(kp1)=',len(kp1))
print('des1.shape=',des1.shape)

# FLANN matcher parameters
# FLANN_INDEX_KDTREE = 0
indexParams = dict(algorithm = 0, trees = 5)
searchParams = dict(checks=50)   # or pass empty dictionary

flann = cv2.FlannBasedMatcher(indexParams,searchParams)

matches = flann.knnMatch(des1,des2,k=2)
print('len(matches)=',len(matches))

# prepare an empty mask to draw good matches
matchesMask = [[0,0] for i in range(len(matches))]

# David G. Lowe's ratio test, populate the mask
for i,(m,n) in enumerate(matches):
    if m.distance < 0.7*n.distance:
        matchesMask[i]=[1,0]

drawParams = dict(matchColor = (0,255,0),
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask,
                   flags = 0)

resultImage = cv2.drawMatchesKnn(queryImage,kp1,trainingImage,kp2,matches,None,**drawParams)

plt.imshow(resultImage,), plt.title('SIFT feature-point matching')
plt.show()