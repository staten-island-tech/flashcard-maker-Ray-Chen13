import json

def save_flashcards(flashcards_data):
    with open("FlashCards.json", "w") as file:
        json.dump(flashcards_data, file, indent=4)  
    try:
        with open("FlashCards.json", "r") as file:
            return json.file(file)
    except FileNotFoundError:
        return []
    
x = input("Would you like to enter Teacher or Student mode: ")

while x != "Exit":
    if x == "Teacher":      
        class Teacher:
            def __init__(self, word, definition, image):
                self.word = word
                self.definition = definition
                self.image = image

            def display_info(self):
                return f"{self.word}: {self.definition}, {self.image}"
            words = input("Tell me a word: "), input("Give me an answer: ")
    break