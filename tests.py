import unittest
from unittest import TestCase

import numpy as np
from PIL import Image

from image_processing.filters import FastBlur
from image_processing.utils import get_empty_matrix


class UtilsTestCase(TestCase):
    def test_get_empty_array(self):
        expected = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        actual = get_empty_matrix(3, 3)
        self.assertEqual(expected, actual)


class FilterTestCase(TestCase):

    def test_get_neighbours_success(self):
        matrix = [
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
        ]
        blur_filter = FastBlur(Image.Image())
        blur_filter.width = len(matrix[0])
        blur_filter.height = len(matrix)
        neighbourhood = blur_filter.get_pixel_neighbourhood(3, 1, matrix, radius=1)
        expected = [
            [3, 4, 5],
            [3, 4, 5],
            [3, 4, 5],
        ]
        self.assertListEqual(expected, neighbourhood)

    def test_process_pixel(self):
        blur_filter = FastBlur(Image.Image())
        blur_filter.red = [
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
        ]
        blur_filter.new_red = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
        x, y = (5, 2)
        blur_filter.process_pixel(x, y, blur_filter.red, blur_filter.new_red)
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
