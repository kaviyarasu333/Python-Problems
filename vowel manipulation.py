n=input()
vowels=['a','A','e','E','i','I','o','O','u','U']
for i in n:
    if i in vowels:
        new=str(i)*len(n)
# print(new)