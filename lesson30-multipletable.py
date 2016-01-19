outerNum = 0
while outerNum < 13:
    innerNum = 0
    while innerNum < 13:
        print "{0} x {1} = {2}".format(outerNum, innerNum, outerNum * innerNum)
        innerNum += 1
    outerNum += 1