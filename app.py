import json

def save_flashcards(flashcards_data):
    with open("FlashCards.json", "w") as file:
        json.dump(flashcards_data, file, indent=4)  

def load_flashcards(flashcards_data):
    try:
        with open("FlashCards.json", "r") as file:
            return json.file(file)
    except FileNotFoundError:
        return []

x = input("Would you like to enter Teacher or Student: ")

while x != "Exit":
    if x == "Teacher":
        class Teacher:
            def __init__(self, word, answer):
                self.word= word
                self.answer= answer

            def flashcards(self):
                return f"{self.word}: {self.answer}"
    
        words = Teacher(input("Tell me a word: "), input("Give me an answer: "))
        print(words.flashcards())

        flashcards_data = load_flashcards()

        word = input("Tell me a word: ")
        answer = input("Give me an answer: ")

        new_flashcard = Teacher(word,answer)

        flashcards_data.append({"word": word, "answer": answer})

        save_flashcards(flashcards_data)

