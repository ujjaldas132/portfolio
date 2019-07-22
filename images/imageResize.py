import cv2
filename="g6.jpg"
img=cv2.imread(filename)
img=cv2.resize(img,(640,426))
cv2.imwrite(filename,img)
