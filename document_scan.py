import cv2
import numpy as np

image = cv2.imread('./images/documentscanner2.jpg')
resized_image = cv2.resize(image, (500, 500))

cv2.imshow('image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
