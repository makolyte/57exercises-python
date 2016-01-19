wordsToReplace = {"utilize" : "use"}

oldFileName = "hello/dummy.txt"
newFileName = "hello/dummyNew.txt"

def genFile():

    with open(oldFileName, 'a+') as f:
        f.writelines("One should never utilize the word 'utilize' in writing. Use 'use' instead")

def replacer():
    newFile = ""
    with open(oldFileName, 'r') as f:
        for line in f.readlines():
            for key in wordsToReplace:
                newFile += line.replace(key, wordsToReplace[key]);


    with open(newFileName, 'a+') as f:
        f.write(newFile)



