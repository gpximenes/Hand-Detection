import cv2
import mediapipe as mp
import math
from handbox import Handbox

def get_distance(x1,y1,x2,y2):
    distance = math.hypot(x2 - x1, y2 - y1)
    return distance

def detect_click(Landmarks, Threshold = 20):
    index_finger_ID = 7
    middle_finger_ID = 11 

    index_X = Landmarks[index_finger_ID][1] 
    index_Y = Landmarks[index_finger_ID][2] 
    middle_X = Landmarks[middle_finger_ID][1] 
    middle_Y = Landmarks[middle_finger_ID][2] 
    distance = get_distance(index_X,index_Y,middle_X,middle_Y)
    if distance < Threshold:
        return True
    else:
        return False
    




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
        #print('Height: ',h ,' Width: ', w)
        
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)


        Landmarks = []
        X_list = []
        Y_list = []

        # Draw Hand Landmarks
        if(results.multi_hand_landmarks):
            for handLms in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
                


            for id, landmark in enumerate(handLms.landmark):
                px, py = int(landmark.x * w), int(landmark.y * h)
                Landmarks.append((id,px,py))
                X_list.append((id,px))
                Y_list.append((id,py))


            if detect_click(Landmarks):
                print("Click")


       
    

        box.draw(Landmarks,img)


        cv2.imshow("Cap", img)

        if cv2.waitKey(1) & 0xFF==ord('a') :
            print(box.get_area())


        if cv2.waitKey(1) & 0xFF==ord('s') :
            break

    else:
        print("Can't get video frame, retrying...")
        cap.release()
        cv2.destroyAllWindows()