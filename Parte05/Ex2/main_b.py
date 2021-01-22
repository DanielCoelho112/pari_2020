#! /usr/bin/python
import cv2
import numpy as np


def main():
    '''
    #cv e o mais facil para trabalhar com image processing
    no imread o valor 1 significa que vem como estava
    '''

    image_path = "../atlascar.png"
    img_rgb = cv2.imread(image_path, 1)
    print(type(img_rgb))
    print(img_rgb.shape)
    '''depois de ler com o cv2 a imagem passa a ser um array multidimensional
     com 360x640x3     

     o tipo de elemento e unit8, logo cada elemento vai de 0 a 255

     Antes de a binarizar e necessario passar para gray
     '''
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    print(type(img_gray))
    print(img_gray.shape)
    print(img_gray.dtype)

    # agora a que vamos binarizar

    '''quando temos de definir uma variavel mas sabemos que nunca a vamos usar, escrevemos _
    127 e o valor do treshold, 255 e o valor para onde fica, ou seja se o pixel tiver mais de 127 fica com 255

    '''


    #Em vez do cv2 treshold vamos usar o numpy

    #_, img_tresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

    treshold = 100

    img_tresh = img_gray > treshold

    print(img_tresh.dtype)
    '''
    como fiz uma comparacao o tipo de cada elemento e bool, e o imshow nao lida com isso
    
    estou a converter o true e false para 1 e 0, e depois multiplicando por 255, para ficar de acordo
    
    '''

    img_np_tresh = img_tresh.astype(np.uint8) * 255


    cv2.imshow("Alinea b)",img_np_tresh)



    cv2.waitKey(0)







if __name__ == '__main__':
    main()