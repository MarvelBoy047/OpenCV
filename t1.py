import cv2

'''cv2.IMREAD_COLOR – It specifies to load a color image. Any transparency of image will be neglected. It is the 
default flag. Alternatively, we can pass integer value 1 for this flag. cv2.IMREAD_GRAYSCALE – It specifies to load 
an image in grayscale mode. Alternatively, we can pass integer value 0 for this flag. cv2.IMREAD_UNCHANGED – It 
specifies to load an image as such including alpha channel. Alternatively, we can pass integer value -1 for this 
flag.'''
img = cv2.imread('assets/t1.jpg', 1)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)  # image resize
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('new_img.jpg', img)

cv2.imshow('Image', img)
cv2.waitKey(0)  # window display time 0= infinity
cv2.destroyWindow()
