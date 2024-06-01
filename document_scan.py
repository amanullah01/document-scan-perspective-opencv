import cv2
import numpy as np


def image_processing(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imageCanny = cv2.Canny(gray_image, 450, 600)

    kernel = np.ones((5, 5), np.uint8)
    image_dilation = cv2.dilate(imageCanny, kernel, iterations=2)
    image_erosion = cv2.erode(image_dilation, kernel, iterations=1)
    return image_erosion


def draw_contours(img):
    contours, hierarchy = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        cv2.drawContours(image_contours, cnt, -1, (0, 255, 0), 2)
        return image_contours


image = cv2.imread('./images/documentscanner2.jpg')
resized_image = cv2.resize(image, (500, 500))
image_contours = resized_image.copy()

processed_image = image_processing(resized_image)
contoursImage = draw_contours(processed_image)

cv2.imshow('image', resized_image)
cv2.imshow('Processed image', processed_image)
cv2.imshow('Contours image', contoursImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
