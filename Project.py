import cv2
from cvzone.HandTrackingModule import HandDetector

from keras.models import load_model

import numpy as np
import math

from subprocess32 import call

Gesture_names =  {0:'A',
                  1:'B',
                  2:'C',
                  3:'D',
                  4:'E',
                  5:'F',
                  6:'G',
                  7:'H',
                  8:'I',
                  9:'J',
                  10:'K',
                  11:'L',
                  12:'M',
                  13:'N',
                  14:'O'}

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
imgSize = 300
offset = 30
model = load_model("Model/train.h5")



while True:
    def answer(image1):
        image1 = np.array(image1, dtype='float32')
        image1 /= 255
        pred_array = model.predict(image1)
        print(f'pred_array: {pred_array}')
        result = Gesture_names[np.argmax(pred_array)]
        print(f'Result: {result}')
        print(max(pred_array[0]))
        Accuracy = float("%0.2f" % (max(pred_array[0]) * 100))
        print(result)
        return result, Accuracy

    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x,y,w,h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[abs(y-offset):abs(y+h+offset),abs(x-offset):abs(x+w+offset)]

        imgCropShape = imgCrop.shape


        Ratio = h/w
        try:
            if Ratio>1:
                k = imgSize/h
                wCal = math.ceil(k*w)
                imgReSize = cv2.resize(imgCrop,(wCal,imgSize))
                imgReSizeShape = imgReSize.shape
                wGap = math.ceil((imgSize-wCal)/2)
                imgWhite[:, wGap:wCal+wGap] = imgReSize


            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgReSize = cv2.resize(imgCrop, (imgSize, hCal))
                imgReSizeShape = imgReSize.shape
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap:hCal + hGap,:] = imgReSize

        except:
            pass
        #cv2.imshow('ImageCrop', imgCrop)
        #cv2.imshow('ImageWhite', imgWhite)
        try:
            target = cv2.resize(imgWhite, (100, 100))
            target = target.reshape(1, 100, 100, 3)
            pred, Accuracy = answer(target)
            print(Accuracy, pred)
            if (Accuracy >=0.9):
                cv2.putText(img, "Mean: " + pred, (20, 400), cv2.FONT_HERSHEY_SIMPLEX, 1.2,
                            (165, 250, 0), 4, lineType=cv2.LINE_AA)
            else:
                cv2.putText(img, "Try again", (20, 400), cv2.FONT_HERSHEY_SIMPLEX, 1.2,
                            (165, 250, 0), 4, lineType=cv2.LINE_AA)
        except:
            pass
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    if k == ord('p'):

        call(['python', 'Menu.py'])

        break

    cv2.imshow('Image',img)









