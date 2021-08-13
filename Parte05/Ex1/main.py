#! /usr/bin/python
import argparse
import cv2

def main():

    #Ex1 a)
    #image_filename = '../atlascar.png'

    #Ex1 b)
    parser = argparse.ArgumentParser(description='full path of image')
    parser.add_argument('-fpi', '--full path', type=str, default="false", help='Path of image to read')
    args = vars(parser.parse_args())
    print(args)
    #image_filename = args['full path']

    #imread o valor 1 diz que se for a cores vem a cores


    #image = cv2.imread(image_filename, cv2.IMREAD_COLOR)  # Load an image

    #cv2.imshow('window', image)  # Display the image
    #cv2.waitKey(0) # wait for a key press before proceeding


    # Ex1c)

    while True:
        image_filename = '../atlascar.png'
        image = cv2.imread(image_filename, cv2.IMREAD_COLOR)
        cv2.imshow('window', image)
        cv2.waitKey(3000)
        image_filename = '../atlascar2.png'
        image = cv2.imread(image_filename, cv2.IMREAD_COLOR)
        cv2.imshow('window', image)

        #para guardar a key e fazer:

        key = cv2.waitKey(3000)


if __name__ == '__main__':
    main()