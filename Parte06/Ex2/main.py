#! /usr/bin/python
import cv2


def main():
    # ---------------
    # initial setup
    # ---------------
    window_name = 'A5-Ex2'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
    capture = cv2.VideoCapture(0)  # 0 is the camara's index

    # ---------------
    # program's body
    # ---------------
    while True:
        _, image = capture.read()
        cv2.imshow(window_name, image)
        key = cv2.waitKey(1)
        # if chr(key) == ' ':
        #     break

    # ---------------
    # program's end
    # ---------------
    cv2.destroyAllWindows()
    capture.release()


if __name__ == '__main__':
    main()
