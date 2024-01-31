lst=("a","e","i","o","u")
a=input()
for i in a:
    if i in lst:
        print(i,end="")
        b=a.delete(i)
print(a)