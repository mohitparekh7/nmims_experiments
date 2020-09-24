l1 = [(1,9),(2,9),(3,9)]
l2 = []
print("og list :",l1)
for t in l1:
    l2= l2 + [t[:-1]+(10,)]
print("new list :",l2)