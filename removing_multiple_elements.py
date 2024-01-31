n=int(input("enter the number of elements"))
lst=[]
for i in range(0,n):
    a=int(input())
    lst.append(a)
b=int(input("enter the elements to delete"))
lst1=[]
for i in range(0,b):
    c=int(input())
    lst1.append(c)
for i in lst1:
    lst.remove(i)
print(lst)
