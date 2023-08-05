totalDays = int(input("Enter the number of days : "))

years = totalDays//365
months = (totalDays%365)//30
days = (totalDays%365)%30

print("%1i Years %1i Months %1i Days" %(years,months,days))