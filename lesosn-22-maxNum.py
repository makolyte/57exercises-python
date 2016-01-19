first = 0
second = 0
third = 0
maxi = 0

while True:
    first = float(raw_input("first: "))
    maxi = first
    second = float(raw_input("second: "))
    if second == first:
        print "You must enter unqiue values"
        continue
    if (second > maxi):
        maxi = second
    third = float(raw_input("third: "))
    if third == second or third == first:
        print "You must enter a unique value"
        continue
    if (third > maxi):
        maxi = third
    break

print "The largest is " + str(maxi)

