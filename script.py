year=int(input("Enter the year"))
if year%4!=0:
    print("not a leap year")
elif year%100!=0:
    print("it's leap year")
elif year%400==0:
    print("it's a leap year")
else:
    print("it's not a leap year")