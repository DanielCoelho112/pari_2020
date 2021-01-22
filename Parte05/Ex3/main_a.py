#! /usr/bin/python
import argparse
import cv2


'''
trackbar e util para o utilizador introduzir inputs
Whenever the user moves the Trackbar, the callback function on_trackbar is called
so e chamada essa, depois o codigo para, como metemos waitkey no fim ele fica sempre assim,
se definissemos algo para comecar no zero ele comecava la, mas nunca mais era lido
'''

# Global variables
window_name = 'window - Ex3a'
img_gray = None


def onTrackbar(threshold):
    # Add code here to threshold image_gray and show image in window
    global img_gray
    _, img_tresh = cv2.threshold(img_gray, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow(window_name,img_tresh)

def main():
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())
    '''

    image_path = "../atlascar.png"
    img_rgb = cv2.imread(image_path, 1)
    global img_gray # use global var
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv2.namedWindow(window_name)

    trackbar_name = 'TrackBar'

    cv2.createTrackbar(trackbar_name, window_name, 0, 255, onTrackbar)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()