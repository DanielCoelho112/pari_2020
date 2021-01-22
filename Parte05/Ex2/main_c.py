#! /usr/bin/python
import cv2
import numpy as np


def main():
    '''

    Cada pixel e representado por 3 valores (b,g,r) se for tudo 1 da branco, tudo 0 da pretp
    se for (0,1,0) da verde saturado ...

    '''

    image_path = "../atlascar2.png"
    img_rgb = cv2.imread(image_path, 1)
    print(type(img_rgb))
    print(img_rgb.shape)

    '''o split separa os 3 canais, ele retorna uma tuple com 3 elementos
     '''

    img_b, img_g, img_r = cv2.split(img_rgb)

    print(type(img_b))
    print(img_b.shape)
    print (img_b.dtype)


    # agora a que vamos binarizar

    _, img_b_tresh = cv2.threshold(img_b, 50, 255, cv2.THRESH_BINARY)
    _, img_g_tresh = cv2.threshold(img_g, 100, 255, cv2.THRESH_BINARY)
    _, img_r_tresh = cv2.threshold(img_r, 150, 255, cv2.THRESH_BINARY)


    #para voltar a termos 1 imagem rgb

    img_final = cv2.merge((img_b_tresh, img_g_tresh, img_r_tresh))

    cv2.imshow("Alinea c)",img_final)
    cv2.waitKey(0)







if __name__ == '__main__':
    main()