#! /usr/bin/python
import cv2
from matplotlib import pyplot as plt

# openCV e uma ferramenta para processamento de imagens, visao artificial...

def main():
    img = cv2.imread('../atlascar.png', 0)
    #3 modos de leitura
    #1 color image
    #0 grayscale image
    #-1 inclui alpha channel

    cv2.imshow('Image',img)

    #image e o nome da figura

    cv2.waitKey(5000)

    #se nao pusermos waitkey ele fecha logo

    #cv2.waitKey() is a keyboard binding function. Its argument is the time in milliseconds. The function waits for specified milliseconds for any keyboard event. If you press any key in that time, the program continues. If 0 is passed, it waits indefinitely for a key stroke. It can also be set to detect specific key strokes like, if key a is pressed etc which we will discuss below.
    #se meter 5000 ele vai espera 5s ate carregar numa tecla, caso nao carregue ele segue o programa, se carregar logo, tambem segue




    cv2.destroyAllWindows()
    #so aqui a que se apagam todas as janelas de imagem

    cv2.imwrite('../write_image.png', img)
    #guarou a imagem img no diretorio atual com o nome write_image.png


    #mostra imagem, se carregar na letra esc salta fora, se for na s grava

    img_2 = cv2.imread('../atlascar.png', -1)
    cv2.imshow('image',img_2)
    k = cv2.waitKey(0)
    if k == 27:   #wait for ESC
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.imwrite('../nova_imagem.png', img_2)
        cv2.destroyAllWindows()

    #matplotlib is a plotting library, like plot in matlab, you can save, zoom ...

    img_3 = cv2.imread('../atlascar.png', 1)
    plt.imshow(img_3, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()


if __name__ == "__main__":
    main()