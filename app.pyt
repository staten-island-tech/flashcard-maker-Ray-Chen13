import json

class Teacher:
    def __init__(self, word, definition, image):
        self.word = word
        self.definition = definition
        self.image = image

    def display_info(self):
        return f"{self.word}: {self.definition}, {self.image}"
    
x = input("Would you like to enter Teacher or Student mode: ")

while x != "Teacher":
          
    
