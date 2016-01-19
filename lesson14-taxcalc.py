orderAmt = int(raw_input("What is the order amount?"))
state = raw_input("What is the state?")
tax = 0

if state.upper() == "WI":
    tax = orderAmt * 0.055

print """
Subtotal is {0}
Tax is {1}
Total is {2}
""".format(orderAmt, tax, orderAmt + tax)
