import random

minLen = 100
specialCharsLen = 20
numbersLen = 20

specialCharsList = []
numbersList = []
alphas = []

def putStuff(start, end, list):
    for i in range (start, end):
        list.append(chr(i))

def putPasswords(neededLen, sourceList, passwordList):
     for i in range(1, neededLen):
        char = sourceList[random.randint(0, len(sourceList) - 1)]

        index = random.randint(0, len(password) - 1)
        password.insert(index, char)

putStuff(33, 47, specialCharsList)
putStuff(58, 64, specialCharsList)
putStuff(123,126, specialCharsList)
putStuff(48, 57, numbersList)
putStuff(65, 122, alphas)


password = ['']
putPasswords(minLen, alphas, password)
putPasswords(specialCharsLen, specialCharsList, password)
putPasswords(numbersLen, numbersList, password)

print ''.join(password)











