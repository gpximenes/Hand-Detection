import cv2 
import mediapipe as mp


class Key():
    def __init__(self,text,x,y,width = 40, height = 40):
        self.color = (255, 51, 51) # blue
        self.width = width
        self.height = height
        
        self.x = x
        self.y = y
        
        self.text = text
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.font_size = 1.4

        self.is_pressed = False
        self.pressed_color = (0,255,0) # green

    def draw_key(self,img):

        if not self.is_pressed:
            cv2.rectangle(img, (self.x,self.y),(self.x + self.width,self.y + self.height), self.color, cv2.FILLED)
            cv2.putText(img,self.text, ( self.x + 5 , self.y + self.height - 5 ), self.font , self.font_size, (255,255,255), 2)
        if self.is_pressed:
            cv2.rectangle(img, (self.x,self.y),(self.x + self.width,self.y + self.height), self.pressed_color, cv2.FILLED)
            cv2.putText(img,self.text, ( self.x + 5 , self.y + self.height - 5 ), self.font , self.font_size, (255,255,255), 2)
          


