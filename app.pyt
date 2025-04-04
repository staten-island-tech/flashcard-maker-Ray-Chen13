import json
    
x = input("Would you like to enter Teacher or Student mode: ")

class Flashcards:
        def __init__(self, word, answer):
            self.word = word
            self.answer = answer

        def display_info(self):
            return {"Question": self.word}, {"Answer": self.answer}
        
if x == "Teacher":
    class Teacher:
        def __init__(self, word, answer):
            self.word = word
            self.answer = answer
    x = Flashcards(input("Tell me a word: "), input("Give me an answer: "))

    try:
        with open("flashcards.json", "r") as file:
            flashcards_data = json.load(file)
    except FileNotFoundError:
        flashcards_data = []

    flashcards_data.append(x.to_dict())

    with open("flashcards.json", "w") as file:
        json.dump(flashcards_data, file, indent=4)