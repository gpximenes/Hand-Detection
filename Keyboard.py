from Key import BackSpace, Eraser, Key, Mode_key, SpaceBar
from time import perf_counter

class KeyBoard():
    def __init__(self, ini_pos ,key_size,mode,space=20 ) -> None:
        self.space = space + key_size

        self.mode = mode
        self.last_mode_change = 0

        self.key_texts = ['A','B','C','D','E','F','G','H','I','J',
                        'K','L','M','N','O','P','Q','R','S','T',
                             'U','V','W','X','Y','Z']

        self.rows_text,self.columns_text = (4,8)


        self.key_nums = ['1','2','3','4','5','6','7','8','9','0']

        self.rows_nums,self.columns_nums = (4,3)

        self.key_pos = []
        self.keys = []

        self.ini_pos = ini_pos

        



    def draw_keyboard(self, mode,img):
        if mode == 1:
            positions = self.generate_keys_pos(self.ini_pos, self.rows_text,self.columns_text)
            self.key_pos = positions
            self.draw_keys(self.key_pos, mode,img)
        if mode == 2:
            positions = self.generate_keys_pos(self.ini_pos, self.rows_nums,self.columns_nums)
            self.key_pos = positions
            self.draw_keys(self.key_pos, mode,img)
        



    def generate_keys_pos(self,ini_pos, rows, columns):
        positions = []
        xpos,ypos = ini_pos
        for i in range(rows):
            for j in range(columns):    
                positions.append((xpos + self.space * j, ypos))
            ypos = ypos + self.space
        return positions



    def update_colors(self,img):
        for key in self.keys:
            key.draw_key(img) 

    def change_keyboard_mode(self):
        timeout = 0.4

        deltaTime = perf_counter() - self.last_mode_change
        if deltaTime > timeout:
            if self.mode == 1:
                self.mode = 2
            elif self.mode == 2:
                self.mode = 1
            self.last_mode_change = perf_counter()
            

    
    def draw_keys(self,keys_pos, mode, img):
        self.keys = []

        if mode == 1 :
            texts = self.key_texts

            # Draw Keys
            for i,pos in (enumerate(keys_pos)):
                if i >= len(texts):
                    break
                x,y = pos
                self.keys.append(Key(texts[i],x,y))


            # Draw BackSpace Key
            ini_xpos, ini_ypos = keys_pos[0]
            backspace_pos = (ini_xpos + self.space * self.columns_text ,ini_ypos)
            self.keys.append(BackSpace(backspace_pos[0],backspace_pos[1],50,50))

            # Draw SpaceBar

            spaceBar_pos = (ini_xpos, ini_ypos  + self.space * self.rows_text)
            self.keys.append(SpaceBar(spaceBar_pos[0],spaceBar_pos[1], self.columns_text * self.space))

            # Draw Eraser 

            eraser_pos = (ini_xpos + self.space * self.columns_text ,ini_ypos + self.space * self.rows_text)
            self.keys.append(Eraser(eraser_pos[0],eraser_pos[1]))

            # Draw Mode Key

            mode_key_pos = (ini_xpos, ini_ypos - self.space)
            self.keys.append(Mode_key(mode_key_pos[0],mode_key_pos[1]))



        if mode == 2 :

            texts = self.key_nums
            # Draw Keys
            for i,pos in (enumerate(keys_pos)):
                if i >= len(texts):
                    break
                x,y = pos
                self.keys.append(Key(texts[i],x,y))

            # Draw BackSpace Key
            ini_xpos, ini_ypos = keys_pos[0]
            backspace_pos = (ini_xpos + self.space * self.columns_nums ,ini_ypos)
            self.keys.append(BackSpace(backspace_pos[0],backspace_pos[1],50,50))

            # Draw SpaceBar

            spaceBar_pos = (ini_xpos, ini_ypos  + self.space * self.rows_nums)
            self.keys.append(SpaceBar(spaceBar_pos[0],spaceBar_pos[1], self.columns_nums * self.space))

            # Draw Eraser 

            eraser_pos = (ini_xpos + self.space * self.columns_nums ,ini_ypos + self.space * self.rows_nums)
            self.keys.append(Eraser(eraser_pos[0],eraser_pos[1]))

            # Draw Mode Key

            mode_key_pos = (ini_xpos, ini_ypos - self.space)
            self.keys.append(Mode_key(mode_key_pos[0],mode_key_pos[1]))


        for key in self.keys:
            key.draw_key(img) 
        




        