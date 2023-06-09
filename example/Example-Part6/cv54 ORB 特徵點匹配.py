'''cv54: ORB(Oriented FAST and Rotated BRIEF) 特徵點匹配'''
import numpy as np
import cv2
from matplotlib import pyplot as plt

# query and test images
img1 = cv2.imread('data/s.jpg',0)
height, width = img1.shape
rotation_angle_degrees = 30
M = cv2.getRotationMatrix2D((width/2, height/2), rotation_angle_degrees, 1)
img2 = cv2.warpAffine(img1, M, (width, height), borderValue=255)

# create the ORB detector
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# brute force matching
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1,des2)

# Sort by distance.
matches = sorted(matches, key = lambda x:x.distance)
img3 = cv2.drawMatches(img1,kp1,img2,kp2, matches[:25], img2,flags=2)

plt.imshow(img3),plt.title('ORB feature-point matching')
plt.show()
