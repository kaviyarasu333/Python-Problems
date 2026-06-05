a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if a==b==c:
    print("give different numbers")
elif a>=b and a>=c:
    print("first number is greatest")
elif b>=c and b>=a:
    print("second number is greatest")
elif c>a and c>=b:
    print("third number is greatest")