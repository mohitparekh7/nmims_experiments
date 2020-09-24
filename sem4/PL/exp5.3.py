def pf(n):
    l = []
    for i in range(1,n):
        if(n%i==0):
            l.append(i)
    s = 0
    for i in l:
        s+=i
    if (s==n):
        print("true")
    else:
        print("false")
n = int(input("enter the number : "))
pf(n)
