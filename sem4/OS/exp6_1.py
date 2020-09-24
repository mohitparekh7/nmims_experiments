#without arrival time
n=int(input("Enter the number of processes: "))
qt=int(input("Enter the quantum time: "))
bt,rt,ta,wt=[],[],[],[]

for i in range(n):
    print("process no: ",i+1)
    v=int(input("Burst Time:"))
    bt.insert(i,v)
    rt.insert(i,v)
    ta.insert(i,0)
    wt.insert(i,0)

#print(bt)
#print(rt)
#print(ta)
#print(wt)
t=0
tot=sum(bt)

while(1):
    for i in range(n):
        if(rt[i]>0):
            if(rt[i]>qt):
                t=t+qt
                rt[i]-=qt
            else:
                t+=rt[i]
                rt[i]=0
                ta[i]=t
                wt[i]=ta[i]-bt[i]
    if(t>=tot):
        break

ata=(sum(ta))/n
awt=(sum(wt))/n
print("Burst Times: ",bt)
print("Waiting Times: ",wt)
print("Turn around Times: ",ta)
print("Average Waiting Time: ",awt)
print("Average Turn around Time: ",ata)
