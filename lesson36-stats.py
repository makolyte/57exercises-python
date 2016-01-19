import math

def calcMean(numbers):
    return  sum(numbers) / float(len(numbers))

def calcStdDev(numbers, mean):
    variances = []
    for n in numbers:
        variance = pow(n - mean, 2)
        print variance
        variances.append(variance)

    print sum(variances)
    mean = sum(variances) / float(len(variances) - 1)

    return math.sqrt(mean)

def calcStats(numbers):
   mean = calcMean(numbers)
   minv = min(numbers)
   maxv = max(numbers)
   stddev = calcStdDev(numbers, mean)

   print """
   mean={0}
   min={1}
   max={2}
   stddev={3}
   """.format(mean, minv, maxv, stddev)

numbers = [100, 200, 1000, 300]
calcStats(numbers)
