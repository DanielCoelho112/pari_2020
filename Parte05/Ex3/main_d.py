#! /usr/bin/python
import argparse
import cv2
import json
from functools import partial


'''
trackbar e util para o utilizador introduzir inputs
Whenever the user moves the Trackbar, the callback function on_trackbar is called
'''




def onTrackbarBmin(threshold,img_bgr,window_name,Limites):

    Limites['B']['min'] = threshold
    mask = cv2.inRange(img_bgr,(Limites['B']['min'],Limites['G']['min'],Limites['R']['min']),(Limites['B']['max'],Limites['G']['max'],Limites['R']['max']) )
    cv2.imshow(window_name,mask)

def onTrackbarBmax(threshold,img_bgr,window_name,Limites):

    Limites['B']['max'] = threshold
    mask = cv2.inRange(img_bgr,(Limites['B']['min'],Limites['G']['min'],Limites['R']['min']),(Limites['B']['max'],Limites['G']['max'],Limites['R']['max']) )
    cv2.imshow(window_name,mask)

def onTrackbarGmin(threshold,img_bgr,window_name,Limites):

    Limites['G']['min'] = threshold
    mask = cv2.inRange(img_bgr,(Limites['B']['min'],Limites['G']['min'],Limites['R']['min']),(Limites['B']['max'],Limites['G']['max'],Limites['R']['max']) )
    cv2.imshow(window_name,mask)

def onTrackbarGmax(threshold,img_bgr,window_name,Limites):

    Limites['G']['max'] = threshold
    mask = cv2.inRange(img_bgr,(Limites['B']['min'],Limites['G']['min'],Limites['R']['min']),(Limites['B']['max'],Limites['G']['max'],Limites['R']['max']) )
    cv2.imshow(window_name,mask)

def onTrackbarRmin(threshold,img_bgr,window_name,Limites):

    Limites['R']['min'] = threshold
    mask = cv2.inRange(img_bgr,(Limites['B']['min'],Limites['G']['min'],Limites['R']['min']),(Limites['B']['max'],Limites['G']['max'],Limites['R']['max']) )
    cv2.imshow(window_name,mask)

def onTrackbarRmax(threshold,img_bgr,window_name,Limites):

    Limites['R']['max'] = threshold
    mask = cv2.inRange(img_bgr,(Limites['B']['min'],Limites['G']['min'],Limites['R']['min']),(Limites['B']['max'],Limites['G']['max'],Limites['R']['max']) )
    cv2.imshow(window_name,mask)


def main():
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())
    '''

    Limites = {'B' : {'max' : 200, 'min' : 100},'G' : {'max' : 200, 'min' : 100},'R' : {'max' : 200, 'min' : 100}}


    '''
    print (Limites)

    print((Limites['B']['min']))
    '''


    window_name = "Ex3 b)"
    image_path = "../atlas2000_e_atlasmv.png"
    img_bgr = cv2.imread(image_path, 1)

    cv2.namedWindow(window_name)

    '''
    
    partial, 1 input: funcao que queresmos usar, o resto sao os parametros que sao diferentes,
    os outros sao todos iguais
    
    
    o myOnTrackBar continua a ser uma funcao, por isso a que ele pode ser chamada, mas e uma funcao
    como a ontrakbar, alias e a mesma, mas so com alguns parametros definidos de sitios diferentes, por exemplo
    o treshold foi passado logo e recebido, como nao dissemos nada relativo a ele nao a problema
    
    
    
    
    '''
    '''

    myOnTrackBar1 = partial(onTrackbar, img_gray=img_gray, window_name=window_name)
    myOnTrackBar2 = partial(onTrackbar, img_gray=img_gray, window_name=window_name)
    myOnTrackBar3 = partial(onTrackbar, img_gray=img_gray, window_name=window_name)
    '''

    trackbar_name_Bmin = 'Min B'
    trackbar_name_Bmax = 'Max B'
    trackbar_name_Gmin = 'Min G'
    trackbar_name_Gmax = 'Max G'
    trackbar_name_Rmin = 'Min R'
    trackbar_name_Rmax = 'Max R'

    myonTrackbarBmin = partial(onTrackbarBmin, img_bgr=img_bgr, window_name=window_name,Limites=Limites)
    myonTrackbarBmax = partial(onTrackbarBmax, img_bgr=img_bgr, window_name=window_name,Limites=Limites)
    myonTrackbarGmin = partial(onTrackbarGmin, img_bgr=img_bgr, window_name=window_name,Limites=Limites)
    myonTrackbarGmax = partial(onTrackbarGmax, img_bgr=img_bgr, window_name=window_name,Limites=Limites)
    myonTrackbarRmin = partial(onTrackbarRmin, img_bgr=img_bgr, window_name=window_name,Limites=Limites)
    myonTrackbarRmax = partial(onTrackbarRmax, img_bgr=img_bgr, window_name=window_name,Limites=Limites)


    cv2.createTrackbar(trackbar_name_Bmin, window_name, 0, 255, myonTrackbarBmin)
    cv2.createTrackbar(trackbar_name_Bmax, window_name, 0, 255, myonTrackbarBmax)
    cv2.createTrackbar(trackbar_name_Gmin, window_name, 0, 255, myonTrackbarGmin)
    cv2.createTrackbar(trackbar_name_Gmax, window_name, 0, 255, myonTrackbarGmax)
    cv2.createTrackbar(trackbar_name_Rmin, window_name, 0, 255, myonTrackbarRmin)
    cv2.createTrackbar(trackbar_name_Rmax, window_name, 0, 255, myonTrackbarRmax)




    #o ola e print a primeira vez, depois o codigo para o waitkey, atuando o callback function quando o evento ocorre

    print('ola')
    cv2.waitKey(0)

    file_name = 'limits.json'
    with open(file_name, 'w') as file_handle:
        print('writing dictionary Limites to file ' + file_name)
        json.dump(Limites, file_handle)  #Limits is a dictionary


if __name__ == '__main__':
    main()