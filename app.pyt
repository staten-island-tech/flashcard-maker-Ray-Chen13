import json

x = input("Would you like to enter Teacher or Student mode: ")

class Flashcards:
    def __init__(self, word, answer):
        self.word = word
        self.answer = answer

    def display_info(self):
        return {"Question": self.word, "Answer": self.answer}

    def to_dict(self):
        return {"word": self.word, "answer": self.answer}

if x == "Teacher":
    class Teacher:
        def __init__(self, word, answer):
            self.word = word
            self.answer = answer

    y = Flashcards(input("Tell me a word: "), input("Give me an answer: "))

    try:
        with open("flashcards.json", "r") as file:
            flashcards_data = json.load(file)
    except FileNotFoundError:
        flashcards_data = []
    flashcards_data.append(y.to_dict())

    with open("flashcards.json", "w") as file:
        json.dump(flashcards_data, file, indent=4)

    x = input("Would you like to enter Teacher or Student mode: ")

if x == "Student":
    with open("./flashcards.json", encoding="utf8") as Flashcard:
        data = json.load(Flashcard)

    class Student:
        def __init__(self, tally):
            self.tally = tally

        def streak(self):
            return f"tally"

    y = input("Continue? ")

    play = 0  

    while y == "Yes":
        for flashcard in data:  
            print(flashcard["word"])
            b = input("What's the answer? ")
            if b == flashcard["answer"]:
                print("Correct")
                play += 1 
            else:
                print("Incorrect")
                break 

            y = input("Would you like to Continue? ")
            if y != "Yes":
                break 