#! /usr/bin/python
import argparse
import cv2


def main():
    image_path = "../atlascar.png"
    img_rbg = cv2.imread(image_path)

    center_coordinates = (img_rbg.shape[1] / 2, img_rbg.shape[0] / 2)
    radius = 40
    color = (100, 0, 400)  # bgr color
    thickness = 2  # -1 fill the circle
    # com o circle estou mesmo a pintar na imagem, a imagem a partir daqui tem o circulo
    img_rbg_circle=cv2.circle(img_rbg, center_coordinates, radius, color, thickness)
    #cv2.imshow("Alinea a)", img_rbg_circle)

    print(img_rbg.shape)  # 360,640,3
    print (img_rbg.shape[1] / 2)  # 640
    print(type(img_rbg.shape))

    # adding text, put text returns an image

    text = "PARI 2020/2021"
    org = (10,40)
    font = cv2.FONT_ITALIC
    fontScale = 1
    color_text = (0,0,255)
    thickness = 2

    img_rbg_text = cv2.putText(img_rbg_circle,text,org,fontFace=font,fontScale=fontScale,color=color_text,thickness=thickness)
    cv2.imshow("Alinea b)", img_rbg_text)



    #adding text










    cv2.waitKey(0)


if __name__ == '__main__':
    main()
