import unittest
import cv2
import numpy as np
from model import ImageModel


class TestImageModel(unittest.TestCase):

    def setUp(self):
        self.model = ImageModel()

        # buat dummy image 100x100 RGB
        self.img = np.random.randint(
            0, 255, (100, 100, 3), dtype=np.uint8
        )

    def test_grayscale(self):
        gray = self.model.to_grayscale(self.img)
        self.assertEqual(len(gray.shape), 2)
        self.assertEqual(gray.shape, (100, 100))

    def test_sobel_output_size(self):
        gray = self.model.to_grayscale(self.img)
        sobel = self.model.sobel_filter(gray)
        self.assertEqual(sobel.shape, gray.shape)

    def test_threshold_binary(self):
        gray = self.model.to_grayscale(self.img)
        th = self.model.threshold(gray, 120)

        unique_vals = np.unique(th)
        for v in unique_vals:
            self.assertIn(v, [0, 255])

    def test_load_image_invalid(self):
        img = self.model.load_image("not_exist.jpg")
        self.assertTrue(img is None)


if __name__ == "__main__":
    unittest.main()
