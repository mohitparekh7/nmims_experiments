def table(n):
    if(n!=0):
        return 8 + table(n-1)
    else:
        return 0
n = int(input("enter the number "))
for i in range (1,n+1):
    print(table(i),end=" ")