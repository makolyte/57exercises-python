def namesFilledIn(name):
    if len(name) == 0:
        return False
    return True

def namesAtLeast2(name):
    if len(name) < 2:
        return False
    return True

def validID(ID):
    length = len(ID)
    if length != 7:
        print "ID Not the right length"
        return False

    if "-" not in ID:
        print "No hyphen in ID"
        return False

    split = ID.split('-')
    left = split[0]
    right = split[1]

    if len(left) != 2:
        print "left side of the hyphen isn't two long"
        return False

    if len(right) != 4:
        print "right side of the hypen isn't 4 long"
        return False

    if not left.isalpha():
        print "First two digits must be alpha"
        return False

    if not right.isdigit():
        print "Last 4 digits must be digits"
        return False

    return True


def controller(first, last, zip, id):
    if not namesFilledIn(first):
        print "first name isnt filled in"
        return

    if not namesFilledIn(last):
        print "last name isn't filled in"
        return

    if not namesAtLeast2(first):
        print "first name isn't at least 2"

    if not namesAtLeast2(last):
        print "last name isn't at least 2"

    if not validID(id):
        return

    print "It's clean"
    

print controller("", "", 0, "")
print controller("hi", "h", 0, "")
print controller("hi", "ha", 0, "hi1234") 
print controller("hi", "ha", 0, "hi1-234") 
print controller("hi", "ha", 0, "h1-1234") 
print controller("hi", "ha", 0, "hi-1a34") 

print controller("hi", "ha", 0, "hi-1234") 


