n = int(input("enter the number of processes"))
d = dict()
ta , wt = 0,0
l = []
total_ta , total_wt = 0,0
for i in range(n):
    print("process no:",i+1)
    pr=int(input("enter the priority of process"))
    bt=int(input("enter the burst time of process"))
    d.update({pr:bt})
d1=dict(sorted(d.items()))
print(d1)
for k,v in d1.items():
    ta = ta + v
    wt = ta - v
    l.append([ta,wt])
    total_ta +=ta
    total_wt +=wt
print(l)
ata = total_ta/n
awt = total_wt/n
print("average turn around: ",ata)
print("average waiting time: ",awt)
