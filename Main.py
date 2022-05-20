import cv2
import mediapipe as mp
import math
from Handbox import Handbox
from Keyboard import KeyBoard
from TextBar import TextBar

def get_distance(x1,y1,x2,y2):
    distance = math.hypot(x2 - x1, y2 - y1)
    return distance

def detect_click(Landmarks,mode = 1,Threshold = 25):

    if Landmarks:
        if mode == 0: # Using Index fingertip and middle fingertip
            static_finger_ID = 8
            aux_finger_ID = 12 
        
        if mode == 1: # Using thumb fingertip and base of index finger
            static_finger_ID = 6
            aux_finger_ID = 4 

        if mode == 2:
            static_finger_ID = 12 # Using middle fingertip and thumb
            aux_finger_ID = 4 

        if mode == 3:
            static_finger_ID = 8 # Using middle fingertip and thumb
            aux_finger_ID = 4 

        index_X = Landmarks[static_finger_ID][1] 
        index_Y = Landmarks[static_finger_ID][2] 
        aux_X = Landmarks[aux_finger_ID][1] 
        aux_Y = Landmarks[aux_finger_ID][2] 
        distance = get_distance(index_X,index_Y,aux_X,aux_Y)
        if distance < Threshold:
            return True
        else:
            return False
    

def draw_cursor(img,mode,Landmarks):
    if Landmarks:
            if mode == 0: # Using Index fingertip and middle fingertip
                static_finger_ID = 8
                # aux_finger_ID = 12 
            
            if mode == 1: # Using thumb fingertip and base of index finger
                static_finger_ID = 8
                # aux_finger_ID = 4 

            if mode == 2:
                static_finger_ID = 8 # Using middle fingertip and thumb
                # aux_finger_ID = 4 

            if mode == 3:
                static_finger_ID = 8 # Using middle fingertip and thumb
                # aux_finger_ID = 4 

            index_X = Landmarks[static_finger_ID][1] 
            index_Y = Landmarks[static_finger_ID][2] 
            # aux_X = Landmarks[aux_finger_ID][1] 
            # aux_Y = Landmarks[aux_finger_ID][2] 

            cv2.circle(img,(index_X,index_Y),5,(0,255,0),-1)
            # cv2.circle(img,(aux_X,aux_Y)    ,5,(0,255,0),-1)
        

class Main():
    
    def click_key(self,click_pos):
        x_click, y_click = click_pos
        if self.Landmarks:
            for key in self.kb.keys:
                x,y = key.x,key.y
                width,height = key.width,key.height

                if x < x_click < x + width:
                    if y < y_click < y + height:
                        key.is_pressed = True
                        if key.type == 'text': 
                            self.textbar.add_letter(key.text)
                                              
                        if key.type == 'backspace':
                            self.textbar.remove_letter()
                               
                        if key.type == 'spacebar':
                            self.textbar.add_space()
                              
                        if key.type == 'eraser':
                            self.textbar.erase_all()
                               
                        
                            
                        


    def __init__(self) -> None:
        self.cap = cv2.VideoCapture(0)


        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils

        # self.box = Handbox()

        self.textbar = TextBar()

        self.click_mode = 1

        self.main()

    


    def main(self):

        
        while True:
            sucess, img = self.cap.read()
            if sucess:
                img = cv2.flip(img,1)
                h, w, _ = img.shape
                
                imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                results = self.hands.process(imgRGB)


                self.Landmarks = []



                # Draw Hand Landmarks
                if(results.multi_hand_landmarks):
                    for handLms in results.multi_hand_landmarks:
                        # self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
                        pass
                    
                    

                    for id, landmark in enumerate(handLms.landmark):
                        px, py = int(landmark.x * w), int(landmark.y * h)
                        self.Landmarks.append((id,px,py))

                    
                    



                # self.box.draw(self.Landmarks,img)

                self.kb = KeyBoard((50,50),img,40)


                draw_cursor(img,self.click_mode,self.Landmarks)




                if detect_click(self.Landmarks,1):
                    click_pos = (self.Landmarks[8][1],self.Landmarks[8][2])
                    self.click_key(click_pos)              
                    self.kb.update_colors()


                
                cv2.imshow("Cap", img)

                if cv2.waitKey(5) & 0xFF==ord('t') :
                    print(*self.textbar.text, sep="")


                if cv2.waitKey(5) & 0xFF==ord('s') :
                    self.cap.release()
                    cv2.destroyAllWindows()
                    break
                
            else:
                print("Can't get video frame, retrying...")
                self.cap.release()
                cv2.destroyAllWindows()





main = Main()
