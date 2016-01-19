import random
answers = ["Yes", "No", "Maybe", "Ask again later"]

while True:
    raw_input("WHat's your question? ")
    print answers[random.randint(0, len(answers) - 1)]