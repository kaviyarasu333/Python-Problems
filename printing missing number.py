def miss(lst,lst1,lst2,lst3,a):
    n = int(input())
    lst = []
    lst2 = []
    lst3 = []
    for i in range(0, n):
        lst1 = int(input())
        lst.append(lst1)
    for i in range(0, n):
        a = i + 1
        lst2.append(a)
    for i in lst2:
        if i not in lst:
            lst3.append(i)
    print(lst3)
miss()





