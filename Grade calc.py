mark=input()
if mark.isdigit()==True:
    if int(mark)>100:
        print("Enter the valid mark")
    elif int(mark)>90:
        print("A+")
    elif int(mark)>=80:
        print("A")
    elif int(mark)>=70:
        print("B")
    elif int(mark)>=60:
        print("C")
    elif int(mark)>=50:
        print("D")
    else:
        print("Sorry you Failed")
else:
    print("Enter the marks in number")