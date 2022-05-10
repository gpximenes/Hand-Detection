from itertools import count
from turtle import distance
import cv2 
import mediapipe as mp
import time
import math


cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()

mpDraw = mp.solutions.drawing_utils


tipIds = [4, 8, 12, 16, 20]


def get_distance(x1,y1,x2,y2):
    distance = math.hypot(x2 - x1, y2 - y1)
    return distance




count = 0
while True:
    sucess, img = cap.read()
    h, w, c = img.shape
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    Landmarks = []

    myHand = {}
    
    if(results.multi_hand_landmarks):
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            


        for id, lm in enumerate(handLms.landmark):
            px, py, pz = int(lm.x * w), int(lm.y * h), int(lm.z * w)
            Landmarks.append((id,px,py,pz))




    


    cv2.imshow("Cap", img)

    # if count == 5:
    #     for i in range(len(Landmarks)):
    #         print(i, Landmarks[i])
    #     count = 0
    # else:
    #     count = count + 1

    cv2.waitKey(1) or 0xFF == ord('S')

