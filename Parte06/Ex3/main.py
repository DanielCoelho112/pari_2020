#! /usr/bin/python
import argparse
import cv2
import dlib
import numpy as np


def main():
    # initial setup

    falou = False
    falando = 0

    Area0 = 0
    Area1 = 0

    # Load the cascade
    detector = dlib.get_frontal_face_detector()

    # Load the predictor
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    # read the image
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()
        # print(frame.shape)  480,640,3

        # Convert image into grayscale
        gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)

        # Use detector to find landmarks
        faces = detector(gray)

        # como escolhi a primeira cara, se nao houver nenhuma tenho de colocar o try

        try:

            x1 = faces[0].left()  # left point
            y1 = faces[0].top()  # top point
            x2 = faces[0].right()  # right point
            y2 = faces[0].bottom()  # bottom point
            cv2.rectangle(img=frame, pt1=(x1, y1), pt2=(x2, y2), color=(255, 255, 255), thickness=2)
            mask = np.zeros((480, 640))
            mask[y1:y2, x1:x2] = 1
            mask = mask.astype(np.uint8) * 255

            print(mask.shape)

        except:

            x1 = 0
            y1 = 0
            x2 = 0
            y2 = 0
            mask = np.zeros((480, 640))
            mask[y1:y2, x1:x2] = 1
            mask = mask.astype(np.uint8) * 255
            print("No face detected")

        print(frame.shape)
        print(mask.dtype)

        img_add = frame.copy()

        # pintar a cara de verde

        cv2.add(frame, (0, 50, 0, 0), dst=img_add, mask=mask)

        # aplicar canny na imagem

        edges_img = cv2.Canny(gray, 20, 255)
        cv2.imshow(winname="Canny", mat=edges_img)

        # conversao do canny a branco para uma imagem rgb com com vermelho
        edges_color = cv2.merge((np.zeros(edges_img.shape).astype(np.uint8), np.zeros(edges_img.shape).astype(np.uint8),
                                 edges_img.astype(np.uint8)))
        cv2.imshow(winname="Red Canny", mat=edges_color)

        # mask representing everything except face
        mask_inv = 255 - mask

        img_add_2 = img_add.copy()

        print("tipo de dados do edges_color " + str(edges_color.dtype))
        print("tipo de dados do img_add_2 " + str(img_add_2.dtype))

        cv2.add(img_add, edges_color, dst=img_add_2, mask=mask_inv)
        cv2.imshow(winname="Frame plus red canny", mat=img_add_2)

        # Create landmark object
        # detecting mouth using points

        if len(faces) > 0:


            landmarks = predictor(image=gray, box=faces[0])

            # Loop through all the points

            #48,68

            print("Landmarks: " + str(landmarks))



            for n in range(0,68):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                cv2.circle(frame, (x, y), 4, (255, 0, 0), -1)




            for n in range(48,68):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)

            cv2.imshow(winname="Dots", mat=frame)

            #----------------------
            #----------------------


            x_lista = []
            y_lista = []
            x_y_lista = []

            for n in range(48, 68):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                x_lista.append(x)
                y_lista.append(y)

                x_y_lista.append((x,y))


        else:
            print("no face")
            x_lista = [0, 0]
            y_lista = [0, 0]


        falando = falando + 1


        #cv2.convexHull()


        img_add_3 = cv2.rectangle(img=img_add_2, pt1=(min(x_lista), min(y_lista)), pt2=(max(x_lista), max(y_lista)),
                                  color=(0, 0, 255), thickness=2)
        cv2.imshow(winname="Mouth with Canny", mat=img_add_3)
        Area = (max(x_lista) - min(x_lista)) * (max(y_lista) - min(y_lista))

        if (falou == True and falando > 40) or (falou == False):

            if Area > 1.3 * Area1 or Area < 0.70 * Area1:
                img_add_4 = cv2.putText(img_add_3, 'You are talking', (10, 40), fontFace=cv2.FONT_ITALIC, fontScale=1,
                                        color=(0, 0, 255),
                                        thickness=1)
                falou = True
                falando = 0

            else:
                img_add_4 = cv2.putText(img_add_3, 'You are not talking', (10, 40), fontFace=cv2.FONT_ITALIC,
                                        fontScale=1,
                                        color=(0, 255, 0),
                                        thickness=1)
                falou = False
                falando = 0
        else:
            img_add_4 = cv2.putText(img_add_3, 'You are talking', (10, 40), fontFace=cv2.FONT_ITALIC, fontScale=1,
                                    color=(0, 0, 255),
                                    thickness=1)

        cv2.imshow(winname="Speech Recognition", mat=img_add_4)
        Area1 = Area

        # Exit when escape is pressed
        if cv2.waitKey(delay=1) == 27:
            break

    # When everything done, release the video capture and video write objects
    cap.release()

    # Close all windows
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
