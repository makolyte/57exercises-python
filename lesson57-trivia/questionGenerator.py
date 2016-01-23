FILE_NAME = "question.fssv" #file separator separated values, haha

class Question():
    SEPARATOR = chr(28) #File Separator char, since i won't type that in
    def __init__(self):
        """
        :param choices is a list of choices. For simplicity,  I will only verify that the answer is in the choices
        :param answerNumber: choices[answerNumber-1] is the answer. It's -1 because choices are displayed in 1-based index
        """
        self.questionText = ""
        self.choices = []
        self.answerNum = 0

    def SaveToFile(self):
        choiceStr = ""
        for choice in self.choices:
            choiceStr += choice + Question.SEPARATOR

        output = "{1}{0}{2}{0}{3}\n".format(Question.SEPARATOR, self.questionText,self.answerNum, choiceStr)

        with open(FILE_NAME, 'a+') as questionFile:
            questionFile.write(output)

    @staticmethod
    def ParseFromFileLine(fileLine):
        arr = filter(None, fileLine.rstrip('\n').split(Question.SEPARATOR ))
        question = Question()
        question.questionText = arr[0]
        question.answerNum = int(arr[1])
        for choice in arr[2:]:
            question.choices.append(choice)

        return question

    def ToString(self):
        choiceStr = ""
        for i,choice in enumerate(self.choices):
            choiceStr += "\t{0}. {1}\n".format(i+1, choice)

        return "Question: {0}\n{1}".format(self.questionText, choiceStr)


def genQuestions():
    question1 = Question()
    question1.questionText = "What color is the sky?"
    question1.choices = ["blue", "red", "potato", "yellow"]
    question1.answerNum = 1
    question1.SaveToFile()

    #gen more questions, but i don't feel like typing them all in.

def askQuestion(question):
    try:
         answer = int(raw_input(question.ToString()))
         if answer == question.answerNum:
             print "right!"
         else:
             print "wrong! Didn't you pay attention in trivia class?"
    except ValueError:
        print "You didn't put in a valid choice, so I'm just gonna mark you wrong on that one"

def getAllQuestions():
    questions = []
    try:
        with open(FILE_NAME, 'r') as questionFile:
            for questionLine in questionFile.readlines():
                question = Question.ParseFromFileLine(questionLine)
                questions.append(question)

    except IOError:
        return None

    return questions

def gameLoop():
    INVALID_INPUT = "oops, you need to enter 1 or 2"

    while True:
        try:
            choice = int(raw_input( "What do you wanna do?\n\t1 - gen Questions\n\t2 - play game\n"))
            if choice == 1:
                genQuestions()
                print "questions generated!"
            elif choice == 2:
                questions = getAllQuestions()
                if not questions:
                    print "you need to add questions if you wanna play, come on!"
                    continue

                for question in questions:
                    askQuestion(question)
            else:
                print INVALID_INPUT
        except ValueError:
            print INVALID_INPUT


gameLoop()




