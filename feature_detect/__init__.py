import logging

import cv2

from ability.opencv.contour import find_second_layer_contours
from ability.opencv.opencv_debug_utils import debug_show_img_and_wait_q
from chapter_case.case.word_1 import Word1Context

_logger = logging.getLogger("android_word_time_display_2_chapter")


def run_android_word_1_display_2(context: Word1Context):
    img = cv2.imread('img.png')

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    debug_show_img_and_wait_q("gray", img_gray)

    ret, thres = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)
    debug_show_img_and_wait_q("thres", thres)

    contours = find_second_layer_contours(thres)

    # contours, hierarchy = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cpy = img.copy()
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        click_x = int(x + w / 2)
        click_y = int(y + h / 2)
        cv2.drawMarker(cpy, (click_x, click_y), (0, 0, 255), thickness=3)
        cv2.rectangle(cpy, (x, y), (x + w, y + h), (0, 0, 255))
    cv2.drawContours(cpy, contours, -1, (0, 0, 255))
    debug_show_img_and_wait_q("cpy", cpy)


if __name__ == '__main__':
    run_android_word_1_display_2(None)
