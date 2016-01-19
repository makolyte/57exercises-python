from math import log, pow
def monthsToPayOff(balance, monthlyPayment, APR):
    leftSide = (1/-30)
    dailyRate = APR / 365
    denom = log(1 + dailyRate)

    #inside
    power = pow(1 + APR, 30)
    print power
    numer = log(1 + (balance / monthlyPayment) * (1 - power))
    

    return leftSide  * (numer / denom)


print monthsToPayOff(5000, 100, 12)
