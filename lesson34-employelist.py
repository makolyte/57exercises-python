def printEmployes(empList):
    print "There are {0} employees".format(len(empList))
    for emp in empList:
        print emp

employees = [
    "Mac", "Yasmin", "Gail", "Linda", "Doug", "Trevor", "Kalvin", "Susan"
]

while True:
    printEmployes(employees)
    remove = raw_input("Who do you wanna remove?")
    if remove in employees:
        employees.remove(remove)
        print "Removed {0}".format((remove));
    else:
        print "Couldn't find them"
