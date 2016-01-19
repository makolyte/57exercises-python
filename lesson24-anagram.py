def isAnagram(word1, word2):
    if len(word1) != len(word2):
        return False;

    for char in word1:
        if char not in word2:
            print char + " not in " + word2
            return False;

    return True;



assert isAnagram("note", "tone")
assert not isAnagram("note", "dummmmmmm")
assert isAnagram("noter", "tonem")
