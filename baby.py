from random import choice

questions = ["Why is water blue?: ", "Why do we need oxigen?: ",
             "Why do we need strings?: "]

question = choice(questions)

answer = input(question).strip().lower()

while answer != "just because":
    answer = input("why?: ").strip().lower()

print("Oh ...ok")
