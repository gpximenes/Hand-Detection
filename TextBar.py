
from time import perf_counter


class TextBar():
    def __init__(self) -> None:

        self.text = []

        self.last_key = ""
        self.time_last_click = None
        self.deltaTime = None

        self.timeout = 1


    def add_letter(self,letter):
        if not self.text:
            self.text.append(letter)
            self.time_last_click = perf_counter()
            return

        if self.text[- 1] != letter:
            self.text.append(letter)
            self.time_last_click = perf_counter()
            return

        deltaTime = perf_counter() - self.time_last_click 
        if self.text[-1] == letter and deltaTime >  self.timeout:
            self.text.append(letter)
            self.time_last_click = perf_counter()
        
        else:
            return

        

        
        

