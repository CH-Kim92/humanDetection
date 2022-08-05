import cv2
from cv2 import RETR_TREE
from matplotlib.pyplot import contour
import numpy as np


cap = cv2.VideoCapture(1)
object_detection = cv2.createBackgroundSubtractorMOG2(
    history=100, varThreshold=30)

count = 0
while (cap.isOpened()):

    ret, frame = cap.read()

    hegith, width, _ = frame.shape

    # Extract region that I am interested

    region = frame[100:500, 530:950]
    # Obejct detection from background
    mask = object_detection.apply(region)

    # Delete the shadow .. more precise
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)

    # Contours
    contours, _ = cv2.findContours(
        mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    up = 0
    down = 0
    cc = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 700:
            x, y, w, h = cv2.boundingRect(cnt)
            cc += 1
            cv2.rectangle(region, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # The rectangle is up the line (<)
            if y < 250:
                up += 1
                exist = up
            else:
                down += 1
        if up > down and cc != up:
            count += up
            #cv2.drawContours(region, [cnt], -1, (0, 255, 0), 1)
    print(cc)
    cc = 0
    # Write text on the screen
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = "num person : {d}".format(d=count)
    cv2.putText(region,
                text,
                (50, 50),
                font, 1,
                (0, 255, 255),
                2,
                cv2.LINE_4)
    cv2.line(region, pt1=(0, 250), pt2=(1280, 250), color=(
        255, 255, 0), thickness=2, lineType=8, shift=0)
    cv2.imshow('cap', region)
    cv2.imshow('mask', mask)

    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
