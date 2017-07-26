__author__ = 'Foleevora'

import numpy as np
import cv2

def showVideo():
    # 1. 웹캠 구동
    try:
        print('카메라를 구동합니다.')
        cap = cv2.VideoCapture(0)
    except:
        print('카메라 구동 실패')
        return

    cap.set(3, 480)
    cap.set(4, 320)

    while True:
        ret, frame = cap.read()

        if not ret:
            print('비디오 읽기 오류')
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    # 2. 동영상 재생
    # try:
    #     print('동영상을 재생합니다.')
    #     cap = cv2.VideoCapture('videos/video.mp4')
    # except:
    #     print('동영상 재생 실패')
    #     return
    #
    # while True:
    #     ret, frame = cap.read()
    #
    #     if not ret:
    #         print('동영상 읽기 오류')
    #         break
    #
    #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #     cv2.imshow('frame', gray)
    #
    #     k = cv2.waitKey(1) & 0xFF
    #     if k == 27:
    #         break
    #
    # cap.release()
    # cv2.destroyAllWindows()

showVideo()
