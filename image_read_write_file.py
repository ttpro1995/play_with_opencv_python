__author__ = "Thai Thien"
__email__ = "tthien@apcs.vn"

import cv2
import os
from os import path
import numpy as np

source_path = "source_image"
output_path = "output_image"


def read_and_write_image():
    image = cv2.imread(path.join(source_path, 'dd1.jpg'))
    cv2.imwrite(path.join(output_path, 'dd1.jpg'), image)


def read_as_grayscale_and_write():
    image = cv2.imread(path.join(source_path, 'dd1.jpg'),
                       cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(path.join(output_path, 'dd1_gray.jpg'), image)


def generate_random_gray_image():
    randomByteArr = bytearray(os.urandom(120000))
    flatNpArr = np.array(randomByteArr)

    # convert to 400x300
    grayImage = flatNpArr.reshape(300, 400)
    cv2.imwrite(path.join(output_path, "random_gray.png"), grayImage)

    # convert to 400x100 color image
    bgrImage = flatNpArr.reshape(100, 400, 3)
    cv2.imwrite(path.join(output_path, "random_color.png"), bgrImage)


def read_and_change_the_pixel():
    image = cv2.imread(path.join(source_path, 'dd1.jpg'))
    print(image.item(150, 120, 0))
    image.itemset((150, 120, 0), 255)
    print(image.item(150, 120, 0))


def green_to_zero():
    image = cv2.imread(path.join(source_path, 'dd1.jpg'))
    image[:, :, 1] = 0
    cv2.imwrite(path.join(output_path, "zero_green.png"), image)


def get_roi():
    image = cv2.imread(path.join(source_path, 'dd1.jpg'))
    my_roi = image[170:400, 60:400]
    cv2.imwrite(path.join(output_path, "roi.png"), my_roi)


def put_roi_into_image():
    image = cv2.imread(path.join(source_path, 'dd1.jpg'))
    my_roi = image[170:400, 60:400]
    image[0:230, 160:500] = my_roi
    cv2.imwrite(path.join(output_path, "image_with_roi.png"), image)


if __name__ == "__main__":
    put_roi_into_image()
