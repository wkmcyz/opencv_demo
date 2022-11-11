import cv2


def debug_show_img_and_wait_q(title: str, img):
    """
    用来调试的方法，展示指定的图片，并且阻塞程序一直到按下 'q' 键。
    """
    _debug = True
    if not _debug:
        return
    cv2.imshow(f"{title} Press 'q' to quit window to continue.", img)
    while cv2.waitKey(0) == ord('q'):
        return
