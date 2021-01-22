#! /usr/bin/python
import cv2
import numpy as np


def main():
    '''
    agora e pegar na mascara e onde esta branco meter a cor original
        '''

    image_path = "../atlas2000_e_atlasmv.png"
    img_rgb = cv2.imread(image_path, 1)
    print(type(img_rgb))
    print(img_rgb.shape)

    '''    
    inrange vai buscar os pixels que fiquem dentro dos parametros, retorna a mascara
    '''
    BGRmin = (0, 80, 0)
    BGRmax = (60, 255, 60)

    mask = cv2.inRange(img_rgb, BGRmin, BGRmax)
    # print(mask)

    img_b, img_g, img_r = cv2.split(img_rgb)

    #assim mask para a ficar 0 ou 1,quando multiplicado os pixels ficam ou nao
    #nos sitios em que e 1, nao vai sofrer alteracoes, pois vai ficar igual


    img_b2 = cv2.multiply(img_b, mask / 255)
    img_g2 = cv2.multiply(img_g, mask / 255)
    img_r2 = cv2.multiply(img_r, mask / 255)



    img_final = cv2.merge((img_b2, img_g2, img_r2))

    '''
    print(type(mask))
    print(mask.shape)
    print(mask.dtype)
    '''

    cv2.imshow("Alinea h)", img_final)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()