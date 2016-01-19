
while True:
    try:
        rate = float(raw_input("rate?"))
        if rate == 0:
            print "Can't enter 0"
            continue
    except:
        print "you must enter a number"

    print "Double your investment in {0} years".format(72 / rate)
        
