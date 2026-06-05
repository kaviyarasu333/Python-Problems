n=int(input("Enter the number"))
type=str(n)
i=0
while type.isdigit()==True:
   if type[i]=="+" or type[i]=="-":
       i+=0
   else:
       i+=1
   if len(type)==i:
       break
print(i)