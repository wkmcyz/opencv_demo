import cv2 as cv

if __name__ == '__main__':
    img = cv.imread('fly.png', 0)
    surf = cv.xfeatures2d.SURF_create(400)
    kp, des = surf.detectAndCompute(img, None)
    print(len(kp))
