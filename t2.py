import random

import cv2

img = cv2.imread('assets/t1.jpg', 1)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)  # image resize
# for i in  range(100):    # img modification(randomizing number of pixels)
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
tag = img[500:700, 600:900]
img[100:300, 650:950] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)  # window display time 0= infinity
cv2.destroyWindow()
