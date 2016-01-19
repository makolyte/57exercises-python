def convertCtoF(C):
    #do shiz
    F = (C * 9/5) + 32
    print "{0} C is {1} F".format(C, F)
def convertFtoC(F):
    #do shiz
    C = (F - 32) * 5/9
    print "{0} F is {1} C".format(F, C)

while True:
    tempType = raw_input("C/F? ").upper()
    temp = float(raw_input("what's temp? "))

    if tempType == "C":
        convertCtoF(temp)
    elif tempType == "F":
        convertFtoC(temp)
    else:
        print "Enter C or F"
    
