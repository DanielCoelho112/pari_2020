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
    print(type(img_rgb))
    print(img_rgb.shape)
    '''
    cv2.imshow('test',img_rgb)
    cv2.waitKey(0)
    exit(0)
    '''

    '''    
    inrange vai buscar os pixels que fiquem dentro dos parametros, retorna a mascara
    '''
    BGRmin = (0,80,0)
    BGRmax = (60,255,60)

    mask = cv2.inRange(img_rgb,BGRmin,BGRmax)
    print(mask)

    print(type(mask))
    print(mask.shape)
    print(mask.dtype)

    cv2.imshow("Alinea d)",mask)
    cv2.waitKey(0)







if __name__ == '__main__':
    main()