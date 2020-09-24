print("welcome mohit")
def lower(n,m):
    for i in range(n):
        for j in range(n):
            if(i<j):
                print("0",end=" ")
            else:
                print(m[i][j],end=" ")
        print("  ")

l=[[1,2,3],[4,5,6],[7,8,9]]
n = 3
print("orignal list")
for i in range(n):
    for j in range(n):
        print(l[i][j],end=" ")
    print(" ")
print("new matrix:")
lower(n,l)
