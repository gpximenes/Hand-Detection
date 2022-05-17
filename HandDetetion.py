from turtle import update, width
import cv2
import mediapipe as mp
import math
from handbox import Handbox
from Keyboard import KeyBoard

def get_distance(x1,y1,x2,y2):
    distance = math.hypot(x2 - x1, y2 - y1)
    return distance

def detect_click(Landmarks, Threshold = 25, mode = 0):

    if Landmarks:
        if mode == 1: # Using Index fingertip and middle fingertip
            static_finger_ID = 8
            aux_finger_ID = 12 
        
        if mode == 0: # Using thumb fingertip and base of index finger
            static_finger_ID = 5
            aux_finger_ID = 4 

        index_X = Landmarks[static_finger_ID][1] 
        index_Y = Landmarks[static_finger_ID][2] 
        middle_X = Landmarks[aux_finger_ID][1] 
        middle_Y = Landmarks[aux_finger_ID][2] 
        distance = get_distance(index_X,index_Y,middle_X,middle_Y)
        if distance < Threshold:
            return True
        else:
            return False
    

def click_key(click_pos):
    x_click, y_click = click_pos


    if Landmarks:
        for key in kb.keys:
            x,y = key.x,key.y
            width,height = key.width,key.height

            if x < x_click < x + width:
                if y < y_click < y + height:
                    key.is_pressed = True


cap = cv2.VideoCapture(0)



mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


box = Handbox()


COLOR = (255, 51, 51)

while True:
    sucess, img = cap.read()
    if sucess:
        img = cv2.flip(img,1)
        h, w, _ = img.shape
        
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)


        Landmarks = []
        X_list = []
        Y_list = []

        # Draw Hand Landmarks
        if(results.multi_hand_landmarks):
            for handLms in results.multi_hand_landmarks:
                # mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
                pass


            for id, landmark in enumerate(handLms.landmark):
                px, py = int(landmark.x * w), int(landmark.y * h)
                Landmarks.append((id,px,py))
                X_list.append((id,px))
                Y_list.append((id,py))



        box.draw(Landmarks,img)

        kb = KeyBoard((50,50),img, 40)



        if detect_click(Landmarks):
            click_pos = (Landmarks[8][1],Landmarks[8][2])
            print("Click on pos:", click_pos)
            click_key(click_pos)


        
        kb.update_colors()


        
        cv2.imshow("Cap", img)

        if cv2.waitKey(1) & 0xFF==ord('a') :
            print(box.get_area())


        if cv2.waitKey(1) & 0xFF==ord('s') :
            cap.release()
            cv2.destroyAllWindows()
            break
            

    else:
        print("Can't get video frame, retrying...")
        cap.release()
        cv2.destroyAllWindows()