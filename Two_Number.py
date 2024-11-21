list=[1,2,3,4,5,6,7,8,9,]
x=int(input())
y=int(input())
a=0
b=0
for i in list:
    for j in range(1,len(list)):
        if i+j==x:
            if i-j==y:
                a+=i
                b+=j
print(a*b)
