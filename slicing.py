hello = "Hello World"

print "hello[:] prints [{0}]".format(hello[:])

#This won't throw an 'index out of range' exception
print "hello[500:] prints [{0}]".format(hello[500:])

#Neither will this
print "hello[0:500] prints [{0}]".format(hello[0:500])

#from 0 to 5
print "hello[:5] prints [{0}]".format(hello[:5])

#every other character
print "hello[::2] prints [{0}]".format(hello[::2])

#reversed
print "hello[::-1] prints [{0}]".format( hello[::-1])

