#! /usr/bin/python
import cv2
import numpy as np


def main():
    '''

        A mascara ja tenho, agora tenho de adicionar valor na componente vermelho dos pixeis pertencentes a mascara anterior
        Para adicionar Add
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
    print(mask.shape)
    print(mask.dtype)

    '''
    cv2.add vai somar a imagem dada aquelas componetes bgr para todos os pixeis, se so metermos um escalar ele soma o escalar em todo o lado
    
    '''
    img_add = img_rgb.copy()

    '''
    
    ao fazer issto estamos a tornar mais vermelho todos os pixels da imagem e nao so os pretendidos pela mascar
    
    cv2.add(img_rgb, (0, 0, 50, 0),dst=img_add)
    '''

    cv2.add(img_rgb, (-100, -100, 250, 0), dst=img_add,mask=mask)



    '''
    print(type(mask))
    print(mask.shape)
    print(mask.dtype)
    '''

    cv2.imshow("Alinea f)",img_add)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()