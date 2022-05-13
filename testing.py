import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread(
    'C:\\Users\\ariel\\Documents\\Python\\Python\\Queueing\\opencv_frame_0.jpeg')


def remove_noise(image):
    return cv2.medianBlur(image, 5)


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


img2 = get_grayscale(img)

h, w, c = img2.shape
boxes = pytesseract.image_to_boxes(img2)
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(
        img2, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('img2', img2)
cv2.waitKey(0)
