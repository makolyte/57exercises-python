count = 0
sum = 0
while True:
    if count == 5:
        break

    try:
        nextNum = float(raw_input("next num? "))
        sum += nextNum
    except:
        donothing = 0
    count += 1

print "SUm= %d" % sum
    
