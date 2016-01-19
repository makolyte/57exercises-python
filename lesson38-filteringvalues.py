input = ""
for i in range(1, 101):
    input += str(i) + " "

inputArr = input.split(" ")
filteredList = []
for integer in inputArr:
    print "integer={0}".format(integer)
    if integer != "":

        if int(integer) % 2 == 0:
            filteredList.append(integer)

print " ".join(filteredList)