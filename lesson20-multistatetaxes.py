def getTax(state, county):
    if state == "WI":
        if county == "eau":
            return 0.005
        elif county == "dunn":
            return 0.004
    elif state == "IL":
        return 0.08

    return 0

while True:
    state  = raw_input("state?" )
    county = raw_input("county?")

    taxMultipler = getTax(state, county)

    order = 10.00
    tax = order * taxMultipler
    total = order + tax
    print """
        Order = {0}
        Tax = {1}
        Total = {2}""".format(order, tax, total)


            
