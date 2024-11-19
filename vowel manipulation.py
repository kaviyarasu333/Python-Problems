n=input()
initial=''
vowels=['a','A','e','E','i','I','o','O','u','U']
for i in n:
    if i in vowels:
        initial+=i
        break
for i in n:
    if i not in vowels:
        n=n.replace(i,initial)
print(n)