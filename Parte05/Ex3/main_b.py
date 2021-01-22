#! /usr/bin/python
import argparse
import cv2
from functools import partial


'''
trackbar e util para o utilizador introduzir inputs
Whenever the user moves the Trackbar, the callback function on_trackbar is called
'''
# Global variables


def onTrackbar(threshold,img_gray,window_name):
    # Add code here to threshold image_gray and show image in window
    _, img_tresh = cv2.threshold(img_gray, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow(window_name,img_tresh)

def main():
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())
    '''
    window_name = "Ex3 b)"
    image_path = "../atlascar.png"
    img_rgb = cv2.imread(image_path, 1)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv2.namedWindow(window_name)

    '''
    
    partial, 1 input: funcao que queresmos usar, o resto sao os parametros que sao diferentes,
    os outros sao todos iguais
    
    
    o myOnTrackBar continua a ser uma funcao, por isso a que ele pode ser chamada, mas e uma funcao
    como a ontrakbar, alias e a mesma, mas so com alguns parametros definidos de sitios diferentes, por exemplo
    o treshold foi passado logo e recebido, como nao dissemos nada relativo a ele nao a problema
    
    
    
    
    '''

    myOnTrackBar = partial(onTrackbar, img_gray=img_gray, window_name=window_name)

    trackbar_name = 'TrackBar'

    cv2.createTrackbar(trackbar_name, window_name, 0, 255, myOnTrackBar)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()