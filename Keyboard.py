from Key import BackSpace, Key

class KeyBoard():
    def __init__(self, ini_pos ,img,key_size,space=20 ) -> None:
        

        # self.key_texts = ['Q','W','E','R','T','Y','U','I','O','P',
        #                     'A','S','D','F','G','H','J','K','L',
        #                      'Z','X','C','V','B','N','M']

        self.key_texts = ['A','B','C','D','E','F','G','H','I','J',
                        'K','L','M','N','O','P','Q','R','S','T',
                             'U','V','W','X','Y','Z','M']

        self.rows,self.columns = (4,8)

        self.key_pos = []


        self.keys = []

        self.ini_pos = ini_pos

        self.img = img
        self.space = space + key_size

        self.draw_keyboard()



    def draw_keyboard(self):
        positions = self.generate_keys_pos(self.ini_pos)
        self.update_keys_pos(positions)
        self.draw_keys(self.key_pos)
        



    def generate_keys_pos(self,ini_pos):
        positions = []
        xpos,ypos = ini_pos
        for i in range(self.rows):
            for j in range(self.columns):    
                positions.append((xpos + self.space * j, ypos))
            ypos = ypos + self.space

        

       
        return positions


    def update_keys_pos(self,positions):
        self.key_pos = positions


    
    def draw_keys(self,key_pos):
        for i,pos in (enumerate(key_pos)):
            if i >= len(self.key_texts):
                break
            x,y = pos
            self.keys.append(Key(self.key_texts[i],x,y))

        ini_xpos, ini_ypos = key_pos[0]
        backspace_pos = (ini_xpos + self.space * (self.columns + 1) ,ini_ypos)

        self.keys.append(BackSpace(backspace_pos[0],backspace_pos[1],50,50))
        
        for key in self.keys:
            key.draw_key(self.img) 
        



    def update_colors(self):
        for key in self.keys:
            key.draw_key(self.img) 

    def draw_backSpace(self):
        ini_xpos,ini_ypos = self.ini_pos
        backspace_pos = (ini_xpos + self.space * (self.columns + 1) ,ini_ypos)
        x,y = backspace_pos
        self.backSpace = BackSpace(x,y)
        self.keys.append(self.backSpace)
        