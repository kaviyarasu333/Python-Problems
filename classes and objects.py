class Student:
    def __init__(self):
        self.name="kavi"
        self.roll_number=90
        self.marks=80
    def grade_calc(self):
        if self.marks>=90:
            return "A"
        elif self.marks>=80:
            return "B"
        elif self.marks>=70:
            return "C"
        elif self.marks>=60:
            return "D"
        else:
            return "Sorry you've Failed"
    def __str__(self):
        return f"Name: {self.name},Roll:{self.roll_number},Marks:{self.marks},Grade:{self.grade_calc()}"
Student.name=input("Enter the name")
Student.roll_number=int(input("Enter the roll_number"))
Student.marks=int(input("Enter the marks"))
studend=Student()
print(studend)
#or
"""name=input()
roll_number=int(input())
marks=int(input())
obj=Student(name,roll_number,marks)
print(obj)
"""