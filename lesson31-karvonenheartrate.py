def calcHeartRate(age, restingHR):

    intensity = 55
    header = "Intensity".ljust(13, " ") + "|" + " Rate".ljust(13, " ") + "\n\r" + "".ljust(13, "-") + "|".ljust(13, "-")

    print header

    while intensity <= 95:
        pctIntensity = float(intensity) / 100.0
        targetHR = (((220 - age) - restingHR) * pctIntensity) + restingHR
        thisLine =  (str(intensity) + "%").ljust(13, " ") + "| " + str(targetHR) + " bpm".ljust(13, " ")
        print thisLine


        intensity += 5
    
    



calcHeartRate(22, 65)