import cv2 
import pyautogui


class Key():
    def __init__(self,text,x,y,width = 50, height = 50):
        
        self.type = 'text'

        self.width = width
        self.height = height
        
        self.x = x
        self.y = y
        
        self.text = text
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.font_size = 1.4

        self.is_pressed = False
        self.color = (255, 51, 51) # blue
        self.pressed_color = (0,255,0) # green

    def draw_key(self,img):

        if not self.is_pressed:
            cv2.rectangle(img, (self.x,self.y),(self.x + self.width,self.y + self.height), self.color, cv2.FILLED)
            cv2.putText(img,self.text, ( self.x + 5 , self.y + self.height - 5 ), self.font , self.font_size, (255,255,255), 2)
        if self.is_pressed:
            cv2.rectangle(img, (self.x,self.y),(self.x + self.width,self.y + self.height), self.pressed_color, cv2.FILLED)
            cv2.putText(img,self.text, ( self.x + 5 , self.y + self.height - 5 ), self.font , self.font_size, (255,255,255), 2)


    def press_key(self):
        pyautogui.press(self.text)

          

class BackSpace():
    def __init__(self, x, y, width=50, height=50):

        self.type = 'backspace'

        self.width = width
        self.height = height
        
        self.x = x
        self.y = y
        
        self.text = '*'
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.font_size = 1.4
        self.text_color = (255,255,255)

        self.is_pressed = False
        self.color = (255, 51, 51) # Blue
        self.pressed_color = (0,0,255) # Red

    def draw_key(self,img):

        if not self.is_pressed:
            cv2.rectangle(img, (self.x,self.y),(self.x + self.width,self.y + self.height), self.color, cv2.FILLED)
            cv2.putText(img,self.text, ( self.x + 5 , self.y + self.height - 5 ), self.font , self.font_size, self.text_color, 2)
        if self.is_pressed:
            cv2.rectangle(img, (self.x,self.y),(self.x + self.width,self.y + self.height), self.pressed_color, cv2.FILLED)
            cv2.putText(img,self.text, ( self.x + 5 , self.y + self.height - 5 ), self.font , self.font_size, self.text_color, 2)

    def press_key(self):
        pyautogui.press('backspace')
 
class SpaceBar():
    def __init__(self, x, y, width=200, height=50):

        self.type = 'spacebar'

        self.width = width
        self.height = height
        
        self.x = x
        self.y = y
        
        self.text = ' '
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.font_size = 1.4
        self.text_color = (255,255,255)

        self.is_pressed = False
        self.color = (255, 51, 51) # Blue
        self.pressed_color = (0,255,0) # Green

    def draw_key(self,img):

        if not self.is_pressed:
            cv2.rectangle(img, (self.x,self.y),(self.x + self.width,self.y + self.height), self.color, cv2.FILLED)
            cv2.putText(img,self.text, ( self.x + 5 , self.y + self.height - 5 ), self.font , self.font_size, self.text_color, 2)
        if self.is_pressed:
            cv2.rectangle(img, (self.x,self.y),(self.x + self.width,self.y + self.height), self.pressed_color, cv2.FILLED)
            cv2.putText(img,self.text, ( self.x + 5 , self.y + self.height - 5 ), self.font , self.font_size, self.text_color, 2)

    def press_key(self):
        pyautogui.press('space')
 


class Eraser():
    def __init__(self, x, y, width=50, height=50):

        self.type = 'eraser'

        self.width = width
        self.height = height
        
        self.x = x
        self.y = y
        
        self.text = 'X'
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.font_size = 1.4

        self.is_pressed = False
        self.color = (0, 0, 255) # Red
        self.pressed_color = (0,255,0) # Green
        self.text_color = (0,0,0)

    def draw_key(self,img):

        if not self.is_pressed:
            cv2.rectangle(img, (self.x,self.y),(self.x + self.width,self.y + self.height), self.color, cv2.FILLED)
            cv2.putText(img,self.text, ( self.x + 5 , self.y + self.height - 5 ), self.font , self.font_size, self.text_color, 2)
        if self.is_pressed:
            cv2.rectangle(img, (self.x,self.y),(self.x + self.width,self.y + self.height), self.pressed_color, cv2.FILLED)
            cv2.putText(img,self.text, ( self.x + 5 , self.y + self.height - 5 ), self.font , self.font_size, self.text_color, 2)
    def press_key(self):
        pyautogui.hotkey('ctrl','a','delete')

class Mode_key():
    def __init__(self, x, y, width=60, height=60):

        self.type = 'mode'

        self.width = width
        self.height = height
        
        self.x = x
        self.y = y
        
        self.text = 'KB'
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.font_size = 1.4

        self.is_pressed = False
        self.color = (0, 0, 255) # Red
        self.pressed_color = (0,255,0) # Green
        self.text_color = (0,0,0)

    def draw_key(self,img):

        if not self.is_pressed:
            cv2.rectangle(img, (self.x,self.y),(self.x + self.width,self.y + self.height), self.color, cv2.FILLED)
            cv2.putText(img,self.text, ( self.x + 5 , self.y + self.height - 5 ), self.font , self.font_size, self.text_color, 2)
        if self.is_pressed:
            cv2.rectangle(img, (self.x,self.y),(self.x + self.width,self.y + self.height), self.pressed_color, cv2.FILLED)
            cv2.putText(img,self.text, ( self.x + 5 , self.y + self.height - 5 ), self.font , self.font_size, self.text_color, 2)



class CapsLock():
    def __init__(self, x, y, width=70, height=50):

        self.type = 'capslock'

        self.width = width
        self.height = height
        
        self.x = x
        self.y = y
        
        self.text = 'CpLk'
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.font_size = 0.75

        self.is_pressed = False
        self.color = (0, 0, 255) # Red
        self.pressed_color = (0,255,0) # Green
        self.text_color = (0,0,0)

    def draw_key(self,img):

        if not self.is_pressed:
            cv2.rectangle(img, (self.x,self.y),(self.x + self.width,self.y + self.height), self.color, cv2.FILLED)
            cv2.putText(img,self.text, ( self.x + 5 , self.y + self.height - 5 ), self.font , self.font_size, self.text_color, 2)
        if self.is_pressed:
            cv2.rectangle(img, (self.x,self.y),(self.x + self.width,self.y + self.height), self.pressed_color, cv2.FILLED)
            cv2.putText(img,self.text, ( self.x + 5 , self.y + self.height - 5 ), self.font , self.font_size, self.text_color, 2)

