l1 = []
for i in range(3):
    x = int(input("enter value"))
    if(x in l1):
        continue
    else:
        l1 = l1 + [x, ]
print(l1)