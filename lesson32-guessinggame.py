import random
import math

class GuessGame():
    CORRECT = 0
    HIGHER = 1
    LOWER = -1
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.max = int(math.pow(10, difficulty))
        self.number = random.randint(1, self.max)
        self.guesses = 0

    def guess(self, guess):
        self.guesses += 1
        if guess == self.number:
            return GuessGame.CORRECT
        elif guess < self.number:
            return GuessGame.HIGHER
        else:
            return GuessGame.LOWER



def strategy_binarySearch():
    MAX_GUESSES = 100
    guessGame = GuessGame(3)
    ceiling = guessGame.max
    floor = 0
    while guessGame.guesses < MAX_GUESSES:

        myGuess = (ceiling + floor)/2
        print "Floor={0} Ceiling={1}. My guess is {2}".format(floor, ceiling, myGuess)
        result = guessGame.guess(myGuess)
        if result == GuessGame.CORRECT:
            print "I got it correct in {0} guesses".format(guessGame.guesses)
            return
        elif result == guessGame.HIGHER:
            print "The answer is higher"
            floor = myGuess
        else:
            print "The answer is lower"
            ceiling = myGuess

        print ""

strategy_binarySearch()
