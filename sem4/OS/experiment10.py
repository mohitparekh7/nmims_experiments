n=int(input("Enter total no of tracks:"))
l=list(int (i) for i in input("Enter the tracks to read:").split())
a=int(input("Enter initial position of head:"))
d,a1=[],a

print("\nFCFS:")
for i in range(len(l)):
    if a>l[i]:
        d.append(a-l[i])
    else:
        d.append(l[i]-a)
    a=l[i]
print("Order of traversal:",l)
print("Number of Tracks traversed:",d)
print("Average seek length:",(sum(d)/len(d)))

d1,b=[],[]
print("\nSSTF:")
for i in range(len(l)):
    e=[]
    for j in range(len(l)):
       if l[j] not in b: 
        if l[j]>a1:
            e.append(l[j]-a1)
        else:
            e.append(a1-l[j])
       else:
           e.append(0)
    m=max(e)
    for j in e:
        if j!=0 and j<m:
            m=j
    m=e.index(m)
    if a1>l[m]:
        d1.append(a1-l[m])
    else:
        d1.append(l[m]-a1)
    b.append(l[m])
    a1=l[m]
print("Order of traversal:",b)
print("Number of Tracks traversed:",d1)
print("Average seek length:",(sum(d1)/len(d1)))
