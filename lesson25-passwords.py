hello = "hello"

def passwordStrength(password):
    numCount = 0; #8 char
    letterCount = 0; #8 char
    specialCharCount = 0; #8 char
    length = len(password)

    for char in password:
        if char.isdigit():
            numCount = numCount + 1
        elif char.isalpha():
            letterCount = letterCount + 1
        else:
            specialCharCount = specialCharCount + 1

    if numCount == length:
        return "very weak"
    elif letterCount == length:
        return "weak"
    elif (numCount + letterCount) == length:
        return "strong"
    else:
        return "very strong"
    
print passwordStrength("12345")
print passwordStrength("abcdef")
print passwordStrength("abc123xyz")
print passwordStrength("1337h@xor!")
