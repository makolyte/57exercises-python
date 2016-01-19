import random

names = []

while True:
    input = raw_input("Enter a name: ")
    if input == "":
        if len(names) == 0:
            print "No names to choose from"
        else:
            winner = names.pop(random.randint(0, len(names) - 1))
            print "Winner: " + winner
    else:
        names.append(input)