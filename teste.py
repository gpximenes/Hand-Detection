import cv2 
import mediapipe as mp


class Key():
    def __init__(self,text):
        self.color = (255, 51, 51)
        self.width = 50
        self.height = 50
        self.text = text
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.font_size = 1.7

    def draw_key(self,img,x,y):
        self.x = x
        self.y = y
        cv2.rectangle(img, (self.x,self.y),(self.x + self.width,self.y + self.height), self.color, cv2.FILLED)
        cv2.putText(img,self.text, ( self.x + 5 , self.y + self.height - 5 ), self.font , self.font_size, (255,255,255), 2)




cap = cv2.imread('black.jpg')
cap = cap[0:480,0:640]
h, w, _ = cap.shape



key1 = Key("Q")
key1.draw_key(cap,50,50)




while True:
    cv2.imshow("Cap", cap)



    if cv2.waitKey(1) & 0xFF==ord('s') :
        break

