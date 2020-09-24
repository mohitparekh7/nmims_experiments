def first_pri(lt, l1):
    f1, f = lt[0][2], []
    for i in range(len(lt)):
        if lt[i][2] < f1 and (lt[i] not in l1):
            if f == []:
                f = lt[i]
            elif f != [] and lt[i][2] < f[2]:
                f = lt[i]
        else:
            f = lt[0]
        if (len(lt) == 1):
            f = lt[i]
    return f


# input
n = int(input("No of processes"))
l, l1, lt = [], [], []
d = dict()
for i in range(n):
    print("Process no:", i + 1)
    bt = int(input("Burst time:"))
    p = int(input("Priority:"))
    a = int(input("Arrival time:"))
    l.append([i + 1, a, p, bt])

# selection of first job
min = l[0][1]
c = 1000
for i in range(len(l)):

    if l[i][1] <= min and (l[i] not in l1):
        mini = l[i]
        c = l[i][2]
    elif l[i][1] <= mini[1] and c != 1000 and (l[i] not in l1):
        if mini[2] > l[i][2]:
            mini = l[i]
            c = l[i][2]
l1.append(mini)
t = mini[3]

# Other jobs
lt, y = [], []
x = 0
gap = [0]  # to account for the factor if cpu has to wait
while (len(l1) != len(l)):
    lt = []
    if (len(l) == len(l1)):
        break
    for i in range(len(l)):
        if l[i][1] <= t and (l[i] not in l1):
            lt.append(l[i])
    if lt == [] and len(l) != len(l1):
        t = t + 1
        x = x + 1

    if lt != []:
        y = first_pri(lt, l1)
        if y == []:
            break
        else:
            t = t + y[3]
            l1.append(y)
            gap.append(x)
            x = 0
wt, ta, ct, netT, netW = 0, 0, 0, 0, 0
for i in range(len(l1)):
    ct = ct + l1[i][3] + gap[i]
    ta = ct - l1[i][1]
    wt = ta - l1[i][3]
    d.update({l1[i][0]: [ta, wt]})
    netT = netT + ta
    netW = netW + wt

d = dict(sorted(d.items()))

for k, v in d.items():
    print("Process:", k, "turn around time:", v[0], "Waiting time:", v[1])

print("Äverage turn around time:", netT / n, "Average waiting time:", netW / n)
