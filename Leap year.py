year = int(input("Enter a year : "))

if (year%400 == 0 or (year%4 == 0 and year%100 != 0)):
    print("%1i is a Leap Year" %(year))
else:
    print("%1i is not a Leap Year" %(year))