import json
x = input("Teacher or Student")

if x == "Teacher":
    class Teacher:
        def __init__(self, word, answer):
            self.word= word
            self.answer= answer

        def flashcards(self):
            return f"{self.word}"
    
words= Teacher(input("Tell me a word: ")), input("Give me an answer: ")
print(words.flashcards())