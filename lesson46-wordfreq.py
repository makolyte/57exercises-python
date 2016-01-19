wordfreqs = {}

with open("hello/words.txt", 'r') as wordsFile:
    for line in wordsFile.readlines():
        line = line.rstrip('\n')
        for word in line.split(" "):
            if not wordfreqs.has_key(word):
                wordfreqs[word] = 0
            wordfreqs[word] += 1


print wordfreqs