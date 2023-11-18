import cv2

imgpath = 'data/s.jpg'
img = cv2.imread(imgpath)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create(nfeatures=0, nOctaveLayers=3, contrastThreshold=0.04, edgeThreshold=10, sigma=1.6)
keypoints, descriptor = sift.detectAndCompute(gray,None)
img = cv2.drawKeypoints(image=img, outImage=img, keypoints = keypoints, flags = 4, color = (0, 255, 255))

cv2.imshow('sift_keypoints', img)
while (True):
  if cv2.waitKey(0) & 0xff == ord("q"):
    break
cv2.destroyAllWindows()
