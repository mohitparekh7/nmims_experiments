def sum(n):
    x =0
    for i in n:
        x +=i
    print("sum = ",x)
    prime(x)
def prime(x):
    if (x>1):
        for i in range(2,x//2):
            if (x%i==0):
                print("not prime")
                break
        else:
                print("prime")
n = [int(x) for x in input("enter number").split()]
sum(n)