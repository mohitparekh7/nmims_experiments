p, ar = [], []
n = 3
m = 4
c = [[3, 2, 2], [6, 1, 3], [3, 1, 4], [4, 2, 2]]
#a=[[1,0,0],[6,1,2],[2,1,1],[0,0,2]] #Safe
a = [[2, 0, 1], [5, 1, 1], [2, 1, 1], [0, 0, 2]]  # Unsafe
r = [9, 3, 6]
print(c, "\n",a,"\n", r, )

print("Pending requests: ")
for i in range(m):
    l = []
    for j in range(n):
        l.append(c[i][j] - a[i][j])
    p.append(l)
print(p)

print("Available resources:")
for i in range(n):
    s = 0
    for j in range(m):
        s += (a[j][i])
    ar.append(r[i] - s)
print(ar)

v = []
print("")
while (True):
    s,w=0,0
    f=True
    for i in range(m):
        d = 0
        if (i not in v):
            for j in range(n):
                if (ar[j] >= p[i][j]):
                    d += 1
                else:
                    f=False
            if (d == 3):
                for j in range(n):
                    ar[j] = (ar[j] + a[i][j])
                    c[i][j] = 0
                    a[i][j] = 0
                    p[i][j] = 0
                v.append(i)
                f=True
                print(ar)
                print(c)
                print(a)
                print(p, "\n")
                break

    for i in range(m):
        s = sum(p[i])
        if (s != 0):
            w += 1
    if (w== 0 or f==False):
        break

d = 0
for i in range(m):
    s = sum(p[i])
    if s == 0:
        d += 1
if d == m:
    print("Safe State")
    print("Safe sequence:",v)
else:
    print("Unsafe State")

