def tip(bill, percentage):
    return bill + bill * (percentage/100)

print ("Your bill is " + str(tip(float(input("What was your bill? ")), float(input("What percentage would you like to tip? ")))))