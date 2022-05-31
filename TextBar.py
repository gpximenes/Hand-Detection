import os
from time import perf_counter


class TextBar():
    def __init__(self) -> None:

        self.text = []

        self.last_key = ""
        self.time_last_click = 0
        self.deltaTime = None

        self.timeout = 0.5
        os.system('cls')


    def add_letter(self,letter):
        if not self.text:
            self.text.append(letter)
            print(*self.text,sep='')
            return 

        if self.text[- 1] != letter:
            self.text.append(letter)
            os.system('cls')
            print(*self.text,sep='')
            return 

        if self.text[-1] == letter:
            self.text.append(letter)
            os.system('cls')
            print(*self.text,sep='')
        else:
            return 

    def remove_letter(self):
        try: 
                self.text.pop()
                os.system('cls')
                print(*self.text,sep='')
        except:
            pass

    def add_space(self):
            self.text.append(" ")
            os.system('cls')
            print(*self.text,sep='')


    def erase_all(self):
        self.text.clear()
        os.system('cls')
        print(*self.text,sep='')
        
        

        
        

