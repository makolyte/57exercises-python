while True:
    weight = float(raw_input("weight? "))
    height = float(raw_input("height? "))
    bmi = (weight / (height * height)) * 703

    print "Your BMI is {0}".format(bmi)

    if bmi < 18.5:
        print "you're underweight"
    elif bmi > 25:
        print "you're obese"
    else:
        print "congrats, you're not gonna die!"
