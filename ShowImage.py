__author__ = "Foleevora"

import numpy as np
import cv2
import matplotlib.pyplot as plt

def showImage():
    # 1. 이미지 로드
    # imgfile = 'images/logo.jpg'
    # img = cv2.imread(imgfile, cv2.IMREAD_COLOR)

    # cv2.namedWindow('logo', cv2.WINDOW_NORMAL)
    # cv2.imshow('logo', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # 2. 이미지 복사
    # imgfile = 'images/logo.jpg'
    # img = cv2.imread(imgfile, cv2.IMREAD_COLOR)
    # cv2.imshow('logo', img)
    #
    # k = cv2.waitKey(0) & 0xFF
    #
    # if k == 27:
    #     cv2.destroyAllWindows()
    # elif k == ord('c'):
    #     cv2.imwrite('images/logo_copy.jpg', img)
    #     cv2.destroyAllWindows()

    # 3. matplotlib를 이용하여 이미지 로드
    # imgfile = 'images/logo.jpg'
    # img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)
    #
    # plt.imshow(img, cmap='gray', interpolation='bicubic')
    # plt.xticks([])
    # plt.yticks([])
    # plt.title('logo')
    # plt.show()

showImage()
