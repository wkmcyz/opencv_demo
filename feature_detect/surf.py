import cv2

if __name__ == '__main__':
    img = cv2.imread('img.png')
    surf = cv2.xfeatures2d.SURF_create(400)
    kp, des = surf.detectAndCompute(img, None)
    print(len(kp))
