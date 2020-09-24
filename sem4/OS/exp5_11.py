n = int(input("enter the number of processes:"))
l1 = dict()
l2 = dict()
l3 = dict()

for i in range(n):
    print("process no: ",i+1)
    at = int(input("enter the arrival time : "))
    bt = int(input("enter the burst time : "))
    pr = int(input("enter the priority:"))
    l1.update({i+1:at})
    l2.update({i+1:bt})
    l3.update({i+1:pr})

#print(l1)
#print(sorted(l1.items(), key=lambda kv:(kv[1], kv[0])))
#print(l2)
#print(l3)

d1 = dict(sorted(l1.items(), key=lambda kv:(kv[1], kv[0])))
ta = 0
l = []
total_ta = 0
total_wt = 0
d2 = {}


for k,v in d1.items():
    ta = ta + l2[k]
    wt = ta - l2[k]
    l.append([k,ta, wt])
    total_ta += ta
    total_wt += wt

print("process no , turnaround time, waiting time")
print(l)
print("average turnaround time:",total_ta/n)
print("average waiting time:",total_wt/n)