x = []
while True:
    l = input()
    if l:
        x.append(l)
    else:
        break
print(x)
n = len(x)
#print(n)
mov = 0
i = 0
while(i<n):
    #print("in i ")
    a = x[i]
    ptr = 0
    for j in range(i+1,n):
        #print("in j ")
        if (a > x[j]):
            for k in range (i,n-1):
                #print("in k")
                x[k] , x[k+1] = x[k+1] , x[k]
            mov = mov +1
            ptr += 1
            break
        else:
            continue
    if (ptr == 0 ):
        i += 1
print(x)
print(mov)

