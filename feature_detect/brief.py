import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

from base import debug_show_img_and_wait_q

if __name__ == '__main__':
    img = cv.imread('img.png')
    cpy = img.copy()
    # Initiate FAST detector
    star = cv.xfeatures2d.StarDetector_create()
    # Initiate BRIEF extractor
    brief = cv.xfeatures2d.BriefDescriptorExtractor_create()
    # find the keypoints with STAR
    kp = star.detect(img, None)
    # compute the descriptors with BRIEF
    kp, des = brief.compute(img, kp)
    for k in kp:
        print(k)
        # cv.drawMarker(cpy, kp, (0, 0, 255))
    # debug_show_img_and_wait_q("kp", cpy)
    print(brief.descriptorSize())
    print(des.shape)
