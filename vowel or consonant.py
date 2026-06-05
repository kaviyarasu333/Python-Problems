char=str(input())
vowels=['a','e','i','o','u']
if char.isalpha()==True:
    print('It is a vowel'if char.lower() in vowels else "It's not a vowel")
else:
    print("It's not alphabet")