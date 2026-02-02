import cv2
import numpy as np

class ImageModel:

    def load_image(self, path):
        return cv2.imread(path)

    def to_grayscale(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def sobel_filter(self, gray):
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        sobel = np.sqrt(sobelx**2 + sobely**2)
        sobel = np.uint8(np.clip(sobel, 0, 255))
        return sobel

    def threshold(self, img, thresh=100):
        _, th = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
        return th
