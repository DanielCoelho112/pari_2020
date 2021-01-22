#! /usr/bin/python
import argparse
import cv2
import numpy as np


def main():
    # Ex1 a)
    # image_filename = '../atlascar.png'

    image_filename = '2020-11-10 14:24:26.407870canvas.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR)
    cv2.imshow('2', image)
    capture = cv2.VideoCapture(0)
    _, camera_image = capture.read()
    cv2.imshow('1', camera_image)

    mask_white = cv2.inRange(image, (254, 254, 254), (255, 255, 255))
    print(type(mask_white))
    mask=255-mask_white

    cv2.imshow('3', mask)
    mask=mask.astype(np.bool)
    copia=camera_image.copy()

    copia[mask] = image[mask]
    cv2.imshow('4', copia)

    key = cv2.waitKey(0)

    '''
    while True:
        
        cv2.imshow('window', image)
        cv2.waitKey(3000)
        image_filename = '../atlascar2.png'
        image = cv2.imread(image_filename, cv2.IMREAD_COLOR)
        cv2.imshow('window', image)

        #para guardar a key e fazer:

        
    '''


if __name__ == '__main__':
    main()
