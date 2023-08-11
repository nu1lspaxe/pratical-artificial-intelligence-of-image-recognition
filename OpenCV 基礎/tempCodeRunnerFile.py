#用cv2.setMouseCallback建立滑鼠回應函式
cv2.setMouseCallback("draw", onMouse)
#等待
cv2.waitKey(0)