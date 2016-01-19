if raw_input("Is the car silent when you turn the key?") == "y":
    if raw_input("Are the battery terminals corroded?") == "y":
        print "Clean terminals and try starting again"
    else:
        print "Replace cables and try again"
else:
    print "I'm too lazy to type the rest of the bullcrap"
