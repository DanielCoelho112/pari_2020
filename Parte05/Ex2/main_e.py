#! /usr/bin/python
import cv2
import numpy as np


def main():
    '''

    Cada pixel e representado por 3 valores (b,g,r) se for tudo 1 da branco, tudo 0 da pretp
    se for (0,1,0) da verde saturado ...

    '''

    image_path = "../atlas2000_e_atlasmv.png"
    img_rgb = cv2.imread(image_path, 1)
    img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)


    HSVmin = (255/4 - 20,50,50)
    HSVmax = (255/4 + 20,255,255)

    mask = cv2.inRange(img_hsv,HSVmin,HSVmax)
    print(mask)

    print(type(mask))
    print(mask.shape)
    print(mask.dtype)

    cv2.imshow("Alinea e)",mask)
    cv2.waitKey(0)







if __name__ == '__main__':
    main()