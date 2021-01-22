#! /usr/bin/python
import argparse
import cv2
import numpy as np
from functools import partial

# global variable
drawing = False
color_ = (0, 0, 0)


def onMouse(event, x, y, s, p, image):
    global drawing
    global color_

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        print("X Mouse Position: " + str(x) + " Y Mouse Position: " + str(y))


    if event == cv2.EVENT_MOUSEMOVE and drawing == True:
        image_circle = cv2.circle(image, (x, y), 5, color_, -1)
        cv2.imshow('Paint', image_circle)

    if event == cv2.EVENT_LBUTTONUP:
        drawing = False


def main():
    global color_


    drawing = False

    quadro_size = (400, 600,3)
    quadro = np.ones(quadro_size)
    quadro = np.multiply(quadro, 255)

    window_name = 'Paint'

    img_rbg = cv2.imshow('Paint', quadro)

    myonMouse = partial(onMouse, image=quadro)

    cv2.setMouseCallback(window_name, myonMouse)



    while True:
        key = cv2.waitKey(0)
        if chr(key) == 'r':
            color_ = (0,0,255)
            quadro=cv2.rectangle(quadro, (0,0), (200,50), (255,255,255), -1)
            quadro = cv2.putText(quadro, 'red color', (10,40), fontFace=cv2.FONT_ITALIC, fontScale=1, color=(0,0,255),
                                       thickness=1)
            cv2.imshow("Paint", quadro)
        elif chr(key) == 'g':
            color_ = (0, 255, 0)
            quadro = cv2.rectangle(quadro, (0, 0), (200, 50), (255, 255, 255), -1)
            quadro = cv2.putText(quadro, 'green color', (10, 40), fontFace=cv2.FONT_ITALIC, fontScale=1,
                                 color=(0, 255, 0),
                                 thickness=1)
            cv2.imshow("Paint", quadro)
        elif chr(key) == 'b':
            color_ = (255 ,0, 0)
            quadro = cv2.rectangle(quadro, (0, 0), (200, 50), (255, 255, 255), -1)
            quadro = cv2.putText(quadro, 'blue color', (10, 40), fontFace=cv2.FONT_ITALIC, fontScale=1,
                                 color=(255, 0, 0),
                                 thickness=1)
            cv2.imshow("Paint", quadro)

        elif chr(key) == ' ':
            break


if __name__ == '__main__':
    main()
